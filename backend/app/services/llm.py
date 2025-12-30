from typing import Optional, List
import asyncio
import logging
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from app.config import get_settings

logger = logging.getLogger(__name__)


class GeminiLLM:
    """Google Gemini API LLM Service"""
    
    def __init__(self, api_key: str, model: str = "gemini-1.5-flash"):
        self.api_key = api_key
        self.model_name = model
        self._model = None
        self._initialized = False
    
    def _initialize(self):
        if self._initialized:
            return
        
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.api_key)
            self._model = genai.GenerativeModel(self.model_name)
            self._initialized = True
            logger.info(f"Gemini model '{self.model_name}' initialized successfully")
        except ImportError:
            raise ImportError("google-generativeai package not installed. Run: pip install google-generativeai")
        except Exception as e:
            logger.error(f"Failed to initialize Gemini: {e}")
            raise
    
    async def generate(
        self,
        prompt: str,
        system_prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 8192,
        **kwargs
    ) -> str:
        self._initialize()
        
        # Combine system prompt and user prompt for comprehensive response
        full_prompt = f"""## SYSTEM INSTRUCTIONS
{system_prompt}

## USER REQUEST
{prompt}

## IMPORTANT
- Provide a COMPREHENSIVE, DETAILED response
- Include ALL sections mentioned in the system instructions
- Use proper Markdown formatting with headers, tables, code blocks
- Minimum 1500 words for thorough coverage
- Be specific and actionable, not generic
- Include real-world examples and specific recommendations"""
        
        # Run in executor since Gemini SDK is synchronous
        loop = asyncio.get_event_loop()
        try:
            response = await loop.run_in_executor(
                None,
                lambda: self._generate_sync(full_prompt, temperature, max_tokens)
            )
            return response
        except Exception as e:
            logger.error(f"Gemini generation error: {e}")
            raise
    
    def _generate_sync(self, prompt: str, temperature: float, max_tokens: int) -> str:
        import google.generativeai as genai
        
        try:
            # Use maximum available tokens for comprehensive responses
            generation_config = genai.GenerationConfig(
                temperature=temperature,
                max_output_tokens=65536,  # Maximum for gemini-2.5-flash
                top_p=0.95,
                top_k=40,
            )
            
            # Safety settings to avoid blocking
            safety_settings = [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
            ]
            
            response = self._model.generate_content(
                prompt,
                generation_config=generation_config,
                safety_settings=safety_settings,
            )
            
            # Check for blocked content or empty response
            if not response.parts:
                logger.warning("Gemini returned empty response")
                if response.prompt_feedback:
                    logger.warning(f"Prompt feedback: {response.prompt_feedback}")
                return "I apologize, but I couldn't generate a response for this request. Please try rephrasing your question."
            
            # Get full text response
            full_text = response.text
            
            # Log response length for debugging
            logger.info(f"Generated response length: {len(full_text)} characters")
            
            return full_text
        except Exception as e:
            logger.error(f"Gemini API error: {type(e).__name__}: {e}")
            raise


class LocalEmbeddings:
    """Local sentence-transformers embeddings"""
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self._model = None
    
    def _load_model(self):
        if self._model is not None:
            return
        
        from sentence_transformers import SentenceTransformer
        self._model = SentenceTransformer(self.model_name)
        logger.info(f"Embedding model '{self.model_name}' loaded")
    
    def encode(self, texts: List[str]) -> List[List[float]]:
        self._load_model()
        embeddings = self._model.encode(texts, convert_to_numpy=True)
        return embeddings.tolist()


class LLMService:
    """Main LLM Service using Gemini API"""
    
    def __init__(self):
        self.settings = get_settings()
        self._llm: Optional[GeminiLLM] = None
        self._embeddings: Optional[LocalEmbeddings] = None
    
    async def initialize(self):
        """Initialize the LLM service"""
        if not self.settings.gemini_api_key:
            logger.warning("GEMINI_API_KEY not set. LLM features will not work.")
            return
        
        try:
            self._llm = GeminiLLM(
                api_key=self.settings.gemini_api_key,
                model=self.settings.gemini_model,
            )
            # Test initialization
            self._llm._initialize()
            logger.info("✓ Gemini LLM service initialized")
        except Exception as e:
            logger.error(f"✗ Failed to initialize Gemini: {e}")
            raise
    
    @property
    def llm(self) -> GeminiLLM:
        if self._llm is None:
            if not self.settings.gemini_api_key:
                raise ValueError("GEMINI_API_KEY not configured. Please add it to your .env file.")
            self._llm = GeminiLLM(
                api_key=self.settings.gemini_api_key,
                model=self.settings.gemini_model,
            )
        return self._llm
    
    @property
    def embeddings(self) -> LocalEmbeddings:
        if self._embeddings is None:
            self._embeddings = LocalEmbeddings(self.settings.embedding_model)
        return self._embeddings
    
    async def generate(
        self,
        prompt: str,
        system_prompt: str,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> str:
        temperature = temperature or self.settings.temperature
        max_tokens = max_tokens or self.settings.max_new_tokens
        
        return await self.llm.generate(
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
    
    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        return self.embeddings.encode(texts)


# Global instance
llm_service = LLMService()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.config import get_settings
from app.api.routes import router as api_router
from app.services.cache import CacheService
from app.services.knowledge_base import KnowledgeBaseService
from app.services.llm import llm_service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    
    logger.info("=" * 50)
    logger.info("Starting PromptCraft AI Backend (Gemini)")
    logger.info("=" * 50)
    logger.info(f"Gemini Model: {settings.gemini_model}")
    
    try:
        await llm_service.initialize()
        logger.info("✓ Gemini LLM service initialized")
    except Exception as e:
        logger.error(f"✗ Failed to initialize Gemini: {e}")
        logger.info("Please check your GEMINI_API_KEY in .env")
    
    try:
        app.state.cache = CacheService(settings.redis_url)
        logger.info("✓ Cache service initialized")
    except Exception as e:
        logger.warning(f"Cache service unavailable: {e}")
        app.state.cache = None
    
    try:
        app.state.knowledge_base = KnowledgeBaseService()
        await app.state.knowledge_base.initialize()
        logger.info("✓ Knowledge base initialized")
    except Exception as e:
        logger.warning(f"Knowledge base initialization error: {e}")
        app.state.knowledge_base = None
    
    logger.info("=" * 50)
    logger.info("Backend ready! API available at /api/v1")
    logger.info("=" * 50)
    
    yield
    
    if app.state.cache:
        await app.state.cache.close()
    logger.info("Backend shutdown complete")


def create_app() -> FastAPI:
    settings = get_settings()
    
    app = FastAPI(
        title="PromptCraft AI Backend",
        description="AI-powered system architecture and UI design assistant - Powered by Gemini",
        version="1.0.0",
        lifespan=lifespan,
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.include_router(api_router, prefix="/api/v1")
    
    return app


app = create_app()


@app.get("/health")
async def health_check():
    settings = get_settings()
    return {
        "status": "healthy",
        "service": "promptcraft-backend",
        "llm": "gemini",
        "model": settings.gemini_model,
        "version": "1.0.0"
    }

from typing import List, Dict, Any, Optional
import json
import numpy as np
import logging

from app.config import get_settings
from app.knowledge.system_architectures import SYSTEM_ARCHITECTURES
from app.knowledge.design_patterns import DESIGN_PATTERNS
from app.knowledge.tech_stacks import TECH_STACKS
from app.services.llm import llm_service

logger = logging.getLogger(__name__)


class SimpleVectorStore:
    """Simple in-memory vector store using numpy - no external dependencies"""
    
    def __init__(self):
        self.documents: List[str] = []
        self.metadatas: List[Dict] = []
        self.ids: List[str] = []
        self.embeddings: Optional[np.ndarray] = None
    
    def add(self, documents: List[str], metadatas: List[Dict], ids: List[str]):
        """Add documents to the store"""
        self.documents.extend(documents)
        self.metadatas.extend(metadatas)
        self.ids.extend(ids)
        
        # Generate embeddings
        new_embeddings = llm_service.get_embeddings(documents)
        new_embeddings_np = np.array(new_embeddings)
        
        if self.embeddings is None:
            self.embeddings = new_embeddings_np
        else:
            self.embeddings = np.vstack([self.embeddings, new_embeddings_np])
        
        logger.info(f"Added {len(documents)} documents to vector store")
    
    def query(
        self,
        query_text: str,
        n_results: int = 5,
        where: Optional[Dict] = None
    ) -> Dict[str, List]:
        """Query the store for similar documents"""
        if self.embeddings is None or len(self.documents) == 0:
            return {"documents": [[]], "metadatas": [[]], "distances": [[]]}
        
        # Get query embedding
        query_embedding = np.array(llm_service.get_embeddings([query_text])[0])
        
        # Calculate cosine similarity
        similarities = np.dot(self.embeddings, query_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding)
        )
        
        # Apply filter if specified
        valid_indices = list(range(len(self.documents)))
        if where:
            valid_indices = [
                i for i, meta in enumerate(self.metadatas)
                if all(meta.get(k) == v for k, v in where.items())
            ]
        
        if not valid_indices:
            return {"documents": [[]], "metadatas": [[]], "distances": [[]]}
        
        # Get top results from valid indices
        valid_similarities = [(i, similarities[i]) for i in valid_indices]
        valid_similarities.sort(key=lambda x: x[1], reverse=True)
        top_indices = [x[0] for x in valid_similarities[:n_results]]
        
        return {
            "documents": [[self.documents[i] for i in top_indices]],
            "metadatas": [[self.metadatas[i] for i in top_indices]],
            "distances": [[1 - similarities[i] for i in top_indices]],  # Convert similarity to distance
        }
    
    def count(self) -> int:
        return len(self.documents)


class KnowledgeBaseService:
    def __init__(self):
        self.settings = get_settings()
        self._store: Optional[SimpleVectorStore] = None
        self._initialized = False
    
    async def initialize(self):
        if self._initialized:
            return
        
        self._store = SimpleVectorStore()
        
        try:
            await self._populate_knowledge_base()
            self._initialized = True
            logger.info("✓ Knowledge base initialized with in-memory vector store")
        except Exception as e:
            logger.error(f"Failed to initialize knowledge base: {e}")
            # Still mark as initialized so app can start
            self._initialized = True
    
    async def _populate_knowledge_base(self):
        documents = []
        metadatas = []
        ids = []
        
        for arch_id, arch in SYSTEM_ARCHITECTURES.items():
            doc = f"System: {arch['name']}\n\n{arch['description']}\n\n"
            doc += f"Scale: {arch['scale']}\n"
            doc += f"Key Components: {', '.join(arch['components'])}\n"
            doc += f"Technologies: {json.dumps(arch['technologies'])}\n"
            doc += f"Patterns: {', '.join(arch['patterns'])}\n"
            doc += f"Use Cases: {', '.join(arch['use_cases'])}"
            
            documents.append(doc)
            metadatas.append({
                "type": "architecture",
                "name": arch["name"],
                "scale": arch["scale"],
            })
            ids.append(f"arch_{arch_id}")
        
        for pattern_id, pattern in DESIGN_PATTERNS.items():
            doc = f"Pattern: {pattern['name']}\n\n{pattern['description']}\n\n"
            doc += f"When to use: {pattern['when_to_use']}\n"
            doc += f"Benefits: {', '.join(pattern['benefits'])}\n"
            doc += f"Considerations: {', '.join(pattern['considerations'])}"
            
            documents.append(doc)
            metadatas.append({
                "type": "pattern",
                "name": pattern["name"],
                "category": pattern.get("category", "general"),
            })
            ids.append(f"pattern_{pattern_id}")
        
        for stack_id, stack in TECH_STACKS.items():
            doc = f"Tech Stack: {stack['name']}\n\n{stack['description']}\n\n"
            doc += f"Best for: {', '.join(stack['best_for'])}\n"
            doc += f"Components: {json.dumps(stack['components'])}"
            
            documents.append(doc)
            metadatas.append({
                "type": "tech_stack",
                "name": stack["name"],
            })
            ids.append(f"stack_{stack_id}")
        
        if documents:
            self._store.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids,
            )
    
    async def query(
        self,
        query: str,
        n_results: int = 5,
        filter_type: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        if not self._initialized:
            await self.initialize()
        
        where_filter = {"type": filter_type} if filter_type else None
        
        results = self._store.query(
            query_text=query,
            n_results=n_results,
            where=where_filter,
        )
        
        formatted_results = []
        if results and results["documents"]:
            for i, doc in enumerate(results["documents"][0]):
                formatted_results.append({
                    "content": doc,
                    "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                    "distance": results["distances"][0][i] if results.get("distances") else None,
                })
        
        return formatted_results
    
    async def get_architecture_context(self, query: str) -> str:
        results = await self.query(query, n_results=3, filter_type="architecture")
        patterns = await self.query(query, n_results=2, filter_type="pattern")
        
        context = "## Relevant System Architectures:\n\n"
        for r in results:
            context += f"{r['content']}\n\n---\n\n"
        
        context += "\n## Relevant Design Patterns:\n\n"
        for p in patterns:
            context += f"{p['content']}\n\n---\n\n"
        
        return context

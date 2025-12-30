from fastapi import APIRouter, Depends, HTTPException, Request
from typing import Optional
import logging

from app.models.schemas import (
    ChatRequest,
    ChatResponse,
    ArchitectureRequest,
    UIResearchRequest,
    UIResearchResponse,
)
from app.services.agents.architecture_agent import ArchitectureAgent
from app.services.agents.ui_research_agent import UIResearchAgent
from app.services.cache import CacheService
from app.config import get_settings

router = APIRouter()
logger = logging.getLogger(__name__)


def get_cache(request: Request) -> Optional[CacheService]:
    return getattr(request.app.state, 'cache', None)


def get_knowledge_base(request: Request):
    return getattr(request.app.state, 'knowledge_base', None)


async def safe_cache_get(cache: Optional[CacheService], key: str) -> Optional[str]:
    if cache:
        try:
            return await cache.get(key)
        except Exception as e:
            logger.warning(f"Cache get error: {e}")
    return None


async def safe_cache_set(cache: Optional[CacheService], key: str, value: str, ttl: int):
    if cache:
        try:
            await cache.set(key, value, ttl=ttl)
        except Exception as e:
            logger.warning(f"Cache set error: {e}")


@router.post("/chat/architecture", response_model=ChatResponse)
async def architecture_chat(
    request: ArchitectureRequest,
    cache: Optional[CacheService] = Depends(get_cache),
    kb = Depends(get_knowledge_base),
):
    cache_key = f"arch:{hash(request.prompt)}"
    cached = await safe_cache_get(cache, cache_key)
    if cached:
        return ChatResponse(content=cached, cached=True)
    
    try:
        agent = ArchitectureAgent(knowledge_base=kb)
        response = await agent.generate(request.prompt, request.context)
        
        await safe_cache_set(cache, cache_key, response, get_settings().cache_ttl)
        return ChatResponse(content=response, cached=False)
    except Exception as e:
        logger.error(f"Architecture generation error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate response: {str(e)}")


@router.post("/chat/ui", response_model=UIResearchResponse)
async def ui_research_chat(
    request: UIResearchRequest,
    cache: Optional[CacheService] = Depends(get_cache),
):
    cache_key = f"ui:{hash(request.prompt)}"
    cached = await safe_cache_get(cache, cache_key)
    if cached:
        try:
            return UIResearchResponse.model_validate_json(cached)
        except Exception:
            pass  # Continue to generate new response
    
    try:
        agent = UIResearchAgent()
        response = await agent.research(request.prompt, request.industry)
        
        await safe_cache_set(cache, cache_key, response.model_dump_json(), get_settings().cache_ttl)
        return response
    except Exception as e:
        logger.error(f"UI research error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate response: {str(e)}")


@router.post("/chat/database", response_model=ChatResponse)
async def database_chat(
    request: ChatRequest,
    cache: Optional[CacheService] = Depends(get_cache),
    kb = Depends(get_knowledge_base),
):
    cache_key = f"db:{hash(request.prompt)}"
    cached = await safe_cache_get(cache, cache_key)
    if cached:
        return ChatResponse(content=cached, cached=True)
    
    try:
        agent = ArchitectureAgent(knowledge_base=kb)
        response = await agent.generate_database_schema(request.prompt)
        
        await safe_cache_set(cache, cache_key, response, get_settings().cache_ttl)
        return ChatResponse(content=response, cached=False)
    except Exception as e:
        logger.error(f"Database schema generation error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate response: {str(e)}")


@router.post("/chat/api", response_model=ChatResponse)
async def api_design_chat(
    request: ChatRequest,
    cache: Optional[CacheService] = Depends(get_cache),
    kb = Depends(get_knowledge_base),
):
    cache_key = f"api:{hash(request.prompt)}"
    cached = await safe_cache_get(cache, cache_key)
    if cached:
        return ChatResponse(content=cached, cached=True)
    
    try:
        agent = ArchitectureAgent(knowledge_base=kb)
        response = await agent.generate_api_design(request.prompt)
        
        await safe_cache_set(cache, cache_key, response, get_settings().cache_ttl)
        return ChatResponse(content=response, cached=False)
    except Exception as e:
        logger.error(f"API design generation error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate response: {str(e)}")


@router.post("/chat/prompts", response_model=ChatResponse)
async def prompts_chat(
    request: ChatRequest,
    cache: Optional[CacheService] = Depends(get_cache),
):
    cache_key = f"prompts:{hash(request.prompt)}"
    cached = await safe_cache_get(cache, cache_key)
    if cached:
        return ChatResponse(content=cached, cached=True)
    
    try:
        agent = ArchitectureAgent()
        response = await agent.generate_prompt_template(request.prompt)
        
        await safe_cache_set(cache, cache_key, response, get_settings().cache_ttl)
        return ChatResponse(content=response, cached=False)
    except Exception as e:
        logger.error(f"Prompt template generation error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate response: {str(e)}")

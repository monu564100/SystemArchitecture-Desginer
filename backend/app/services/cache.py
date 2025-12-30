import redis.asyncio as redis
from typing import Optional
import json


class CacheService:
    def __init__(self, redis_url: str):
        self.redis_url = redis_url
        self._client: Optional[redis.Redis] = None
    
    async def _get_client(self) -> redis.Redis:
        if self._client is None:
            try:
                self._client = redis.from_url(self.redis_url, decode_responses=True)
                await self._client.ping()
            except Exception:
                self._client = None
        return self._client
    
    async def get(self, key: str) -> Optional[str]:
        try:
            client = await self._get_client()
            if client:
                return await client.get(key)
        except Exception:
            pass
        return None
    
    async def set(self, key: str, value: str, ttl: int = 3600) -> bool:
        try:
            client = await self._get_client()
            if client:
                await client.setex(key, ttl, value)
                return True
        except Exception:
            pass
        return False
    
    async def delete(self, key: str) -> bool:
        try:
            client = await self._get_client()
            if client:
                await client.delete(key)
                return True
        except Exception:
            pass
        return False
    
    async def close(self):
        if self._client:
            await self._client.close()
            self._client = None

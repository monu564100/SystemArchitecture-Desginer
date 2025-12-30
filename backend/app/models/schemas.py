from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from enum import Enum


class CategoryType(str, Enum):
    ARCHITECTURE = "architecture"
    UI = "ui"
    DATABASE = "database"
    API = "api"
    PROMPTS = "prompts"


class ChatRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=5000)
    context: Optional[str] = None


class ArchitectureRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=5000)
    context: Optional[str] = None
    scale: Optional[str] = Field(default="large", description="small, medium, large, enterprise")
    requirements: Optional[List[str]] = None


class UIResearchRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=5000)
    industry: Optional[str] = None
    style_preferences: Optional[List[str]] = None


class ColorPalette(BaseModel):
    primary: str
    secondary: str
    accent: str
    background: str
    text: str
    additional: List[str] = []


class FontRecommendation(BaseModel):
    heading: str
    body: str
    accent: Optional[str] = None
    fallbacks: List[str] = []


class UIInspiration(BaseModel):
    platform_name: str
    description: str
    key_features: List[str]
    url: Optional[str] = None


class UIResearchResponse(BaseModel):
    content: str
    color_palettes: List[ColorPalette]
    fonts: FontRecommendation
    inspirations: List[UIInspiration]
    design_principles: List[str]
    image_suggestions: List[str]
    cached: bool = False


class ChatResponse(BaseModel):
    content: str
    cached: bool = False
    metadata: Optional[Dict[str, Any]] = None


class SystemArchitecture(BaseModel):
    name: str
    description: str
    components: List[Dict[str, Any]]
    data_flow: str
    scalability_patterns: List[str]
    technologies: Dict[str, List[str]]

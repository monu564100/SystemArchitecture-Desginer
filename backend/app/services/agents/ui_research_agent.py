from typing import Optional, List
import json
from app.services.llm import llm_service
from app.models.schemas import UIResearchResponse, ColorPalette, FontRecommendation, UIInspiration
from app.knowledge.ui_knowledge import UI_INSPIRATIONS, INDUSTRY_PALETTES, FONT_PAIRINGS

UI_RESEARCH_SYSTEM_PROMPT = """You are a world-class UI/UX designer and brand strategist with 15+ years of experience at top design agencies (IDEO, Pentagram, Frog Design) and tech companies (Apple, Airbnb, Stripe).

## YOUR MISSION
Provide COMPREHENSIVE UI/UX research and recommendations that a design team could use to create a stunning, conversion-optimized interface. Your responses must be DETAILED, SPECIFIC, and ACTIONABLE.

## RESPONSE FORMAT (JSON)
You MUST return a valid JSON object with this structure. Make the "analysis" field extremely detailed (1000+ words).

{
  "analysis": "YOUR DETAILED MARKDOWN ANALYSIS HERE - THIS MUST BE COMPREHENSIVE",
  "color_palettes": [...],
  "fonts": {...},
  "inspirations": [...],
  "design_principles": [...],
  "image_suggestions": [...]
}

## ANALYSIS SECTION REQUIREMENTS (Mandatory Sections)

Your "analysis" field must include ALL of these sections in Markdown:

### 1. 🎯 EXECUTIVE SUMMARY
- Project understanding
- Target audience profile
- Key design objectives
- Expected business outcomes

### 2. 🔍 COMPETITIVE ANALYSIS
Analyze 5-7 similar successful platforms:
- What they do well
- What could be improved
- Unique differentiators
- Market positioning

### 3. 👥 USER PERSONA & JOURNEY
- Primary user persona (age, goals, pain points)
- User journey mapping
- Key touchpoints
- Emotional considerations

### 4. 🎨 COLOR PSYCHOLOGY DEEP DIVE
- Why each color was chosen
- Psychological impact on users
- Industry conventions
- Accessibility considerations (WCAG AA/AAA)
- Dark mode adaptations

### 5. 🔤 TYPOGRAPHY RATIONALE
- Why these fonts work together
- Readability analysis
- Brand personality alignment
- Font scale recommendations:
  - H1: 48px / 3rem
  - H2: 36px / 2.25rem
  - H3: 24px / 1.5rem
  - Body: 16px / 1rem
  - Small: 14px / 0.875rem
- Line height and spacing

### 6. 📐 LAYOUT & SPACING SYSTEM
- Grid system (12-column, etc.)
- Spacing scale (4px base, 8, 16, 24, 32, 48, 64)
- Container widths
- Breakpoints for responsive design

### 7. 🧩 COMPONENT RECOMMENDATIONS
- Button styles (primary, secondary, ghost)
- Form design patterns
- Card layouts
- Navigation patterns
- Modal/dialog design
- Loading states
- Empty states
- Error states

### 8. ✨ MICRO-INTERACTIONS
- Hover effects
- Click feedback
- Loading animations
- Success/error feedback
- Scroll behaviors
- Transitions (timing, easing)

### 9. 📱 RESPONSIVE STRATEGY
- Mobile-first vs desktop-first
- Key breakpoints
- Touch targets (44px minimum)
- Mobile navigation patterns

### 10. ♿ ACCESSIBILITY CHECKLIST
- Color contrast ratios
- Focus indicators
- Screen reader compatibility
- Keyboard navigation
- ARIA labels

### 11. 🖼️ IMAGERY GUIDELINES
- Photography style
- Illustration style
- Icon system recommendations
- Image treatment (filters, overlays)
- Stock photo sources

### 12. 🚀 IMPLEMENTATION PRIORITIES
- Phase 1: MVP design elements
- Phase 2: Enhanced interactions
- Phase 3: Advanced features
- Recommended tools (Figma, etc.)

## JSON FIELD REQUIREMENTS

### color_palettes (provide 2-3 complete palettes)
Each palette must have:
- primary: Main brand color
- secondary: Supporting color
- accent: Call-to-action color
- background: Page background
- text: Primary text color
- additional: Array of 3-5 additional colors

### fonts
Must include:
- heading: Display/heading font
- body: Body text font
- accent: Optional accent font
- fallbacks: System font fallbacks

### inspirations (5-7 platforms)
Each must have:
- platform_name: Company/product name
- description: 2-3 sentences on why it's relevant
- key_features: Array of 3-5 specific UI features to emulate
- url: Website URL

### design_principles (8-10 principles)
Specific, actionable principles like:
- "Use generous whitespace (minimum 24px between sections)"
- "Limit primary CTAs to one per viewport"

### image_suggestions (8-10 suggestions)
Specific recommendations like:
- "Hero images: Lifestyle photography showing diverse users"
- "Icons: Outlined style, 24px base, 2px stroke weight"

## QUALITY STANDARDS
- Analysis must be 1000+ words
- All hex colors must be valid
- All font names must be real Google Fonts or system fonts
- All inspiration URLs should be real websites
- Be specific, not generic"""


class UIResearchAgent:
    def __init__(self):
        pass
    
    async def research(self, prompt: str, industry: Optional[str] = None) -> UIResearchResponse:
        context = self._build_context(prompt, industry)
        
        full_prompt = f"""
User Request: {prompt}

Industry: {industry or "Not specified"}

Reference Information:
{context}

Research and recommend UI design elements for this project. Consider:
1. Similar successful platforms in this space
2. Color psychology relevant to the industry/use case
3. Typography that enhances the user experience
4. Image styles that would resonate with the target audience
5. Key design principles to follow

Provide your response in the specified JSON format.
"""
        
        response = await llm_service.generate(
            prompt=full_prompt,
            system_prompt=UI_RESEARCH_SYSTEM_PROMPT,
        )
        
        return self._parse_response(response)
    
    def _build_context(self, prompt: str, industry: Optional[str]) -> str:
        context_parts = []
        
        prompt_lower = prompt.lower()
        for key, inspiration in UI_INSPIRATIONS.items():
            if any(keyword in prompt_lower for keyword in inspiration.get("keywords", [])):
                context_parts.append(f"Reference Platform - {inspiration['name']}:\n{inspiration['description']}")
        
        if industry and industry.lower() in INDUSTRY_PALETTES:
            palette_info = INDUSTRY_PALETTES[industry.lower()]
            context_parts.append(f"Industry Color Psychology ({industry}):\n{json.dumps(palette_info, indent=2)}")
        
        for key, fonts in FONT_PAIRINGS.items():
            if key in prompt_lower:
                context_parts.append(f"Recommended Font Pairing for {key}:\n{json.dumps(fonts, indent=2)}")
        
        return "\n\n".join(context_parts) if context_parts else "No specific references found."
    
    def _parse_response(self, response: str) -> UIResearchResponse:
        try:
            start_idx = response.find("{")
            end_idx = response.rfind("}") + 1
            if start_idx != -1 and end_idx > start_idx:
                json_str = response[start_idx:end_idx]
                data = json.loads(json_str)
                
                color_palettes = [
                    ColorPalette(**palette) for palette in data.get("color_palettes", [])
                ]
                
                fonts_data = data.get("fonts", {})
                fonts = FontRecommendation(
                    heading=fonts_data.get("heading", "Inter"),
                    body=fonts_data.get("body", "Inter"),
                    accent=fonts_data.get("accent"),
                    fallbacks=fonts_data.get("fallbacks", ["system-ui", "sans-serif"]),
                )
                
                inspirations = [
                    UIInspiration(**insp) for insp in data.get("inspirations", [])
                ]
                
                return UIResearchResponse(
                    content=data.get("analysis", response),
                    color_palettes=color_palettes or [self._default_palette()],
                    fonts=fonts,
                    inspirations=inspirations,
                    design_principles=data.get("design_principles", []),
                    image_suggestions=data.get("image_suggestions", []),
                )
        except (json.JSONDecodeError, KeyError, TypeError):
            pass
        
        return UIResearchResponse(
            content=response,
            color_palettes=[self._default_palette()],
            fonts=FontRecommendation(
                heading="Inter",
                body="Inter",
                fallbacks=["system-ui", "sans-serif"],
            ),
            inspirations=[],
            design_principles=[],
            image_suggestions=[],
        )
    
    def _default_palette(self) -> ColorPalette:
        return ColorPalette(
            primary="#6366f1",
            secondary="#8b5cf6",
            accent="#06b6d4",
            background="#0a0a0b",
            text="#f5f5f5",
            additional=["#10b981", "#f59e0b"],
        )

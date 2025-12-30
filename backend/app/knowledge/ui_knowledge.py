UI_INSPIRATIONS = {
    "ecommerce": {
        "name": "E-commerce Platforms",
        "keywords": ["shop", "store", "ecommerce", "e-commerce", "marketplace", "retail", "product"],
        "description": """
**Top E-commerce UI References:**

1. **Shopify Themes** - Clean, conversion-focused layouts
   - Hero sections with strong CTAs
   - Product grids with hover states
   - Trust badges and social proof
   
2. **Apple Store** - Premium, minimalist aesthetic
   - Large product imagery
   - Generous whitespace
   - Focused product storytelling

3. **Nike** - Dynamic, bold design
   - Full-bleed imagery
   - Strong typography
   - Interactive product customization

**Key UI Patterns:**
- Sticky add-to-cart buttons
- Quick view modals
- Mega navigation menus
- Filter sidebars
- Wishlist functionality
- Recently viewed products
""",
        "platforms": ["Shopify", "Apple", "Nike", "Glossier", "Allbirds"]
    },
    
    "saas_dashboard": {
        "name": "SaaS Dashboard",
        "keywords": ["dashboard", "saas", "admin", "analytics", "panel", "management"],
        "description": """
**Top SaaS Dashboard References:**

1. **Linear** - Modern, keyboard-first design
   - Dark mode default
   - Minimal chrome
   - Command palette (Cmd+K)
   
2. **Stripe Dashboard** - Information-dense yet clean
   - Clear data hierarchy
   - Contextual actions
   - Excellent empty states

3. **Notion** - Flexible, block-based UI
   - Customizable layouts
   - Inline editing
   - Slash commands

**Key UI Patterns:**
- Sidebar navigation
- Data tables with sorting/filtering
- Charts and visualizations
- Settings pages
- Notification systems
- Onboarding flows
""",
        "platforms": ["Linear", "Stripe", "Notion", "Figma", "Vercel"]
    },
    
    "social_media": {
        "name": "Social Media Platforms",
        "keywords": ["social", "feed", "posts", "community", "network", "profile"],
        "description": """
**Top Social Media UI References:**

1. **Twitter/X** - Fast, scannable feeds
   - Infinite scroll
   - Threaded conversations
   - Rich media embeds
   
2. **Instagram** - Visual-first design
   - Grid layouts
   - Stories format
   - Explore discovery

3. **Discord** - Community-focused
   - Channel organization
   - Real-time presence
   - Rich formatting

**Key UI Patterns:**
- Feed algorithms
- Like/react interactions
- Share/repost mechanics
- Direct messaging
- User profiles
- Notification badges
""",
        "platforms": ["Twitter", "Instagram", "Discord", "Reddit", "TikTok"]
    },
    
    "fintech": {
        "name": "Fintech Applications",
        "keywords": ["finance", "banking", "payment", "money", "investment", "wallet", "crypto"],
        "description": """
**Top Fintech UI References:**

1. **Stripe** - Developer-friendly, trustworthy
   - Clear pricing display
   - Step-by-step flows
   - Documentation integration
   
2. **Robinhood** - Simplified investing
   - Clean data visualization
   - Green/red color coding
   - Celebration moments

3. **Wise (TransferWise)** - Transparent, honest
   - Fee transparency
   - Progress tracking
   - Multi-currency display

**Key UI Patterns:**
- Account summaries
- Transaction history
- Security indicators
- Two-factor authentication
- Card management
- Budget visualizations
""",
        "platforms": ["Stripe", "Robinhood", "Wise", "Revolut", "Coinbase"]
    },
    
    "healthcare": {
        "name": "Healthcare Applications",
        "keywords": ["health", "medical", "doctor", "patient", "wellness", "fitness"],
        "description": """
**Top Healthcare UI References:**

1. **One Medical** - Modern, approachable
   - Appointment booking
   - Video visit support
   - Health records access
   
2. **Headspace** - Calming, supportive
   - Soft illustrations
   - Progress tracking
   - Guided experiences

3. **Apple Health** - Comprehensive yet simple
   - Data aggregation
   - Trend analysis
   - Privacy-focused

**Key UI Patterns:**
- Appointment scheduling
- Prescription management
- Health metrics display
- Provider search
- Secure messaging
- Emergency contacts
""",
        "platforms": ["One Medical", "Headspace", "Calm", "MyFitnessPal", "Apple Health"]
    },
    
    "education": {
        "name": "Education Platforms",
        "keywords": ["learning", "course", "education", "school", "training", "tutorial"],
        "description": """
**Top Education UI References:**

1. **Coursera** - Structured learning paths
   - Course cards
   - Progress indicators
   - Certificate displays
   
2. **Duolingo** - Gamified learning
   - Streak mechanics
   - XP and levels
   - Bite-sized lessons

3. **Notion** - Flexible documentation
   - Knowledge bases
   - Collaborative editing
   - Template libraries

**Key UI Patterns:**
- Course catalogs
- Video players
- Quiz interfaces
- Progress dashboards
- Discussion forums
- Certificate generation
""",
        "platforms": ["Coursera", "Duolingo", "Udemy", "Skillshare", "Khan Academy"]
    }
}

INDUSTRY_PALETTES = {
    "technology": {
        "description": "Modern, innovative, trustworthy",
        "primary_colors": ["#0066FF", "#6366F1", "#3B82F6"],
        "accent_colors": ["#06B6D4", "#10B981", "#8B5CF6"],
        "psychology": "Blue conveys trust and reliability, common in tech"
    },
    "healthcare": {
        "description": "Calming, clean, professional",
        "primary_colors": ["#0891B2", "#059669", "#0D9488"],
        "accent_colors": ["#6366F1", "#EC4899", "#F59E0B"],
        "psychology": "Blue and green promote calm and health associations"
    },
    "finance": {
        "description": "Trustworthy, secure, professional",
        "primary_colors": ["#1E40AF", "#047857", "#1F2937"],
        "accent_colors": ["#10B981", "#EF4444", "#F59E0B"],
        "psychology": "Dark blue and green convey stability and growth"
    },
    "ecommerce": {
        "description": "Energetic, trustworthy, action-oriented",
        "primary_colors": ["#DC2626", "#EA580C", "#2563EB"],
        "accent_colors": ["#10B981", "#F59E0B", "#8B5CF6"],
        "psychology": "Orange and red drive action, blue builds trust"
    },
    "education": {
        "description": "Friendly, accessible, encouraging",
        "primary_colors": ["#7C3AED", "#2563EB", "#059669"],
        "accent_colors": ["#F59E0B", "#EC4899", "#06B6D4"],
        "psychology": "Purple represents wisdom, blue focus, green growth"
    },
    "entertainment": {
        "description": "Exciting, dynamic, engaging",
        "primary_colors": ["#DC2626", "#9333EA", "#EC4899"],
        "accent_colors": ["#F59E0B", "#06B6D4", "#10B981"],
        "psychology": "Vibrant colors create excitement and engagement"
    },
    "luxury": {
        "description": "Elegant, sophisticated, exclusive",
        "primary_colors": ["#0F172A", "#78716C", "#92400E"],
        "accent_colors": ["#D4AF37", "#F5F5F4", "#1F2937"],
        "psychology": "Black and gold convey luxury and exclusivity"
    },
    "sustainability": {
        "description": "Natural, eco-friendly, authentic",
        "primary_colors": ["#059669", "#65A30D", "#0D9488"],
        "accent_colors": ["#92400E", "#F59E0B", "#0891B2"],
        "psychology": "Greens and earth tones convey environmental focus"
    }
}

FONT_PAIRINGS = {
    "modern": {
        "heading": "Inter",
        "body": "Inter",
        "description": "Clean, neutral, highly readable"
    },
    "elegant": {
        "heading": "Playfair Display",
        "body": "Source Sans Pro",
        "description": "Sophisticated serif with clean sans-serif"
    },
    "tech": {
        "heading": "Space Grotesk",
        "body": "IBM Plex Sans",
        "description": "Technical feel, great for SaaS"
    },
    "friendly": {
        "heading": "Nunito",
        "body": "Open Sans",
        "description": "Rounded, approachable, warm"
    },
    "bold": {
        "heading": "Bebas Neue",
        "body": "Roboto",
        "description": "Strong headlines, readable body"
    },
    "minimal": {
        "heading": "DM Sans",
        "body": "DM Sans",
        "description": "Geometric, clean, minimal"
    },
    "editorial": {
        "heading": "Libre Baskerville",
        "body": "Lora",
        "description": "Classic editorial feel, great for content"
    },
    "startup": {
        "heading": "Satoshi",
        "body": "General Sans",
        "description": "Modern startup aesthetic"
    }
}

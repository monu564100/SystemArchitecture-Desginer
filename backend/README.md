# PromptCraft AI Backend

AI-powered backend for system architecture and UI research - **Powered by Google Gemini**.

## 🌟 Features

- **Google Gemini AI** - Fast, powerful AI responses
- **System Architecture Agent** - Production-level architecture recommendations (Amazon, Netflix, YouTube scale)
- **UI Research Agent** - Color palettes, fonts, design inspirations
- **Knowledge Base** - Pre-loaded with real-world architecture patterns
- **Vector Search** - ChromaDB for semantic search
- **Caching** - Redis for fast responses

## 🚀 Quick Start

### 1. Get Gemini API Key

1. Go to https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy the key

### 2. Setup

```bash
cd backend

# Create .env from example
copy .env.example .env

# Edit .env and add your Gemini API key
# GEMINI_API_KEY=your_key_here

# Install dependencies
pip install -r requirements.txt

# Run the backend
python run.py
```

### 3. Or use the batch file (Windows)

```bash
# Just double-click start-backend.bat
```

## 📦 Configuration

Edit `.env` file:

```env
# Gemini API (Required)
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-1.5-flash

# Optional - Redis for caching
REDIS_URL=redis://localhost:6379
```

### Available Gemini Models

| Model | Best For |
|-------|----------|
| `gemini-1.5-flash` | Fast responses, good quality (default) |
| `gemini-1.5-pro` | Best quality, slower |
| `gemini-pro` | Balanced |

## 📚 Knowledge Base

Pre-loaded architecture knowledge includes:

### System Architectures
- Amazon e-commerce (microservices, DynamoDB, caching)
- YouTube streaming (CDN, transcoding, recommendation)
- Netflix (service mesh, chaos engineering, edge)
- Uber (dispatch, geospatial, real-time)
- Twitter/X (timeline, fanout, real-time)
- Spotify (audio streaming, playlists)
- Slack (real-time messaging, websockets)
- Stripe (payment processing, fraud detection)

### Design Patterns
- Microservices, CQRS, Event Sourcing
- Circuit Breaker, Saga Pattern
- API Gateway, Service Mesh

### UI Knowledge
- Industry color palettes (fintech, healthcare, e-commerce)
- Font pairings
- Platform inspirations

## 🔧 API Endpoints

### Health Check
```
GET /health
```

### Chat Endpoints
```
POST /api/v1/chat/architecture
POST /api/v1/chat/ui
POST /api/v1/chat/database
POST /api/v1/chat/api
POST /api/v1/chat/prompts
```

### Example Request
```bash
curl -X POST http://localhost:8000/api/v1/chat/architecture \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Design a video streaming platform like YouTube"}'
```

## 🖥️ System Requirements

- Python 3.10+
- Internet connection (for Gemini API)
- Optional: Redis for caching

## 📄 License

MIT License

TECH_STACKS = {
    "modern_web_saas": {
        "name": "Modern Web SaaS Stack",
        "description": "Production-ready stack for building scalable SaaS applications",
        "best_for": ["SaaS", "B2B applications", "Dashboards", "Admin panels"],
        "components": {
            "frontend": {
                "framework": "Next.js 14+ / React 18+",
                "styling": "Tailwind CSS + shadcn/ui",
                "state": "Zustand / TanStack Query",
                "forms": "React Hook Form + Zod",
                "testing": "Vitest + Playwright"
            },
            "backend": {
                "runtime": "Node.js 20+ / Bun",
                "framework": "Fastify / Hono / tRPC",
                "orm": "Prisma / Drizzle",
                "validation": "Zod",
                "auth": "Lucia / Auth.js"
            },
            "database": {
                "primary": "PostgreSQL (Neon / Supabase)",
                "cache": "Redis (Upstash)",
                "search": "Meilisearch / Typesense"
            },
            "infrastructure": {
                "hosting": "Vercel / Railway / Fly.io",
                "cdn": "Cloudflare",
                "monitoring": "Sentry + PostHog",
                "ci_cd": "GitHub Actions"
            }
        }
    },
    
    "enterprise_java": {
        "name": "Enterprise Java Stack",
        "description": "Battle-tested stack for enterprise applications",
        "best_for": ["Enterprise", "Banking", "Insurance", "Government"],
        "components": {
            "frontend": {
                "framework": "React / Angular",
                "styling": "Material UI / Ant Design",
                "state": "Redux Toolkit / NgRx"
            },
            "backend": {
                "runtime": "Java 21+ / Kotlin",
                "framework": "Spring Boot 3+",
                "orm": "Hibernate / Spring Data JPA",
                "api": "Spring WebFlux / Spring MVC",
                "security": "Spring Security"
            },
            "database": {
                "primary": "Oracle / PostgreSQL",
                "cache": "Redis / Hazelcast",
                "search": "Elasticsearch"
            },
            "infrastructure": {
                "container": "Kubernetes / OpenShift",
                "service_mesh": "Istio",
                "monitoring": "Prometheus + Grafana",
                "logging": "ELK Stack"
            }
        }
    },
    
    "realtime_communication": {
        "name": "Real-time Communication Stack",
        "description": "Stack optimized for real-time features like chat and collaboration",
        "best_for": ["Chat apps", "Collaboration tools", "Gaming", "Live features"],
        "components": {
            "frontend": {
                "framework": "React / Solid.js",
                "realtime": "Socket.io-client / Ably SDK",
                "state": "Zustand / Jotai"
            },
            "backend": {
                "runtime": "Node.js / Elixir / Go",
                "framework": "Fastify / Phoenix / Fiber",
                "realtime": "Socket.io / Phoenix Channels / WebRTC",
                "presence": "Redis Pub/Sub"
            },
            "database": {
                "primary": "PostgreSQL / CockroachDB",
                "realtime": "Redis Streams / Kafka",
                "cache": "Redis"
            },
            "infrastructure": {
                "hosting": "Fly.io / AWS",
                "cdn": "Cloudflare",
                "websocket": "Ably / Pusher / self-hosted"
            }
        }
    },
    
    "ai_ml_platform": {
        "name": "AI/ML Platform Stack",
        "description": "Stack for building AI-powered applications",
        "best_for": ["AI applications", "ML platforms", "Data products"],
        "components": {
            "frontend": {
                "framework": "Next.js / Streamlit / Gradio",
                "visualization": "D3.js / Plotly"
            },
            "backend": {
                "runtime": "Python 3.11+",
                "framework": "FastAPI / LangServe",
                "ml": "LangChain / LlamaIndex",
                "inference": "vLLM / TGI"
            },
            "database": {
                "vector": "Pinecone / Qdrant / Chroma",
                "primary": "PostgreSQL + pgvector",
                "cache": "Redis"
            },
            "ml_ops": {
                "training": "Modal / RunPod",
                "serving": "Replicate / Baseten",
                "monitoring": "LangSmith / Weights & Biases"
            }
        }
    },
    
    "ecommerce": {
        "name": "E-commerce Stack",
        "description": "Complete stack for online stores and marketplaces",
        "best_for": ["E-commerce", "Marketplaces", "Retail"],
        "components": {
            "frontend": {
                "framework": "Next.js / Remix",
                "commerce": "Shopify Hydrogen / Medusa.js",
                "styling": "Tailwind CSS"
            },
            "backend": {
                "headless": "Medusa.js / Saleor",
                "payments": "Stripe / Square",
                "shipping": "EasyPost / Shippo"
            },
            "database": {
                "primary": "PostgreSQL",
                "search": "Algolia / Elasticsearch",
                "cache": "Redis"
            },
            "infrastructure": {
                "hosting": "Vercel / AWS",
                "cdn": "Cloudflare / Fastly",
                "media": "Cloudinary / imgix"
            }
        }
    },
    
    "mobile_first": {
        "name": "Mobile-First Stack",
        "description": "Stack for building mobile applications with shared codebase",
        "best_for": ["Mobile apps", "Cross-platform", "Consumer apps"],
        "components": {
            "mobile": {
                "framework": "React Native / Flutter / Expo",
                "navigation": "React Navigation / Go Router",
                "state": "Zustand / Riverpod"
            },
            "backend": {
                "baas": "Supabase / Firebase",
                "custom": "Node.js + Fastify / Go",
                "push": "Firebase Cloud Messaging"
            },
            "database": {
                "primary": "PostgreSQL (Supabase)",
                "local": "WatermelonDB / SQLite",
                "sync": "PowerSync / ElectricSQL"
            },
            "infrastructure": {
                "hosting": "Railway / Fly.io",
                "ci_cd": "EAS Build / Codemagic",
                "analytics": "PostHog / Amplitude"
            }
        }
    },
    
    "data_intensive": {
        "name": "Data-Intensive Application Stack",
        "description": "Stack for applications with heavy data processing needs",
        "best_for": ["Analytics", "Data platforms", "ETL pipelines"],
        "components": {
            "ingestion": {
                "streaming": "Apache Kafka / Redpanda",
                "batch": "Apache Spark / dbt"
            },
            "processing": {
                "stream": "Apache Flink / Kafka Streams",
                "batch": "Apache Spark / Trino"
            },
            "storage": {
                "warehouse": "Snowflake / BigQuery / ClickHouse",
                "lake": "Delta Lake / Apache Iceberg",
                "oltp": "PostgreSQL / CockroachDB"
            },
            "visualization": {
                "bi": "Metabase / Superset",
                "embedded": "Cube.js"
            }
        }
    },
    
    "serverless": {
        "name": "Serverless Stack",
        "description": "Stack leveraging serverless architecture for minimal ops",
        "best_for": ["Startups", "MVPs", "Variable traffic", "Cost optimization"],
        "components": {
            "frontend": {
                "framework": "Next.js / Astro",
                "hosting": "Vercel / Cloudflare Pages"
            },
            "backend": {
                "functions": "Vercel Functions / Cloudflare Workers",
                "framework": "Hono / Nitro",
                "queue": "Upstash QStash / Trigger.dev"
            },
            "database": {
                "primary": "PlanetScale / Neon / Turso",
                "kv": "Upstash Redis / Cloudflare KV",
                "blob": "Cloudflare R2 / S3"
            },
            "infrastructure": {
                "auth": "Clerk / Auth0",
                "email": "Resend / Postmark",
                "monitoring": "Sentry"
            }
        }
    },
    
    "high_performance": {
        "name": "High-Performance Stack",
        "description": "Stack optimized for maximum performance and low latency",
        "best_for": ["High-frequency trading", "Gaming", "Real-time systems"],
        "components": {
            "backend": {
                "language": "Rust / Go / C++",
                "framework": "Actix-web / Fiber / gRPC",
                "async": "Tokio / Goroutines"
            },
            "database": {
                "primary": "ScyllaDB / TiKV",
                "cache": "Redis / Dragonfly",
                "timeseries": "TimescaleDB / QuestDB"
            },
            "messaging": {
                "queue": "Redpanda / NATS",
                "rpc": "gRPC / Cap'n Proto"
            },
            "infrastructure": {
                "hosting": "Bare metal / Dedicated servers",
                "network": "Kernel bypass / DPDK",
                "observability": "eBPF / Grafana"
            }
        }
    },
    
    "content_platform": {
        "name": "Content Platform Stack",
        "description": "Stack for content-heavy websites and blogs",
        "best_for": ["Blogs", "News sites", "Documentation", "Marketing sites"],
        "components": {
            "frontend": {
                "framework": "Astro / Next.js",
                "cms": "Sanity / Contentful / Payload CMS",
                "styling": "Tailwind CSS"
            },
            "backend": {
                "cms": "Payload CMS / Strapi",
                "search": "Algolia / Pagefind"
            },
            "database": {
                "primary": "PostgreSQL / MongoDB",
                "media": "Cloudinary / Uploadcare"
            },
            "infrastructure": {
                "hosting": "Vercel / Netlify",
                "cdn": "Cloudflare",
                "analytics": "Plausible / Fathom"
            }
        }
    }
}

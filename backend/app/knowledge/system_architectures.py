SYSTEM_ARCHITECTURES = {
    "amazon_ecommerce": {
        "name": "Amazon-style E-commerce Platform",
        "description": """
Amazon's architecture is a masterpiece of distributed systems engineering, handling millions of requests per second.

**Core Architecture Principles:**
- Service-Oriented Architecture (SOA) with thousands of microservices
- Two-Pizza Teams: Each service owned by a small team
- "You build it, you run it" philosophy

**Key Components:**

1. **Frontend Layer:**
   - CloudFront CDN for static assets
   - Elastic Load Balancers (ALB/NLB)
   - React/Next.js for web, React Native for mobile

2. **API Gateway Layer:**
   - Amazon API Gateway for REST/WebSocket APIs
   - Rate limiting, authentication, request routing
   - Request/Response transformation

3. **Microservices Layer:**
   - Product Catalog Service (DynamoDB + Elasticsearch)
   - User Service (Cognito + RDS)
   - Order Service (Event-driven with SQS/SNS)
   - Payment Service (PCI-compliant isolated VPC)
   - Inventory Service (Real-time with DynamoDB Streams)
   - Recommendation Engine (SageMaker + Personalize)
   - Search Service (OpenSearch/Elasticsearch)
   - Review Service (DynamoDB + sentiment analysis)

4. **Data Layer:**
   - DynamoDB for high-throughput key-value
   - Aurora PostgreSQL for relational data
   - ElastiCache Redis for session/caching
   - S3 for media storage
   - Redshift for analytics

5. **Event-Driven Architecture:**
   - EventBridge for event routing
   - SQS for message queuing
   - SNS for pub/sub
   - Kinesis for real-time streaming

6. **Search & Discovery:**
   - Elasticsearch with custom ranking
   - ML-powered search relevance
   - A/B testing infrastructure

**Scalability Patterns:**
- Auto Scaling Groups
- Database read replicas
- Global Tables for multi-region
- Caching at every layer
""",
        "scale": "enterprise",
        "components": [
            "CDN", "Load Balancer", "API Gateway", "Microservices",
            "Message Queue", "Cache", "Search Engine", "Data Warehouse"
        ],
        "technologies": {
            "frontend": ["React", "Next.js", "CloudFront"],
            "backend": ["Node.js", "Java", "Python", "Go"],
            "database": ["DynamoDB", "Aurora", "Redis", "Elasticsearch"],
            "infrastructure": ["AWS", "Kubernetes", "Docker"],
            "messaging": ["SQS", "SNS", "Kinesis", "EventBridge"]
        },
        "patterns": [
            "Microservices", "Event Sourcing", "CQRS", "Saga Pattern",
            "Circuit Breaker", "Bulkhead", "Strangler Fig"
        ],
        "use_cases": ["E-commerce", "Marketplace", "Retail platform"]
    },
    
    "youtube_streaming": {
        "name": "YouTube-style Video Streaming Platform",
        "description": """
YouTube serves over 1 billion hours of video daily with sub-second latency globally.

**Core Architecture:**

1. **Video Upload Pipeline:**
   - Chunked uploads to Cloud Storage
   - Upload service validates and queues
   - Transcoding service (FFmpeg clusters)
   - Multiple quality renditions (144p to 8K)
   - Adaptive bitrate encoding (HLS/DASH)

2. **Content Delivery:**
   - Global CDN with edge caching
   - PoP (Points of Presence) in 100+ locations
   - Intelligent routing based on user location
   - P2P delivery for popular content

3. **Video Player:**
   - Adaptive Bitrate Streaming (ABR)
   - Buffer management algorithms
   - Quality switching without rebuffering
   - Playback analytics

4. **Backend Services:**
   - Video Metadata Service (Spanner/Vitess)
   - User Service (Authentication, Profiles)
   - Subscription Service
   - Notification Service (Push/Email)
   - Comment Service (Sharded MySQL)
   - Like/Dislike Service (Counter service)
   - Watch History Service
   - Playlist Service

5. **Recommendation System:**
   - Real-time ML inference
   - Collaborative filtering
   - Content-based filtering
   - Deep learning models (TensorFlow)
   - A/B testing framework

6. **Live Streaming:**
   - RTMP/WebRTC ingestion
   - Real-time transcoding
   - Low-latency HLS
   - Chat integration
   - DVR functionality

7. **Data Pipeline:**
   - Event streaming (Kafka)
   - Real-time analytics (Flink)
   - Batch processing (Spark)
   - Data warehouse (BigQuery)

**Key Metrics:**
- 99.99% availability
- < 200ms start time
- < 2s latency for live
""",
        "scale": "enterprise",
        "components": [
            "Video Transcoding", "CDN", "Recommendation Engine",
            "Real-time Analytics", "Live Streaming", "Search"
        ],
        "technologies": {
            "frontend": ["React", "Polymer", "Web Components"],
            "backend": ["Python", "Go", "C++", "Java"],
            "database": ["Vitess", "Bigtable", "Spanner", "Redis"],
            "infrastructure": ["GCP", "Kubernetes", "Borg"],
            "streaming": ["Kafka", "Flink", "Pub/Sub"]
        },
        "patterns": [
            "CQRS", "Event Sourcing", "Sharding", "CDN Caching",
            "Adaptive Streaming", "Edge Computing"
        ],
        "use_cases": ["Video platform", "Streaming service", "Live streaming"]
    },
    
    "netflix_streaming": {
        "name": "Netflix-style Streaming Platform",
        "description": """
Netflix handles 15% of global internet traffic with exceptional reliability.

**Architecture Overview:**

1. **Client Applications:**
   - Platform-specific players (iOS, Android, TV, Web)
   - Adaptive streaming client
   - Offline download support
   - DRM implementation (Widevine, FairPlay)

2. **API Gateway (Zuul):**
   - Dynamic routing
   - Load balancing
   - Authentication
   - Canary deployments
   - A/B testing routing

3. **Backend Services (Microservices):**
   - Account Service
   - Profile Service
   - Content Service
   - Playback Service
   - Bookmark Service
   - Billing Service
   - Recommendation Service

4. **Content Encoding Pipeline:**
   - Per-title encoding optimization
   - Shot-based encoding
   - Multiple codecs (AV1, VP9, H.265, H.264)
   - HDR/Dolby Vision support
   - Quality metrics (VMAF)

5. **Open Connect CDN:**
   - Custom CDN appliances
   - Embedded in ISP networks
   - 15,000+ servers globally
   - Proactive caching of popular content

6. **Data Platform:**
   - Event streaming (Kafka)
   - Real-time processing (Flink)
   - Data warehouse (Spark + Iceberg)
   - Feature store for ML

7. **Recommendation & Personalization:**
   - Homepage ranking
   - Artwork personalization
   - Search personalization
   - Similar titles
   - Because you watched

8. **Chaos Engineering:**
   - Chaos Monkey (instance failures)
   - Chaos Kong (region failures)
   - Latency Monkey (network delays)

**Key Technologies:**
- Service mesh (Envoy)
- Container orchestration (Titus)
- Time-series database (Atlas)
- Distributed tracing (Edgar)
""",
        "scale": "enterprise",
        "components": [
            "Custom CDN", "Microservices", "ML Platform",
            "Encoding Pipeline", "A/B Testing", "Chaos Engineering"
        ],
        "technologies": {
            "frontend": ["React", "Node.js"],
            "backend": ["Java", "Python", "Node.js", "Go"],
            "database": ["Cassandra", "CockroachDB", "Redis", "Elasticsearch"],
            "infrastructure": ["AWS", "Titus", "Docker"],
            "streaming": ["Kafka", "Flink", "Spark"]
        },
        "patterns": [
            "Microservices", "Circuit Breaker", "Bulkhead",
            "Chaos Engineering", "Edge Computing", "A/B Testing"
        ],
        "use_cases": ["Streaming platform", "OTT service", "Media delivery"]
    },
    
    "uber_ride_sharing": {
        "name": "Uber-style Ride Sharing Platform",
        "description": """
Uber processes millions of rides daily with real-time matching and routing.

**Core Components:**

1. **Mobile Applications:**
   - Rider app (iOS/Android)
   - Driver app with navigation
   - Real-time location tracking
   - Push notifications

2. **Dispatch System:**
   - Real-time driver matching
   - Surge pricing algorithm
   - ETA calculation
   - Route optimization

3. **Location Services:**
   - GPS tracking at 4-second intervals
   - Geospatial indexing (H3)
   - Map matching algorithms
   - Traffic prediction

4. **Backend Services:**
   - User Service (riders/drivers)
   - Trip Service
   - Payment Service
   - Rating Service
   - Notification Service
   - Pricing Service
   - Fraud Detection Service

5. **Real-time Infrastructure:**
   - WebSocket connections for live updates
   - Event-driven architecture
   - In-memory caching (Redis)
   - Message queues (Kafka)

6. **Data Platform:**
   - Real-time analytics
   - ML models for demand prediction
   - Batch processing for reporting
   - Data lake architecture

7. **Maps & Navigation:**
   - Custom routing engine
   - Real-time traffic data
   - Turn-by-turn navigation
   - POI database

**Scalability:**
- Geographically distributed
- Cell-based architecture
- Auto-scaling based on demand
- Multi-region failover
""",
        "scale": "enterprise",
        "components": [
            "Real-time Matching", "Geospatial Services", "Payment Processing",
            "Push Notifications", "Route Optimization", "Surge Pricing"
        ],
        "technologies": {
            "frontend": ["React Native", "Swift", "Kotlin"],
            "backend": ["Go", "Python", "Java", "Node.js"],
            "database": ["MySQL (Vitess)", "Redis", "Cassandra", "PostgreSQL"],
            "infrastructure": ["GCP", "Kubernetes", "Docker"],
            "messaging": ["Kafka", "Redis Pub/Sub"]
        },
        "patterns": [
            "Event Sourcing", "CQRS", "Saga Pattern",
            "Cell-based Architecture", "Domain-Driven Design"
        ],
        "use_cases": ["Ride sharing", "Delivery platform", "Logistics"]
    },
    
    "twitter_social": {
        "name": "Twitter/X-style Social Media Platform",
        "description": """
Twitter handles 500M+ tweets daily with real-time timeline delivery.

**Architecture Components:**

1. **Tweet Ingestion:**
   - API Gateway for tweet submission
   - Validation and rate limiting
   - Fan-out service for delivery
   - Media upload service

2. **Timeline Service:**
   - Pull model for inactive users
   - Push model for active users (fan-out on write)
   - Hybrid approach for celebrities
   - Redis for timeline caching

3. **Social Graph:**
   - Follower/Following relationships
   - Graph database (FlockDB)
   - Bidirectional lookup
   - Recommendations

4. **Search & Trends:**
   - Real-time indexing (Earlybird)
   - Trend detection algorithms
   - Hashtag tracking
   - User search

5. **Backend Services:**
   - User Service
   - Tweet Service
   - Timeline Service
   - Notification Service
   - DM Service
   - Media Service
   - Analytics Service

6. **Real-time Features:**
   - WebSocket for live updates
   - Streaming API
   - Push notifications
   - Live video (Periscope)

7. **Data Infrastructure:**
   - Event log (Kafka)
   - Hadoop for batch processing
   - Manhattan (key-value store)
   - Analytics pipeline

**Key Challenges:**
- Hot spots (celebrity tweets)
- Real-time delivery at scale
- Spam/abuse detection
- Content moderation
""",
        "scale": "enterprise",
        "components": [
            "Fan-out Service", "Timeline Cache", "Social Graph",
            "Real-time Search", "Trend Detection", "Media Processing"
        ],
        "technologies": {
            "frontend": ["React", "React Native", "GraphQL"],
            "backend": ["Scala", "Java", "Python"],
            "database": ["Manhattan", "Redis", "MySQL", "FlockDB"],
            "infrastructure": ["AWS/GCP", "Kubernetes", "Mesos"],
            "messaging": ["Kafka", "Kestrel"]
        },
        "patterns": [
            "Fan-out on Write", "Fan-out on Read", "CQRS",
            "Event Sourcing", "Cache-aside"
        ],
        "use_cases": ["Social media", "Microblogging", "News platform"]
    },
    
    "stripe_payments": {
        "name": "Stripe-style Payment Processing Platform",
        "description": """
Stripe processes billions in payments with 99.999% uptime and PCI compliance.

**Architecture Overview:**

1. **API Layer:**
   - RESTful API with idempotency
   - Webhook delivery system
   - SDK generation (OpenAPI)
   - Rate limiting & quotas

2. **Payment Processing:**
   - Payment intent workflow
   - Card network integration
   - 3D Secure authentication
   - Fraud detection (Radar)

3. **Core Services:**
   - Account Service
   - Payment Service
   - Subscription Service
   - Invoice Service
   - Payout Service
   - Dispute Service
   - Reporting Service

4. **Security & Compliance:**
   - PCI DSS Level 1
   - Tokenization (vault)
   - Encryption at rest/transit
   - Key management (HSM)

5. **Financial Infrastructure:**
   - Ledger system
   - Double-entry bookkeeping
   - Reconciliation engine
   - Multi-currency support

6. **Reliability:**
   - Multi-region deployment
   - Automatic failover
   - Request hedging
   - Circuit breakers

7. **Developer Experience:**
   - Dashboard & analytics
   - Test mode
   - Detailed logging
   - Webhook testing

**Key Principles:**
- Exactly-once semantics
- Idempotent operations
- Audit trail for everything
- Real-time fraud detection
""",
        "scale": "enterprise",
        "components": [
            "Payment Gateway", "Fraud Detection", "Ledger System",
            "Webhook Delivery", "Card Vault", "Reconciliation"
        ],
        "technologies": {
            "frontend": ["React", "TypeScript"],
            "backend": ["Ruby", "Go", "Scala"],
            "database": ["PostgreSQL", "Redis", "MongoDB"],
            "infrastructure": ["AWS", "Kubernetes"],
            "security": ["HSM", "Vault", "mTLS"]
        },
        "patterns": [
            "Saga Pattern", "Idempotency", "Event Sourcing",
            "CQRS", "Circuit Breaker", "Bulkhead"
        ],
        "use_cases": ["Payment processing", "Fintech", "E-commerce payments"]
    },
    
    "slack_messaging": {
        "name": "Slack-style Real-time Messaging Platform",
        "description": """
Slack handles millions of concurrent connections with real-time message delivery.

**Architecture Components:**

1. **Real-time Gateway:**
   - WebSocket connections
   - Connection state management
   - Presence system
   - Typing indicators

2. **Message Services:**
   - Message ingestion
   - Message storage
   - Search indexing
   - File attachments

3. **Channel Architecture:**
   - Public channels
   - Private channels
   - Direct messages
   - Threads

4. **Backend Services:**
   - User Service
   - Workspace Service
   - Channel Service
   - Message Service
   - Search Service
   - File Service
   - Notification Service
   - Integration Service (Apps/Bots)

5. **Search Infrastructure:**
   - Real-time indexing
   - Elasticsearch cluster
   - Faceted search
   - Message filtering

6. **Integrations:**
   - App directory
   - Webhook system
   - Bot framework
   - OAuth provider

7. **Data Layer:**
   - Sharded MySQL
   - Redis for caching
   - S3 for files
   - Elasticsearch for search

**Scalability Considerations:**
- Connection management at scale
- Message fan-out
- Search scalability
- File storage costs
""",
        "scale": "large",
        "components": [
            "WebSocket Gateway", "Message Queue", "Search Engine",
            "File Storage", "Integration Platform", "Presence System"
        ],
        "technologies": {
            "frontend": ["React", "Electron", "React Native"],
            "backend": ["PHP (Hack)", "Java", "Go"],
            "database": ["MySQL (Vitess)", "Redis", "Elasticsearch"],
            "infrastructure": ["AWS", "Kubernetes"],
            "messaging": ["Kafka", "Job Queue"]
        },
        "patterns": [
            "Event-Driven", "CQRS", "Sharding",
            "Connection Pooling", "Read-through Cache"
        ],
        "use_cases": ["Team messaging", "Collaboration tool", "Enterprise chat"]
    },
    
    "airbnb_marketplace": {
        "name": "Airbnb-style Marketplace Platform",
        "description": """
Airbnb connects millions of hosts and guests with complex matching and booking.

**Core Architecture:**

1. **Search & Discovery:**
   - Elasticsearch for listings
   - ML-powered ranking
   - Personalized results
   - Map-based search
   - Filters and facets

2. **Booking System:**
   - Availability calendar
   - Pricing engine
   - Instant book vs request
   - Reservation management

3. **Backend Services:**
   - User Service (hosts/guests)
   - Listing Service
   - Booking Service
   - Payment Service
   - Review Service
   - Messaging Service
   - Notification Service
   - Trust & Safety Service

4. **Trust & Safety:**
   - Identity verification
   - Background checks
   - Fraud detection
   - Content moderation
   - Risk scoring

5. **Pricing Intelligence:**
   - Dynamic pricing
   - Market data analysis
   - Competitor pricing
   - Seasonal adjustments

6. **Host Tools:**
   - Calendar management
   - Pricing suggestions
   - Performance analytics
   - Professional photography

7. **Data Platform:**
   - Event streaming
   - ML pipeline
   - A/B testing
   - Analytics dashboard

**Key Challenges:**
- Two-sided marketplace
- Trust building
- International payments
- Regulatory compliance
""",
        "scale": "enterprise",
        "components": [
            "Search Engine", "Booking System", "Payment Processing",
            "Trust & Safety", "Pricing Engine", "Messaging"
        ],
        "technologies": {
            "frontend": ["React", "Next.js", "React Native"],
            "backend": ["Ruby on Rails", "Java", "Python"],
            "database": ["MySQL", "Redis", "Elasticsearch", "DynamoDB"],
            "infrastructure": ["AWS", "Kubernetes"],
            "ml": ["Spark", "Airflow", "TensorFlow"]
        },
        "patterns": [
            "Service-Oriented Architecture", "Event Sourcing",
            "CQRS", "Saga Pattern", "Feature Flags"
        ],
        "use_cases": ["Marketplace", "Booking platform", "Rental service"]
    },
    
    "spotify_music": {
        "name": "Spotify-style Music Streaming Platform",
        "description": """
Spotify serves 500M+ users with personalized music recommendations.

**Architecture Overview:**

1. **Audio Delivery:**
   - Audio transcoding (Ogg Vorbis)
   - CDN distribution
   - Offline caching
   - Gapless playback
   - Crossfade

2. **Recommendation Engine:**
   - Collaborative filtering
   - Content-based analysis
   - Audio feature extraction
   - Discover Weekly algorithm
   - Release Radar

3. **Backend Services:**
   - User Service
   - Catalog Service
   - Playlist Service
   - Social Service
   - Radio Service
   - Podcast Service
   - Ad Service

4. **Search & Browse:**
   - Full-text search
   - Browse categories
   - New releases
   - Charts

5. **Social Features:**
   - Friend activity
   - Collaborative playlists
   - Artist following
   - Social sharing

6. **Data Infrastructure:**
   - Event delivery (Kafka)
   - Data warehouse (BigQuery)
   - ML platform
   - A/B testing (Experimentation)

7. **Artist Platform:**
   - Spotify for Artists
   - Analytics dashboard
   - Release tools
   - Canvas videos

**Technical Highlights:**
- Microservices (800+)
- Event-driven architecture
- Feature flags everywhere
- Heavy ML usage
""",
        "scale": "enterprise",
        "components": [
            "Audio CDN", "Recommendation Engine", "Playlist Service",
            "Search", "Social Graph", "Analytics Platform"
        ],
        "technologies": {
            "frontend": ["React", "Electron", "Swift", "Kotlin"],
            "backend": ["Java", "Python", "Go"],
            "database": ["Cassandra", "PostgreSQL", "Redis", "BigQuery"],
            "infrastructure": ["GCP", "Kubernetes"],
            "ml": ["TensorFlow", "Spark", "Kubeflow"]
        },
        "patterns": [
            "Microservices", "Event Sourcing", "CQRS",
            "Feature Flags", "A/B Testing"
        ],
        "use_cases": ["Music streaming", "Podcast platform", "Audio content"]
    },
    
    "discord_communication": {
        "name": "Discord-style Communication Platform",
        "description": """
Discord handles millions of concurrent voice/video connections with real-time messaging.

**Core Architecture:**

1. **Real-time Gateway:**
   - WebSocket connections
   - Presence & status
   - Typing indicators
   - Event dispatching

2. **Voice/Video:**
   - WebRTC for media
   - Selective forwarding units (SFU)
   - Voice processing (Opus codec)
   - Screen sharing
   - Go Live streaming

3. **Backend Services:**
   - User Service
   - Guild (Server) Service
   - Channel Service
   - Message Service
   - Voice Service
   - Role/Permission Service
   - Moderation Service

4. **Guild System:**
   - Roles & permissions
   - Channel categories
   - Server boosting
   - Audit logs

5. **Safety & Moderation:**
   - AutoMod
   - Report system
   - Content scanning
   - Rate limiting

6. **Data Layer:**
   - Cassandra for messages
   - PostgreSQL for metadata
   - Redis for caching
   - ScyllaDB for high-throughput

7. **Infrastructure:**
   - Elixir for real-time
   - Rust for performance-critical
   - Python for ML/data
   - Go for services

**Scale Challenges:**
- Millions of concurrent connections
- Real-time voice at scale
- Message storage growth
- Permission calculations
""",
        "scale": "large",
        "components": [
            "WebSocket Gateway", "Voice Server", "Message Store",
            "Permission System", "Media Processing", "Bot Platform"
        ],
        "technologies": {
            "frontend": ["React", "Electron", "React Native"],
            "backend": ["Elixir", "Rust", "Python", "Go"],
            "database": ["Cassandra", "ScyllaDB", "PostgreSQL", "Redis"],
            "infrastructure": ["GCP", "Kubernetes"],
            "media": ["WebRTC", "FFmpeg"]
        },
        "patterns": [
            "Event-Driven", "Actor Model", "CQRS",
            "Sharding", "Connection Multiplexing"
        ],
        "use_cases": ["Gaming community", "Team communication", "Voice chat"]
    }
}

import { CategoryType } from "@/components/Sidebar";

const architectureResponse = (idea: string) => `## 🏗️ System Architecture for: ${idea}

### **Frontend Stack**
**Recommended:** React + TypeScript + Vite
- **Why React?** Component-based, huge ecosystem, great for complex UIs
- **TypeScript:** Type safety prevents runtime errors
- **Vite:** Lightning-fast HMR, optimized builds

**Alternatives:**
- **Next.js** (if you need SSR/SEO)
- **Vue 3** (simpler learning curve)
- **SvelteKit** (smaller bundle size)

### **Backend Stack**
**Recommended:** Node.js + Express/Fastify + PostgreSQL
- **Node.js:** JavaScript everywhere, async by default
- **Fastify:** 2x faster than Express, great for APIs
- **PostgreSQL:** Robust, scalable, great for complex queries

**Performance Formula:**
$$\\text{Response Time} = T_{network} + T_{processing} + T_{database}$$

Where the goal is to minimize each component through:
- CDN caching: $T_{network} \\downarrow$
- Efficient algorithms: $T_{processing} \\downarrow$
- Query optimization: $T_{database} \\downarrow$

### **State Management**
- **Client:** Zustand or TanStack Query
- **Server:** Redis for caching
- **Real-time:** Socket.io or Ably

### **DevOps & Deployment**
| Component | Recommendation |
|-----------|---------------|
| **Hosting** | Vercel (frontend) + Railway (backend) |
| **CI/CD** | GitHub Actions |
| **Monitoring** | Sentry + LogRocket |
| **CDN** | Cloudflare |

### **Folder Structure**
\`\`\`
src/
├── components/     # Reusable UI components
├── features/       # Feature-based modules
├── hooks/          # Custom React hooks
├── lib/            # Utility functions
├── pages/          # Route components
├── services/       # API calls
└── stores/         # State management
\`\`\`

> **Pro Tip:** This architecture scales well from MVP to production! 🚀`;

const uiResponse = (idea: string) => `## 🎨 UI Package Recommendations for: ${idea}

### **Component Libraries**

**Primary Choice: shadcn/ui**
- Modern, accessible, customizable
- Copy-paste components (own your code)
- Works perfectly with Tailwind CSS
- Great for dashboards and forms

**Alternatives:**
| Library | Best For | Bundle Size |
|---------|----------|-------------|
| **Radix UI** | Accessibility | ~50KB |
| **Chakra UI** | Quick prototyping | ~200KB |
| **Mantine** | Feature-rich apps | ~150KB |

### **Styling Approach**
**Recommended: Tailwind CSS**
- Utility-first, rapid development
- Consistent design system
- Small production bundle

Bundle size comparison:
$$\\text{Tailwind (purged)} \\approx 10\\text{KB} << \\text{Bootstrap} \\approx 200\\text{KB}$$

### **Icons & Assets**
- **Icons:** Lucide Icons (lightweight, consistent)
- **Illustrations:** unDraw or Storyset
- **Animations:** Framer Motion

### **Business Perspective UI Tips**
1. **Clear Visual Hierarchy:** Use size, color, and spacing
2. **Consistent Actions:** Primary buttons for main CTA
3. **Loading States:** Never leave users guessing
4. **Error Handling:** Clear, actionable messages
5. **Mobile-First:** 60%+ users are on mobile

### **Color Psychology**
| Color | Emotion | Use Case |
|-------|---------|----------|
| **Blue** | Trust | Finance, Tech |
| **Green** | Growth | Health, Eco |
| **Purple** | Luxury | Premium |
| **Orange** | Energy | E-commerce |

### **Install Command**
\`\`\`bash
npx shadcn@latest init
npx shadcn@latest add button card input
\`\`\``;

const databaseResponse = (idea: string) => `## 🗄️ Database Schema Design for: ${idea}

### **Recommended Database: PostgreSQL**

**Why PostgreSQL?**
- ACID compliant, reliable
- JSON support for flexibility
- Full-text search built-in
- Scales to millions of records

### **Normalization Forms**
Database normalization reduces redundancy:

$$\\text{1NF} \\rightarrow \\text{2NF} \\rightarrow \\text{3NF} \\rightarrow \\text{BCNF}$$

### **Core Tables**

\`\`\`sql
-- Users table with auth
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  full_name VARCHAR(255),
  avatar_url TEXT,
  role VARCHAR(50) DEFAULT 'user',
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Enable Row Level Security
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Example related table
CREATE TABLE projects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  status VARCHAR(50) DEFAULT 'draft',
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_projects_user ON projects(user_id);
\`\`\`

### **Query Performance**
Index selection impacts query time:

$$O(\\log n) \\text{ with index} << O(n) \\text{ full scan}$$

### **Best Practices**
| Practice | Benefit |
|----------|---------|
| **UUIDs** | Secure, distributed-friendly |
| **Indexes** | Faster queries |
| **Soft deletes** | Data recovery |
| **Audit trails** | Compliance |
| **RLS** | Multi-tenant security |

### **ORM Recommendation**
**Prisma** or **Drizzle ORM**
- Type-safe queries
- Easy migrations
- Great developer experience`;

const apiResponse = (idea: string) => `## 🔌 API Design for: ${idea}

### **RESTful API Structure**

**Base URL:** \`https://api.yourapp.com/v1\`

### **Authentication Endpoints**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | \`/auth/register\` | Create account |
| POST | \`/auth/login\` | Get JWT token |
| POST | \`/auth/refresh\` | Refresh token |
| POST | \`/auth/logout\` | Invalidate token |

### **CRUD Operations**
\`\`\`
GET    /resources          # List all (paginated)
POST   /resources          # Create new
GET    /resources/:id      # Get single
PATCH  /resources/:id      # Update
DELETE /resources/:id      # Delete
\`\`\`

### **Response Format**
\`\`\`json
{
  "success": true,
  "data": { ... },
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 150
  }
}
\`\`\`

### **Rate Limiting Formula**
$$\\text{Requests allowed} = \\frac{\\text{Limit}}{\\text{Window (seconds)}} \\times \\text{Time elapsed}$$

**Recommended limits:**
- 100 requests/minute for authenticated
- 20 requests/minute for public

### **HTTP Status Codes**
| Code | Meaning |
|------|---------|
| **200** | Success |
| **201** | Created |
| **400** | Bad Request |
| **401** | Unauthorized |
| **403** | Forbidden |
| **404** | Not Found |
| **429** | Rate Limited |
| **500** | Server Error |

### **Security Headers**
\`\`\`
Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
\`\`\``;

const promptsResponse = (idea: string) => `## ✨ AI Prompt Templates for: ${idea}

### **System Prompt Template**
\`\`\`
You are an expert software developer helping to build [PROJECT_TYPE].
Focus on: clean code, best practices, TypeScript, modern patterns.
Always explain your reasoning briefly.
\`\`\`

### **Prompt Engineering Formula**
The effectiveness of a prompt can be modeled as:

$$E = C \\times S \\times R$$

Where:
- $C$ = **Context** (background information)
- $S$ = **Specificity** (detailed requirements)
- $R$ = **Role** (persona assignment)

### **Feature Implementation Prompt**
\`\`\`
I need to implement [FEATURE] for my [APP_TYPE].

Tech stack:
- Frontend: React + TypeScript + Tailwind
- Backend: Node.js + PostgreSQL
- Auth: JWT

Requirements:
1. [Requirement 1]
2. [Requirement 2]
3. [Requirement 3]

Please provide:
1. Component structure
2. API endpoints needed
3. Database changes
4. Step-by-step implementation
\`\`\`

### **Bug Fix Prompt**
\`\`\`
I have a bug in my code:

**Expected behavior:**
[What should happen]

**Actual behavior:**
[What's happening]

**Code:**
[paste code here]

**Error message:**
[paste error]

Please identify the issue and provide a fix.
\`\`\`

### **Pro Tips**
| Tip | Why It Works |
|-----|--------------|
| **Be specific** | Reduces ambiguity |
| **Show context** | Better understanding |
| **One thing at a time** | Focused responses |
| **Ask for options** | Multiple solutions |
| **Iterate** | Refine results |

> **Remember:** The quality of AI output is directly proportional to the quality of your prompt! 💡`;

export function getMockResponse(category: CategoryType, input: string): string {
  switch (category) {
    case "architecture":
      return architectureResponse(input);
    case "ui":
      return uiResponse(input);
    case "database":
      return databaseResponse(input);
    case "api":
      return apiResponse(input);
    case "prompts":
      return promptsResponse(input);
    default:
      return "I can help you with that! Please select a category from the sidebar.";
  }
}

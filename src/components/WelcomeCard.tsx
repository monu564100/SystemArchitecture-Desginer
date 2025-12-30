import { memo } from "react";
import { LayoutGrid, Brush, HardDrive, Webhook, MessageSquareCode } from "lucide-react";
import { CategoryType } from "./Sidebar";

interface WelcomeCardProps {
  category: CategoryType;
  onExampleClick?: (example: string) => void;
}

const welcomeContent: Record<CategoryType, { icon: React.ElementType; title: string; description: string; examples: string[] }> = {
  architecture: {
    icon: LayoutGrid,
    title: "System Architecture Design",
    description: "Get detailed tech stack recommendations for your app or website. I'll suggest the best frontend frameworks, backend technologies, databases, and deployment strategies.",
    examples: [
      "A real-time chat application with video calls",
      "An e-commerce marketplace like Etsy",
      "A project management tool like Trello",
    ],
  },
  ui: {
    icon: Brush,
    title: "UI Package Suggestions",
    description: "Discover the perfect UI libraries and design systems for your project. I'll recommend components, themes, and styling approaches from a business perspective.",
    examples: [
      "Modern SaaS dashboard with charts",
      "Mobile-first e-commerce checkout flow",
      "Admin panel with data tables and forms",
    ],
  },
  database: {
    icon: HardDrive,
    title: "Database Schema Design",
    description: "Design robust database schemas for your application. I'll help you with table structures, relationships, indexes, and best practices.",
    examples: [
      "Social network with posts, comments, likes",
      "Booking system for a hotel",
      "Inventory management system",
    ],
  },
  api: {
    icon: Webhook,
    title: "API Design Guidelines",
    description: "Plan your RESTful or GraphQL APIs with proper endpoints, authentication, and error handling. Get production-ready API specifications.",
    examples: [
      "Payment gateway integration API",
      "User authentication with OAuth",
      "Real-time notification service",
    ],
  },
  prompts: {
    icon: MessageSquareCode,
    title: "Prompt Templates",
    description: "Get ready-to-use prompts for AI coding assistants. Optimized templates for Cursor, Copilot, and other AI tools.",
    examples: [
      "Code review and refactoring",
      "Bug fixing and debugging",
      "Feature implementation guide",
    ],
  },
};

export const WelcomeCard = memo(function WelcomeCard({ category, onExampleClick }: WelcomeCardProps) {
  const content = welcomeContent[category];
  const Icon = content.icon;

  return (
    <div className="flex-1 flex items-center justify-center p-6">
      <div className="max-w-lg w-full">
        <div className="bg-card rounded-3xl p-8 border border-border">
          <div className="w-16 h-16 rounded-2xl bg-primary/20 flex items-center justify-center mb-6 mx-auto">
            <Icon className="w-8 h-8 text-primary" />
          </div>
          
          <h2 className="text-2xl font-bold text-center text-foreground mb-3">
            {content.title}
          </h2>
          
          <p className="text-muted-foreground text-center mb-8">
            {content.description}
          </p>

          <div className="space-y-3">
            <p className="text-xs font-medium text-muted-foreground uppercase tracking-wider">
              Try asking about:
            </p>
            {content.examples.map((example, index) => (
              <button
                key={index}
                onClick={() => onExampleClick?.(example)}
                className="w-full bg-secondary/50 rounded-xl p-3 text-sm text-foreground/80 text-left cursor-pointer hover:bg-secondary transition-colors"
              >
                "{example}"
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
});

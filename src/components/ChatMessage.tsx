import { memo, useCallback } from "react";
import { Bot, User, Download } from "lucide-react";
import { cn } from "@/lib/utils";
import { MarkdownRenderer } from "./MarkdownRenderer";
import { Button } from "./ui/button";

export interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
  timestamp: Date;
  category?: string;
  userPrompt?: string;
}

interface ChatMessageProps {
  message: Message;
}

export const ChatMessage = memo(function ChatMessage({ message }: ChatMessageProps) {
  const isAssistant = message.role === "assistant";

  const handleDownloadKnowledge = useCallback(() => {
    // Create knowledge JSON for AI agent training
    const knowledgeData = {
      metadata: {
        generated_at: message.timestamp.toISOString(),
        category: message.category || "general",
        source: "PromptCraft AI",
        version: "1.0",
      },
      training_data: {
        prompt: message.userPrompt || "User query",
        response: message.content,
        context: {
          domain: message.category || "system_design",
          type: "expert_knowledge",
        },
      },
      knowledge_base: {
        content: message.content,
        format: "markdown",
        topics: extractTopics(message.content),
      },
      usage_instructions: {
        description: "This JSON file contains AI-generated knowledge that can be used to train or fine-tune AI agents.",
        integration: [
          "Import this file into your AI training pipeline",
          "Use the 'training_data' section for prompt-response pairs",
          "Use 'knowledge_base.content' for RAG (Retrieval-Augmented Generation)",
          "Topics can be used for categorization and filtering",
        ],
      },
    };

    // Create and download the file
    const blob = new Blob([JSON.stringify(knowledgeData, null, 2)], {
      type: "application/json",
    });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `ai_agent_knowledge_${message.category || "general"}_${Date.now()}.json`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }, [message]);

  return (
    <div
      className={cn(
        "flex gap-4 p-5 rounded-2xl transition-all",
        isAssistant ? "bg-zinc-900/50 border border-zinc-800" : "bg-transparent"
      )}
    >
      <div
        className={cn(
          "w-10 h-10 rounded-xl flex items-center justify-center shrink-0",
          isAssistant
            ? "bg-zinc-800 text-zinc-300"
            : "bg-zinc-800/50 text-zinc-400"
        )}
      >
        {isAssistant ? (
          <Bot className="w-5 h-5" />
        ) : (
          <User className="w-5 h-5" />
        )}
      </div>
      <div className="flex-1 min-w-0">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2">
            <span className="font-bold text-sm text-zinc-200">
              {isAssistant ? "PromptCraft AI" : "You"}
            </span>
            <span className="text-xs text-zinc-600">
              {message.timestamp.toLocaleTimeString([], {
                hour: "2-digit",
                minute: "2-digit",
              })}
            </span>
          </div>
          {isAssistant && (
            <Button
              variant="outline"
              size="sm"
              onClick={handleDownloadKnowledge}
              className="flex items-center gap-2 text-xs border-zinc-700 text-zinc-400 hover:bg-zinc-800 hover:text-zinc-200"
            >
              <Download className="w-3 h-3" />
              Download Knowledge
            </Button>
          )}
        </div>
        {isAssistant ? (
          <MarkdownRenderer content={message.content} />
        ) : (
          <div className="text-sm text-zinc-400 whitespace-pre-wrap leading-relaxed">
            {message.content}
          </div>
        )}
      </div>
    </div>
  );
});

// Helper function to extract topics from content
function extractTopics(content: string): string[] {
  const topics: string[] = [];
  
  // Extract headers as topics
  const headerMatches = content.match(/^#{1,3}\s+(.+)$/gm);
  if (headerMatches) {
    headerMatches.forEach((match) => {
      const topic = match.replace(/^#{1,3}\s+/, "").replace(/[🎯📋🔧💾🔄📊🛡️🔐📈💰🚀⚠️🎨🔤📐✨📱♿🖼️💡📦⚡🧩🔍👥📘🧪❌📖]/g, "").trim();
      if (topic && topic.length > 2) {
        topics.push(topic);
      }
    });
  }
  
  // Extract keywords from content
  const keywords = ["architecture", "database", "api", "security", "scalability", "performance", "microservices", "design pattern", "caching", "authentication"];
  keywords.forEach((keyword) => {
    if (content.toLowerCase().includes(keyword) && !topics.some(t => t.toLowerCase().includes(keyword))) {
      topics.push(keyword.charAt(0).toUpperCase() + keyword.slice(1));
    }
  });
  
  return topics.slice(0, 15); // Limit to 15 topics
}

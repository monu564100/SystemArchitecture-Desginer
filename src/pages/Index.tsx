import { useState, useRef, useEffect, useCallback } from "react";
import { Sidebar, CategoryType } from "@/components/Sidebar";
import { ChatMessage, Message } from "@/components/ChatMessage";
import { ChatInput } from "@/components/ChatInput";
import { WelcomeCard } from "@/components/WelcomeCard";
import { BlackHoleLoader } from "@/components/BlackHoleLoader";
import { apiService } from "@/lib/api";

const Index = () => {
  const [activeCategory, setActiveCategory] = useState<CategoryType>("architecture");
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [backendStatus, setBackendStatus] = useState<"connecting" | "connected" | "error">("connecting");
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const messagesContainerRef = useRef<HTMLDivElement>(null);

  // Scroll to bottom only when new messages are added, not on re-renders
  const scrollToBottom = useCallback(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth", block: "end" });
    }
  }, []);

  // Only scroll when messages change, with a small delay to ensure rendering is complete
  useEffect(() => {
    const timer = setTimeout(() => {
      scrollToBottom();
    }, 100);
    return () => clearTimeout(timer);
  }, [messages.length, scrollToBottom]);

  useEffect(() => {
    apiService.healthCheck().then((isHealthy) => {
      setBackendStatus(isHealthy ? "connected" : "error");
    });
  }, []);

  const handleCategoryChange = useCallback((category: CategoryType) => {
    setActiveCategory(category);
    setMessages([]);
  }, []);

  const handleSend = useCallback(async (content: string) => {
    const userMessage: Message = {
      id: Date.now().toString(),
      role: "user",
      content,
      timestamp: new Date(),
      category: activeCategory,
    };

    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const response = await apiService.chat(activeCategory, content);
      
      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: "assistant",
        content: response,
        timestamp: new Date(),
        category: activeCategory,
        userPrompt: content,
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: "assistant",
        content: `⚠️ **Error connecting to backend**\n\nPlease make sure the backend server is running at http://localhost:8000\n\n\`\`\`\ncd backend\npython run.py\n\`\`\`\n\nError: ${error instanceof Error ? error.message : "Unknown error"}`,
        timestamp: new Date(),
        category: activeCategory,
        userPrompt: content,
      };
      setMessages((prev) => [...prev, errorMessage]);
      setBackendStatus("error");
    }

    setIsLoading(false);
  }, [activeCategory]);

  const handleExampleClick = useCallback((example: string) => {
    handleSend(example);
  }, [handleSend]);

  const categoryTitles: Record<CategoryType, string> = {
    architecture: "System Architecture Design",
    ui: "UI Package Suggestions",
    database: "Database Schema Design",
    api: "API Design Guidelines",
    prompts: "Prompt Templates",
  };

  return (
    <div className="flex h-screen bg-background overflow-hidden font-sans">
      <div className="w-72 flex-shrink-0">
        <Sidebar
          activeCategory={activeCategory}
          onCategoryChange={handleCategoryChange}
        />
      </div>
      
      <main className="flex-1 flex flex-col min-w-0 h-screen">
        <header className="h-16 border-b border-border flex items-center justify-between px-6 bg-card/50 flex-shrink-0">
          <h2 className="font-semibold text-lg text-foreground tracking-tight">
            {categoryTitles[activeCategory]}
          </h2>
          <div className="flex items-center gap-2">
            <div className={`w-2 h-2 rounded-full ${
              backendStatus === "connected" ? "bg-green-500" : 
              backendStatus === "connecting" ? "bg-yellow-500 animate-pulse" : 
              "bg-red-500"
            }`} />
            <span className="text-xs text-muted-foreground">
              {backendStatus === "connected" ? "Backend Connected" : 
               backendStatus === "connecting" ? "Connecting..." : 
               "Backend Offline"}
            </span>
          </div>
        </header>

        <div ref={messagesContainerRef} className="flex-1 overflow-y-auto scroll-smooth">
          {messages.length === 0 ? (
            <WelcomeCard category={activeCategory} onExampleClick={handleExampleClick} />
          ) : (
            <div className="p-6 space-y-4">
              {messages.map((message) => (
                <ChatMessage key={message.id} message={message} />
              ))}
              {isLoading && (
                <BlackHoleLoader />
              )}
              <div ref={messagesEndRef} style={{ height: "1px" }} />
            </div>
          )}
        </div>

        <ChatInput
          onSend={handleSend}
          isLoading={isLoading}
          category={activeCategory}
        />
      </main>
    </div>
  );
};

export default Index;

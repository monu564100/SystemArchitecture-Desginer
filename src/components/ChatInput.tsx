import { useState, useCallback, memo, FormEvent, ChangeEvent } from "react";
import { SendHorizonal, Wand2 } from "lucide-react";
import { CategoryType } from "./Sidebar";

interface ChatInputProps {
  onSend: (message: string) => void;
  isLoading: boolean;
  category: CategoryType;
}

const placeholders: Record<CategoryType, string> = {
  architecture: "Describe your app idea... e.g., 'A social media app for pet owners'",
  ui: "What kind of UI do you need? e.g., 'A modern dashboard for analytics'",
  database: "Describe your data needs... e.g., 'E-commerce with users, products, orders'",
  api: "What APIs do you need? e.g., 'REST API for a blog platform'",
  prompts: "What prompt template do you need? e.g., 'Code review assistant'",
};

export const ChatInput = memo(function ChatInput({ onSend, isLoading, category }: ChatInputProps) {
  const [input, setInput] = useState("");

  const handleSubmit = useCallback((e: FormEvent) => {
    e.preventDefault();
    if (input.trim() && !isLoading) {
      onSend(input.trim());
      setInput("");
    }
  }, [input, isLoading, onSend]);

  const handleChange = useCallback((e: ChangeEvent<HTMLInputElement>) => {
    setInput(e.target.value);
  }, []);

  return (
    <form onSubmit={handleSubmit} className="p-4 border-t border-border bg-card/50 flex-shrink-0">
      <div className="flex items-center gap-3 bg-secondary rounded-2xl p-2 pl-4">
        <Wand2 className="w-5 h-5 text-primary shrink-0" />
        <input
          type="text"
          value={input}
          onChange={handleChange}
          placeholder={placeholders[category]}
          disabled={isLoading}
          className="flex-1 bg-transparent text-sm text-foreground placeholder:text-muted-foreground outline-none font-medium"
        />
        <button
          type="submit"
          disabled={!input.trim() || isLoading}
          className="w-10 h-10 rounded-xl bg-primary text-primary-foreground flex items-center justify-center transition-all hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <SendHorizonal className="w-4 h-4" />
        </button>
      </div>
      <p className="text-xs text-muted-foreground text-center mt-3">
        Powered by AI • Get detailed suggestions for your development needs
      </p>
    </form>
  );
});

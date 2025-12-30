import { CategoryType } from "@/components/Sidebar";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";

interface ChatResponse {
  content: string;
  cached: boolean;
  metadata?: Record<string, unknown>;
}

interface ColorPalette {
  primary: string;
  secondary: string;
  accent: string;
  background: string;
  text: string;
  additional: string[];
}

interface FontRecommendation {
  heading: string;
  body: string;
  accent?: string;
  fallbacks: string[];
}

interface UIInspiration {
  platform_name: string;
  description: string;
  key_features: string[];
  url?: string;
}

interface UIResearchResponse {
  content: string;
  color_palettes: ColorPalette[];
  fonts: FontRecommendation;
  inspirations: UIInspiration[];
  design_principles: string[];
  image_suggestions: string[];
  cached: boolean;
}

const categoryEndpoints: Record<CategoryType, string> = {
  architecture: "/chat/architecture",
  ui: "/chat/ui",
  database: "/chat/database",
  api: "/chat/api",
  prompts: "/chat/prompts",
};

class APIService {
  private baseUrl: string;
  private abortController: AbortController | null = null;
  private timeout: number = 300000; // 5 minutes timeout for long responses

  constructor(baseUrl: string = API_BASE_URL) {
    this.baseUrl = baseUrl;
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    this.abortController = new AbortController();
    
    // Set timeout
    const timeoutId = setTimeout(() => {
      this.abortController?.abort();
    }, this.timeout);

    try {
      const response = await fetch(`${this.baseUrl}${endpoint}`, {
        ...options,
        signal: this.abortController.signal,
        headers: {
          "Content-Type": "application/json",
          ...options.headers,
        },
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        const error = await response.json().catch(() => ({ detail: "Request failed" }));
        throw new Error(error.detail || `HTTP error ${response.status}`);
      }

      return response.json();
    } catch (error) {
      clearTimeout(timeoutId);
      throw error;
    }
  }

  cancelRequest(): void {
    if (this.abortController) {
      this.abortController.abort();
      this.abortController = null;
    }
  }

  async chat(
    category: CategoryType,
    prompt: string,
    context?: string
  ): Promise<string> {
    const endpoint = categoryEndpoints[category];

    if (category === "ui") {
      const response = await this.request<UIResearchResponse>(endpoint, {
        method: "POST",
        body: JSON.stringify({ prompt, industry: context }),
      });
      return this.formatUIResponse(response);
    }

    const response = await this.request<ChatResponse>(endpoint, {
      method: "POST",
      body: JSON.stringify({ prompt, context }),
    });

    return response.content;
  }

  private formatUIResponse(response: UIResearchResponse): string {
    let content = response.content;

    if (response.color_palettes.length > 0) {
      content += "\n\n## 🎨 Recommended Color Palettes\n\n";
      response.color_palettes.forEach((palette, index) => {
        content += `### Palette ${index + 1}\n`;
        content += `| Role | Color |\n|------|-------|\n`;
        content += `| Primary | \`${palette.primary}\` |\n`;
        content += `| Secondary | \`${palette.secondary}\` |\n`;
        content += `| Accent | \`${palette.accent}\` |\n`;
        content += `| Background | \`${palette.background}\` |\n`;
        content += `| Text | \`${palette.text}\` |\n`;
        if (palette.additional.length > 0) {
          content += `| Additional | ${palette.additional.map(c => `\`${c}\``).join(", ")} |\n`;
        }
        content += "\n";
      });
    }

    if (response.fonts) {
      content += "\n## 🔤 Typography Recommendations\n\n";
      content += `| Role | Font |\n|------|------|\n`;
      content += `| Headings | **${response.fonts.heading}** |\n`;
      content += `| Body | **${response.fonts.body}** |\n`;
      if (response.fonts.accent) {
        content += `| Accent | **${response.fonts.accent}** |\n`;
      }
      content += `| Fallbacks | ${response.fonts.fallbacks.join(", ")} |\n`;
    }

    if (response.inspirations.length > 0) {
      content += "\n## 💡 Platform Inspirations\n\n";
      response.inspirations.forEach((insp) => {
        content += `### ${insp.platform_name}\n`;
        content += `${insp.description}\n\n`;
        content += `**Key Features:** ${insp.key_features.join(", ")}\n`;
        if (insp.url) {
          content += `**Reference:** [${insp.url}](${insp.url})\n`;
        }
        content += "\n";
      });
    }

    if (response.design_principles.length > 0) {
      content += "\n## 📐 Design Principles\n\n";
      response.design_principles.forEach((principle) => {
        content += `- ${principle}\n`;
      });
    }

    if (response.image_suggestions.length > 0) {
      content += "\n## 🖼️ Image Suggestions\n\n";
      response.image_suggestions.forEach((suggestion) => {
        content += `- ${suggestion}\n`;
      });
    }

    return content;
  }

  async healthCheck(): Promise<boolean> {
    try {
      const response = await fetch(`${this.baseUrl.replace("/api/v1", "")}/health`);
      return response.ok;
    } catch {
      return false;
    }
  }
}

export const apiService = new APIService();
export type { ChatResponse, UIResearchResponse, ColorPalette, FontRecommendation, UIInspiration };

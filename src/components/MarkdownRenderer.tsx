import { memo } from "react";
import ReactMarkdown from "react-markdown";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import remarkGfm from "remark-gfm";

interface MarkdownRendererProps {
  content: string;
}

export const MarkdownRenderer = memo(function MarkdownRenderer({ content }: MarkdownRendererProps) {
  return (
    <div className="markdown-content">
      <ReactMarkdown
        remarkPlugins={[remarkMath, remarkGfm]}
        rehypePlugins={[rehypeKatex]}
        components={{
          h1: ({ children }) => (
            <h1 className="text-2xl font-bold text-zinc-100 mt-6 mb-4 first:mt-0">
              {children}
            </h1>
          ),
          h2: ({ children }) => (
            <h2 className="text-xl font-bold text-zinc-200 mt-6 mb-3 flex items-center gap-2 border-b border-zinc-800 pb-2">
              {children}
            </h2>
          ),
          h3: ({ children }) => (
            <h3 className="text-lg font-bold text-zinc-300 mt-4 mb-2">
              {children}
            </h3>
          ),
          p: ({ children }) => (
            <p className="text-zinc-400 mb-3 leading-relaxed">{children}</p>
          ),
          strong: ({ children }) => (
            <strong className="font-bold text-zinc-200">{children}</strong>
          ),
          em: ({ children }) => (
            <em className="italic text-zinc-500">{children}</em>
          ),
          ul: ({ children }) => (
            <ul className="list-disc list-inside mb-4 space-y-1 ml-2">{children}</ul>
          ),
          ol: ({ children }) => (
            <ol className="list-decimal list-inside mb-4 space-y-1 ml-2">{children}</ol>
          ),
          li: ({ children }) => (
            <li className="text-zinc-400">{children}</li>
          ),
          code: ({ className, children, ...props }) => {
            const isInline = !className;
            if (isInline) {
              return (
                <code className="bg-zinc-800 px-1.5 py-0.5 rounded-md text-sm font-mono text-zinc-300">
                  {children}
                </code>
              );
            }
            return (
              <code className={className} {...props}>
                {children}
              </code>
            );
          },
          pre: ({ children }) => (
            <pre className="bg-zinc-900 rounded-xl p-4 overflow-x-auto mb-4 border border-zinc-800">
              <code className="text-sm font-mono text-zinc-300">{children}</code>
            </pre>
          ),
          blockquote: ({ children }) => (
            <blockquote className="border-l-4 border-zinc-600 pl-4 my-4 italic text-zinc-500">
              {children}
            </blockquote>
          ),
          hr: () => <hr className="border-zinc-800 my-6" />,
          a: ({ href, children }) => (
            <a
              href={href}
              target="_blank"
              rel="noopener noreferrer"
              className="text-zinc-300 hover:text-white underline"
            >
              {children}
            </a>
          ),
          table: ({ children }) => (
            <div className="overflow-x-auto mb-4">
              <table className="w-full border-collapse border border-zinc-800 rounded-lg">
                {children}
              </table>
            </div>
          ),
          th: ({ children }) => (
            <th className="bg-zinc-900 px-4 py-2 text-left font-bold border border-zinc-800 text-zinc-200">
              {children}
            </th>
          ),
          td: ({ children }) => (
            <td className="px-4 py-2 border border-zinc-800 text-zinc-400">{children}</td>
          ),
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
});

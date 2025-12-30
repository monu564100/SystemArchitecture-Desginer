import { useState, useEffect, memo } from "react";

const loadingMessages = [
  "Searching across the entire internet...",
  "Traversing knowledge databases...",
  "Analyzing system architectures...",
  "Processing design patterns...",
  "Scanning tech documentation...",
  "Extracting relevant insights...",
  "Compiling expert knowledge...",
  "Synthesizing information...",
  "Building comprehensive response...",
  "Almost there...",
];

export const BlackHoleLoader = memo(function BlackHoleLoader() {
  const [progress, setProgress] = useState(0);
  const [messageIndex, setMessageIndex] = useState(0);

  useEffect(() => {
    // Progress animation
    const progressInterval = setInterval(() => {
      setProgress((prev) => {
        if (prev >= 95) return prev;
        const increment = Math.random() * 8 + 2;
        return Math.min(prev + increment, 95);
      });
    }, 500);

    // Message rotation
    const messageInterval = setInterval(() => {
      setMessageIndex((prev) => (prev + 1) % loadingMessages.length);
    }, 2500);

    return () => {
      clearInterval(progressInterval);
      clearInterval(messageInterval);
    };
  }, []);

  return (
    <div className="flex flex-col items-center justify-center py-16 px-4">
      {/* Black Hole Container */}
      <div className="relative w-64 h-64 flex items-center justify-center">
        {/* Outer glow rings */}
        <div className="absolute inset-0 rounded-full bg-gradient-to-r from-zinc-800 via-zinc-600 to-zinc-800 animate-spin opacity-30" style={{ animationDuration: '8s' }} />
        
        {/* Middle spinning ring */}
        <div className="absolute inset-4 rounded-full border-4 border-zinc-700 border-t-zinc-400 animate-spin" style={{ animationDuration: '3s' }} />
        
        {/* Inner spinning ring */}
        <div className="absolute inset-8 rounded-full border-4 border-zinc-800 border-b-zinc-500 animate-spin" style={{ animationDuration: '2s', animationDirection: 'reverse' }} />
        
        {/* Particle rings */}
        <div className="absolute inset-12 rounded-full border-2 border-dashed border-zinc-600 animate-spin" style={{ animationDuration: '6s' }} />
        
        {/* Core black hole */}
        <div className="absolute inset-16 rounded-full bg-gradient-radial from-black via-zinc-950 to-black shadow-2xl shadow-black">
          {/* Event horizon glow */}
          <div className="absolute inset-0 rounded-full bg-gradient-to-br from-zinc-800/20 to-transparent animate-pulse" />
        </div>
        
        {/* Center singularity */}
        <div className="absolute w-12 h-12 rounded-full bg-black border border-zinc-800 shadow-inner flex items-center justify-center">
          <div className="w-4 h-4 rounded-full bg-zinc-900 animate-ping" />
        </div>

        {/* Orbiting particles */}
        <div className="absolute inset-0 animate-spin" style={{ animationDuration: '4s' }}>
          <div className="absolute top-2 left-1/2 w-2 h-2 rounded-full bg-zinc-400 shadow-lg shadow-zinc-400/50" />
        </div>
        <div className="absolute inset-0 animate-spin" style={{ animationDuration: '5s', animationDirection: 'reverse' }}>
          <div className="absolute bottom-4 right-1/4 w-1.5 h-1.5 rounded-full bg-zinc-500" />
        </div>
        <div className="absolute inset-0 animate-spin" style={{ animationDuration: '7s' }}>
          <div className="absolute top-1/4 right-2 w-1 h-1 rounded-full bg-zinc-300" />
        </div>
      </div>

      {/* Loading Text */}
      <div className="mt-8 text-center space-y-4 max-w-md">
        <p className="text-lg font-medium text-zinc-200 animate-pulse">
          {loadingMessages[messageIndex]}
        </p>
        
        {/* Progress Bar */}
        <div className="w-64 mx-auto">
          <div className="h-1 bg-zinc-800 rounded-full overflow-hidden">
            <div 
              className="h-full bg-gradient-to-r from-zinc-600 via-zinc-400 to-zinc-600 transition-all duration-500 ease-out"
              style={{ width: `${progress}%` }}
            />
          </div>
          <p className="text-zinc-500 text-sm mt-2 font-mono">
            {Math.round(progress)}%
          </p>
        </div>

        {/* Subtext */}
        <p className="text-xs text-zinc-600 mt-4">
          Accessing global knowledge networks...
        </p>
      </div>
    </div>
  );
});

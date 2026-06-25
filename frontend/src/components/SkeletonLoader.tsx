import React from 'react';

export const SkeletonLoader: React.FC = () => {
  return (
    <div className="w-full max-w-4xl mx-auto space-y-8 animate-pulse px-4 py-8">
      {/* Title skeleton */}
      <div className="h-10 bg-slate-200 dark:bg-slate-800 rounded-lg w-1/3 mb-4"></div>
      
      {/* Meta grid skeleton */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="h-24 bg-slate-200 dark:bg-slate-800 rounded-xl"></div>
        <div className="h-24 bg-slate-200 dark:bg-slate-800 rounded-xl"></div>
        <div className="h-24 bg-slate-200 dark:bg-slate-800 rounded-xl"></div>
      </div>

      {/* Outcome box skeleton */}
      <div className="h-32 bg-slate-200 dark:bg-slate-800 rounded-xl w-full"></div>

      {/* Timeline skeleton */}
      <div className="relative border-l-2 border-slate-200 dark:border-slate-800 pl-8 space-y-12">
        {[1, 2, 3].map((item) => (
          <div key={item} className="relative">
            {/* Timeline Dot */}
            <div className="absolute -left-[41px] top-1 w-6 h-6 rounded-full bg-slate-200 dark:bg-slate-800 border-4 border-slate-50 dark:border-slate-950"></div>
            
            {/* Phase details */}
            <div className="space-y-4">
              <div className="h-6 bg-slate-200 dark:bg-slate-800 rounded-lg w-1/4"></div>
              <div className="h-4 bg-slate-200 dark:bg-slate-800 rounded-lg w-1/6"></div>
              
              <div className="p-6 bg-slate-100 dark:bg-slate-900/50 border border-slate-200/50 dark:border-slate-800/50 rounded-2xl space-y-4">
                <div className="h-4 bg-slate-200 dark:bg-slate-800 rounded w-1/3"></div>
                <div className="grid grid-cols-2 gap-4">
                  <div className="h-4 bg-slate-200 dark:bg-slate-800 rounded w-3/4"></div>
                  <div className="h-4 bg-slate-200 dark:bg-slate-800 rounded w-2/3"></div>
                </div>
                <div className="h-10 bg-slate-200 dark:bg-slate-800 rounded-xl w-full"></div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

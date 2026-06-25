import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { Search, Compass, Target, ArrowRight, Lightbulb } from 'lucide-react';
import { fetchSkills, type Skill } from '../services/api';

export const Home: React.FC = () => {
  const navigate = useNavigate();
  const [query, setQuery] = useState('');
  const [skills, setSkills] = useState<Skill[]>([]);
  const [filteredSuggestions, setFilteredSuggestions] = useState<Skill[]>([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [error, setError] = useState<string | null>(null);
  
  const suggestionRef = useRef<HTMLDivElement>(null);

  // Fetch available skills for autocomplete
  useEffect(() => {
    fetchSkills()
      .then((data) => {
        setSkills(data);
      })
      .catch((err) => {
        console.error(err);
        setError("Failed to load skills from server. Please make sure the backend is running.");
      });
  }, []);

  // Filter suggestions based on query
  useEffect(() => {
    if (query.trim() === '') {
      setFilteredSuggestions([]);
      return;
    }

    const filtered = skills.filter((skill) =>
      skill.name.toLowerCase().includes(query.toLowerCase())
    );
    setFilteredSuggestions(filtered);
  }, [query, skills]);

  // Click outside listener for suggestions list
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (suggestionRef.current && !suggestionRef.current.contains(event.target as Node)) {
        setShowSuggestions(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim() !== '') {
      // Navigate to the roadmap path
      navigate(`/roadmap/${encodeURIComponent(query.trim())}`);
    }
  };

  const handleSuggestionClick = (skillName: string) => {
    setQuery(skillName);
    setShowSuggestions(false);
    navigate(`/roadmap/${encodeURIComponent(skillName)}`);
  };

  const handleQuickTagClick = (skillName: string) => {
    setQuery(skillName);
    navigate(`/roadmap/${encodeURIComponent(skillName)}`);
  };

  // Popular skills tags to display in Hero
  const popularSkills = [
    { name: 'Python', icon: '🐍' },
    { name: 'Java', icon: '☕' },
    { name: 'Data Science', icon: '📊' },
    { name: 'Artificial Intelligence', icon: '🤖' },
    { name: 'Cyber Security', icon: '🛡️' },
    { name: 'DevOps', icon: '⚙️' },
    { name: 'Cloud Computing', icon: '☁️' },
    { name: 'MERN Stack', icon: '⚛️' }
  ];

  return (
    <div className="relative overflow-hidden py-16 sm:py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto flex flex-col items-center justify-center">
      {/* Background gradients */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 -z-10 w-[800px] h-[350px] bg-gradient-to-r from-indigo-500/10 to-violet-500/10 dark:from-indigo-650/5 dark:to-violet-650/5 blur-3xl rounded-full"></div>

      {/* Hero Section */}
      <div className="text-center max-w-3xl space-y-6 mb-12">
        <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full border border-indigo-200/50 dark:border-indigo-900/50 bg-indigo-50/50 dark:bg-indigo-950/20 text-indigo-600 dark:text-indigo-400 text-xs font-semibold tracking-wide">
          <Compass className="w-3.5 h-3.5 animate-spin-slow" />
          <span>PREDEFINED SYSTEM ROADMAP DATABASE</span>
        </div>
        
        <h1 className="font-display font-extrabold text-4xl sm:text-5xl lg:text-6xl tracking-tight text-slate-900 dark:text-white">
          Learn Any Skill <br/>
          <span className="bg-gradient-to-r from-indigo-600 via-purple-500 to-pink-500 dark:from-indigo-400 dark:via-purple-400 dark:to-pink-400 bg-clip-text text-transparent">
            Step-by-Step
          </span>
        </h1>
        
        <p className="text-lg sm:text-xl text-slate-600 dark:text-slate-400 max-w-2xl mx-auto font-light leading-relaxed">
          Unlock structured roadmap schedules, curriculum phases, exercises, and micro-projects from our local database. Fully tailored for offline reliability and instant exports.
        </p>
      </div>

      {/* Search Form */}
      <div ref={suggestionRef} className="w-full max-w-2xl relative mb-8">
        <form onSubmit={handleSubmit} className="relative z-20">
          <div className="relative group">
            <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-slate-400 group-focus-within:text-indigo-500 transition-colors">
              <Search className="w-5 h-5" />
            </div>
            
            <input
              type="text"
              placeholder="Enter a skill (e.g. Python, Cyber Security, DevOps...)"
              value={query}
              onChange={(e) => {
                setQuery(e.target.value);
                setShowSuggestions(true);
              }}
              onFocus={() => setShowSuggestions(true)}
              className="w-full pl-12 pr-32 py-4 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-xl shadow-slate-100 dark:shadow-none focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-indigo-500 focus:border-transparent text-slate-900 dark:text-white transition-all text-base"
            />
            
            <button
              type="submit"
              className="absolute right-2 top-2 bottom-2 px-6 rounded-xl bg-indigo-600 text-white font-medium hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors flex items-center space-x-1 text-sm shadow-md shadow-indigo-600/10"
            >
              <span>Explore</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </form>

        {/* Suggestion Dropdown */}
        {showSuggestions && filteredSuggestions.length > 0 && (
          <div className="absolute left-0 right-0 mt-2 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-2xl z-30 overflow-hidden divide-y divide-slate-100 dark:divide-slate-800">
            {filteredSuggestions.map((skill) => (
              <button
                key={skill.id}
                onClick={() => handleSuggestionClick(skill.name)}
                className="w-full px-5 py-3.5 text-left hover:bg-slate-50 dark:hover:bg-slate-850 flex items-center justify-between group transition-colors"
              >
                <div className="flex items-center space-x-3">
                  <div className="w-8 h-8 rounded-lg bg-indigo-50 dark:bg-indigo-950/40 text-indigo-600 dark:text-indigo-400 flex items-center justify-center font-bold text-sm">
                    {skill.name[0]}
                  </div>
                  <div>
                    <p className="font-semibold text-sm text-slate-900 dark:text-white group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors">
                      {skill.name}
                    </p>
                    <p className="text-xs text-slate-500 dark:text-slate-400">
                      Duration: {skill.duration}
                    </p>
                  </div>
                </div>
                <ArrowRight className="w-4 h-4 opacity-0 group-hover:opacity-100 group-hover:translate-x-1 transition-all text-indigo-500" />
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Quick Tags */}
      <div className="w-full max-w-3xl text-center space-y-4">
        <p className="text-sm font-semibold text-slate-400 dark:text-slate-500 flex items-center justify-center space-x-2">
          <Lightbulb className="w-4 h-4 text-amber-500 animate-bounce" />
          <span>Or explore these popular pathways</span>
        </p>
        
        <div className="flex flex-wrap justify-center gap-2 max-w-2xl mx-auto">
          {popularSkills.map((tag) => (
            <button
              key={tag.name}
              onClick={() => handleQuickTagClick(tag.name)}
              className="inline-flex items-center space-x-2 px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 hover:border-indigo-500 dark:hover:border-indigo-400 hover:text-indigo-600 dark:hover:text-indigo-400 shadow-sm hover:shadow-md transition-all duration-200 hover:-translate-y-0.5 text-sm font-medium"
            >
              <span>{tag.icon}</span>
              <span>{tag.name}</span>
            </button>
          ))}
        </div>
      </div>

      {/* Backend Alert Check */}
      {error && (
        <div className="mt-12 p-4 rounded-xl border border-red-200/50 dark:border-red-950/20 bg-red-50/50 dark:bg-red-950/10 text-red-600 dark:text-red-400 text-sm max-w-md text-center shadow-lg shadow-red-500/5 animate-pulse">
          {error}
        </div>
      )}

      {/* Feature grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-20 w-full max-w-5xl">
        <div className="p-6 rounded-2xl border border-slate-200/60 dark:border-slate-800/60 bg-white/40 dark:bg-slate-900/20 backdrop-blur-sm shadow-sm space-y-3">
          <div className="w-10 h-10 rounded-xl bg-indigo-50 dark:bg-indigo-950/40 text-indigo-600 dark:text-indigo-400 flex items-center justify-center shadow-inner">
            <Compass className="w-5 h-5" />
          </div>
          <h3 className="font-display font-bold text-lg text-slate-800 dark:text-white">Predefined Roadmaps</h3>
          <p className="text-slate-500 dark:text-slate-400 text-sm font-light leading-relaxed">
            Instant structures for Python, Java, DevOps, AI, and more. Instantly structured directly from local files.
          </p>
        </div>

        <div className="p-6 rounded-2xl border border-slate-200/60 dark:border-slate-800/60 bg-white/40 dark:bg-slate-900/20 backdrop-blur-sm shadow-sm space-y-3">
          <div className="w-10 h-10 rounded-xl bg-purple-50 dark:bg-purple-950/40 text-purple-600 dark:text-purple-400 flex items-center justify-center shadow-inner">
            <Target className="w-5 h-5" />
          </div>
          <h3 className="font-display font-bold text-lg text-slate-800 dark:text-white">Structured Phases</h3>
          <p className="text-slate-500 dark:text-slate-400 text-sm font-light leading-relaxed">
            Each course outlines duration guidelines, daily schedules, sub-topics, custom exercises, and mini projects.
          </p>
        </div>

        <div className="p-6 rounded-2xl border border-slate-200/60 dark:border-slate-800/60 bg-white/40 dark:bg-slate-900/20 backdrop-blur-sm shadow-sm space-y-3">
          <div className="w-10 h-10 rounded-xl bg-pink-50 dark:bg-pink-950/40 text-pink-600 dark:text-pink-400 flex items-center justify-center shadow-inner">
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <h3 className="font-display font-bold text-lg text-slate-800 dark:text-white">PDF Exports</h3>
          <p className="text-slate-500 dark:text-slate-400 text-sm font-light leading-relaxed">
            Download professional, vector-structured PDF versions of your syllabus for offline viewing with a single click.
          </p>
        </div>
      </div>
    </div>
  );
};

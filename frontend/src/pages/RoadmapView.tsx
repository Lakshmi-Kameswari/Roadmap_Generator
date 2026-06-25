import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { 
  ArrowLeft, Download, Clock, Calendar, Trophy, 
  BookOpen, Terminal, CheckCircle2, AlertCircle, RefreshCw 
} from 'lucide-react';
import { fetchRoadmap, getPDFDownloadUrl, fetchSkills, type Roadmap, type Skill } from '../services/api';
import { SkeletonLoader } from '../components/SkeletonLoader';

export const RoadmapView: React.FC = () => {
  const { skill } = useParams<{ skill: string }>();
  const navigate = useNavigate();

  const [roadmap, setRoadmap] = useState<Roadmap | null>(null);
  const [availableSkills, setAvailableSkills] = useState<Skill[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isDownloading, setIsDownloading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Fetch roadmap data and alternative list
  useEffect(() => {
    if (!skill) return;

    setIsLoading(true);
    setError(null);
    setRoadmap(null);

    // Minor delay so loading transitions feel smooth and premium
    const timer = setTimeout(() => {
      fetchRoadmap(skill)
        .then((data) => {
          setRoadmap(data);
          setIsLoading(false);
        })
        .catch((err) => {
          console.error(err);
          setError(err.message || 'Failed to load roadmap.');
          
          // Also fetch available skills to display as suggestions
          fetchSkills()
            .then((skillsData) => setAvailableSkills(skillsData))
            .catch((e) => console.error("Failed to load alternative list", e));
            
          setIsLoading(false);
        });
    }, 600); // 600ms micro-delay for Skeleton loader presentation

    return () => clearTimeout(timer);
  }, [skill]);

  const handleDownloadPDF = async () => {
    if (!skill) return;
    setIsDownloading(true);
    
    try {
      const url = getPDFDownloadUrl(skill);
      // Create temporary anchor to download file
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `${skill.replace(/\s+/g, '_')}_Roadmap.pdf`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (e) {
      console.error(e);
      alert('Could not download PDF. Please try again.');
    } finally {
      setIsDownloading(false);
    }
  };

  // If loading, show the SkeletonLoader
  if (isLoading) {
    return (
      <div className="py-12 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <div className="h-6 bg-slate-200 dark:bg-slate-800 rounded-md w-24 animate-pulse"></div>
        </div>
        <SkeletonLoader />
      </div>
    );
  }

  // Error State: "Skill Not Available"
  if (error || !roadmap) {
    return (
      <div className="py-16 sm:py-24 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col items-center text-center space-y-8">
        <div className="p-4 rounded-full bg-red-50 dark:bg-red-950/20 text-red-500 shadow-xl shadow-red-500/5 animate-pulse">
          <AlertCircle className="w-16 h-16" />
        </div>
        
        <div className="space-y-3">
          <h1 className="font-display font-extrabold text-3xl text-slate-900 dark:text-white">
            LAnguage not Found 
          </h1>
          <p className="text-slate-600 dark:text-slate-400 max-w-lg mx-auto font-light">
            We couldn't find a learning roadmap matching <span className="font-semibold text-indigo-500">"{skill}"</span> in our predefined database.
          </p>
        </div>

        <div className="flex gap-4">
          <Link 
            to="/" 
            className="inline-flex items-center space-x-2 px-6 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-medium shadow-md shadow-indigo-600/10 hover:shadow-lg transition-all hover:-translate-y-0.5"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Search Again</span>
          </Link>
        </div>

        {availableSkills.length > 0 && (
          <div className="w-full border-t border-slate-200 dark:border-slate-800 pt-8 mt-4 space-y-4">
            <p className="text-sm font-semibold text-slate-500 dark:text-slate-400">
              Try exploring one of our catalog skills:
            </p>
            <div className="flex flex-wrap justify-center gap-2">
              {availableSkills.map((s) => (
                <button
                  key={s.id}
                  onClick={() => navigate(`/roadmap/${encodeURIComponent(s.name)}`)}
                  className="px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 hover:border-indigo-500 dark:hover:border-indigo-400 hover:text-indigo-600 dark:hover:text-indigo-400 text-sm font-medium shadow-sm transition-all duration-200 hover:-translate-y-0.5"
                >
                  {s.name}
                </button>
              ))}
            </div>
          </div>
        )}
      </div>
    );
  }

  return (
    <div className="py-12 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      {/* Back navigation */}
      <div className="flex items-center justify-between">
        <Link 
          to="/"
          className="inline-flex items-center space-x-2 text-slate-500 dark:text-slate-400 hover:text-indigo-600 dark:hover:text-indigo-400 text-sm font-medium transition-colors group"
        >
          <ArrowLeft className="w-4 h-4 group-hover:-translate-x-1 transition-transform" />
          <span>Back to Search</span>
        </Link>
        
        <button
          onClick={handleDownloadPDF}
          disabled={isDownloading}
          className="inline-flex items-center space-x-2 px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm shadow-md shadow-indigo-600/10 hover:shadow-lg transition-all hover:-translate-y-0.5 disabled:opacity-50 disabled:pointer-events-none"
        >
          {isDownloading ? (
            <RefreshCw className="w-4 h-4 animate-spin" />
          ) : (
            <Download className="w-4 h-4" />
          )}
          <span>{isDownloading ? 'Generating PDF...' : 'Download PDF'}</span>
        </button>
      </div>

      {/* Roadmap Header Card */}
      <div className="relative overflow-hidden p-8 sm:p-10 rounded-3xl border border-slate-200 dark:border-slate-800/80 bg-white dark:bg-slate-900 shadow-xl shadow-slate-100/50 dark:shadow-none">
        <div className="absolute top-0 right-0 -translate-y-1/4 translate-x-1/4 w-72 h-72 bg-indigo-500/5 dark:bg-indigo-500/10 blur-3xl rounded-full"></div>
        
        <div className="relative space-y-6">
          <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
            <h1 className="font-display font-extrabold text-3xl sm:text-4xl text-slate-900 dark:text-white">
              {roadmap.skill_name} Roadmap
            </h1>
            
            <div className="flex items-center gap-3">
              <span className="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-xl bg-indigo-50 dark:bg-indigo-950/40 text-indigo-600 dark:text-indigo-400 text-xs font-semibold">
                <Calendar className="w-3.5 h-3.5" />
                <span>{roadmap.estimated_duration}</span>
              </span>
              
              <span className="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/20 text-emerald-600 dark:text-emerald-400 text-xs font-semibold">
                <Clock className="w-3.5 h-3.5" />
                <span>{roadmap.daily_study_time} Daily</span>
              </span>
            </div>
          </div>
          
          <div className="border-t border-slate-100 dark:border-slate-800 pt-6">
            <h3 className="text-sm font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider mb-2">
              Expected Learning Outcome
            </h3>
            <p className="text-slate-700 dark:text-slate-300 font-light leading-relaxed">
              {roadmap.expected_outcome}
            </p>
          </div>
        </div>
      </div>

      {/* Timeline Section */}
      <div className="space-y-8">
        <h2 className="font-display font-bold text-2xl text-slate-900 dark:text-white flex items-center space-x-2">
          <BookOpen className="w-6 h-6 text-indigo-500" />
          <span>Curriculum Phases</span>
        </h2>

        <div className="relative border-l-2 border-slate-200 dark:border-slate-800 pl-6 sm:pl-8 space-y-12">
          {roadmap.phases.map((phase, idx) => (
            <div key={idx} className="relative group">
              {/* Timeline Indicator Dot */}
              <div className="absolute -left-[31px] sm:-left-[39px] top-1.5 w-4 h-4 sm:w-5 sm:h-5 rounded-full bg-white dark:bg-slate-950 border-4 border-indigo-600 group-hover:scale-110 transition-transform duration-200"></div>

              <div className="space-y-4">
                {/* Phase Info Header */}
                <div>
                  <span className="text-xs font-bold text-indigo-500 dark:text-indigo-400 uppercase tracking-widest">
                    Phase {idx + 1}
                  </span>
                  <h3 className="font-display font-bold text-xl sm:text-2xl text-slate-900 dark:text-white mt-0.5">
                    {phase.phase_title.includes(':') ? phase.phase_title.split(':')[1].trim() : phase.phase_title}
                  </h3>
                  <p className="text-xs text-slate-400 dark:text-slate-500 font-medium flex items-center space-x-1.5 mt-1">
                    <Calendar className="w-3.5 h-3.5" />
                    <span>Duration: {phase.duration}</span>
                  </p>
                </div>

                {/* Phase Content Card */}
                <div className="p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800/80 bg-white dark:bg-slate-900 shadow-md shadow-slate-100/30 dark:shadow-none space-y-6">
                  {/* Topics List */}
                  <div className="space-y-4">
                    <h4 className="text-sm font-semibold text-slate-500 dark:text-slate-400">
                      Topics & Concept Checklist
                    </h4>
                    
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      {phase.topics.map((topic, tIdx) => (
                        <div key={tIdx} className="p-4 rounded-xl border border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-950/20 space-y-2">
                          <p className="font-semibold text-sm text-slate-800 dark:text-slate-200 flex items-start gap-2">
                            <CheckCircle2 className="w-4 h-4 text-indigo-500 mt-0.5 shrink-0" />
                            <span>{topic.name}</span>
                          </p>
                          
                          <div className="flex flex-wrap gap-1.5 pl-6">
                            {topic.subtopics.map((sub, sIdx) => (
                              <span 
                                key={sIdx} 
                                className="px-2 py-0.5 rounded bg-white dark:bg-slate-900 border border-slate-200/60 dark:border-slate-800/60 text-slate-500 dark:text-slate-400 text-[10px] font-medium"
                              >
                                {sub}
                              </span>
                            ))}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Practice, Mini Project & Milestone Row */}
                  <div className="border-t border-slate-100 dark:border-slate-800 pt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
                    {/* Practice */}
                    <div className="space-y-2">
                      <p className="text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider">
                        Practice Schedule
                      </p>
                      <p className="text-sm text-slate-600 dark:text-slate-350 font-light">
                        {phase.practice_schedule}
                      </p>
                    </div>

                    {/* Milestone */}
                    <div className="space-y-2">
                      <p className="text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider flex items-center space-x-1">
                        <Trophy className="w-3.5 h-3.5 text-amber-500" />
                        <span>Phase Milestone Achievement</span>
                      </p>
                      <p className="text-sm text-slate-600 dark:text-slate-350 font-light">
                        {phase.milestone}
                      </p>
                    </div>
                  </div>

                  {/* Mini Project block */}
                  {phase.mini_project && (
                    <div className="border-t border-slate-100 dark:border-slate-800 pt-6">
                      <div className="p-4 rounded-2xl border border-indigo-100 dark:border-indigo-950/30 bg-indigo-50/20 dark:bg-indigo-950/10 space-y-2">
                        <div className="flex items-center space-x-2 text-indigo-600 dark:text-indigo-400">
                          <Terminal className="w-4 h-4" />
                          <h5 className="font-semibold text-sm">Mini Project: {phase.mini_project.title}</h5>
                        </div>
                        <p className="text-xs text-slate-500 dark:text-slate-450 leading-relaxed font-light pl-6">
                          {phase.mini_project.description}
                        </p>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Capstone Projects Section */}
      {roadmap.major_projects && roadmap.major_projects.length > 0 && (
        <div className="space-y-6 pt-6 border-t border-slate-200 dark:border-slate-900">
          <h2 className="font-display font-bold text-2xl text-slate-900 dark:text-white flex items-center space-x-2">
            <Trophy className="w-6 h-6 text-amber-500" />
            <span>Major Capstone Projects</span>
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {roadmap.major_projects.map((proj, idx) => (
              <div 
                key={idx} 
                className="p-6 rounded-3xl border border-slate-200 dark:border-slate-800/80 bg-white dark:bg-slate-900 hover:border-indigo-500 dark:hover:border-indigo-400 hover:shadow-lg transition-all duration-200 space-y-3"
              >
                <div className="inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-lg bg-amber-550/10 dark:bg-amber-500/10 text-amber-600 dark:text-amber-400 text-[10px] font-bold uppercase tracking-wider">
                  <span>CAPSTONE {idx + 1}</span>
                </div>
                <h4 className="font-display font-bold text-lg text-slate-800 dark:text-white">
                  {proj.title}
                </h4>
                <p className="text-slate-500 dark:text-slate-400 text-xs font-light leading-relaxed">
                  {proj.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

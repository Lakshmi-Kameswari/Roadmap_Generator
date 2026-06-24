import { useState, useEffect } from 'react';
import { Sparkles, Compass, AlertCircle } from 'lucide-react';
import { RoadmapInput } from './components/RoadmapInput';
import { RoadmapView } from './components/RoadmapView';
import { SkeletonLoader } from './components/SkeletonLoader';
import type { SkillRoadmap, UserProgress } from './types';

const API_BASE = 'http://localhost:8000';

function App() {
  const [roadmap, setRoadmap] = useState<SkillRoadmap | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isDownloadingPdf, setIsDownloadingPdf] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  
  const [progress, setProgress] = useState<UserProgress>({
    completedSubtopics: [],
    completedPhases: [],
  });

  // 1. Initial State Hydration from Local Storage
  useEffect(() => {
    const savedRoadmap = localStorage.getItem('skillpath_roadmap');
    const savedProgress = localStorage.getItem('skillpath_progress');
    
    if (savedRoadmap) {
      try {
        setRoadmap(JSON.parse(savedRoadmap));
      } catch (e) {
        localStorage.removeItem('skillpath_roadmap');
      }
    }
    
    if (savedProgress) {
      try {
        setProgress(JSON.parse(savedProgress));
      } catch (e) {
        localStorage.removeItem('skillpath_progress');
      }
    }
  }, []);

  // 2. API Request: Generate Roadmap
  const handleGenerateRoadmap = async (skillName: string) => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await fetch(`${API_BASE}/api/generate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ skill: skillName }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Failed to generate roadmap from the server.');
      }

      const data: SkillRoadmap = await response.json();
      
      // Save to state
      setRoadmap(data);
      
      // Reset checklist progress for the new skill
      const initialProgress: UserProgress = {
        completedSubtopics: [],
        completedPhases: [],
      };
      setProgress(initialProgress);

      // Persist in localStorage
      localStorage.setItem('skillpath_roadmap', JSON.stringify(data));
      localStorage.setItem('skillpath_progress', JSON.stringify(initialProgress));

    } catch (err: any) {
      console.error(err);
      setError(err.message || 'An unexpected error occurred. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  // 4. Interaction: Check/Uncheck subtopics
  const handleToggleSubtopic = (phaseIdx: number, topicIdx: number, subtopicIdx: number) => {
    const subtopicId = `${phaseIdx}-${topicIdx}-${subtopicIdx}`;
    
    setProgress((prev) => {
      const updatedSubs = prev.completedSubtopics.includes(subtopicId)
        ? prev.completedSubtopics.filter(id => id !== subtopicId)
        : [...prev.completedSubtopics, subtopicId];
        
      const updatedProgress = {
        ...prev,
        completedSubtopics: updatedSubs
      };
      
      localStorage.setItem('skillpath_progress', JSON.stringify(updatedProgress));
      return updatedProgress;
    });
  };

  // 5. API Request: Download Roadmap as PDF
  const handleDownloadPdf = async () => {
    if (!roadmap) return;
    setIsDownloadingPdf(true);
    setError(null);

    try {
      const response = await fetch(`${API_BASE}/api/download-pdf`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(roadmap),
      });

      if (!response.ok) {
        throw new Error('Failed to generate PDF. Check if the backend is running.');
      }

      const blob = await response.blob();
      const downloadUrl = window.URL.createObjectURL(blob);
      
      const link = document.createElement('a');
      link.href = downloadUrl;
      const cleanSkill = roadmap.skill_name.toLowerCase().replace(/[^a-z0-9]/g, '_');
      link.download = `${cleanSkill}_roadmap.pdf`;
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(downloadUrl);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Could not download PDF document. Please verify the backend service is running.');
    } finally {
      setIsDownloadingPdf(false);
    }
  };

  // 6. Navigation: Reset back to landing input screen
  const handleBackToSearch = () => {
    // We do NOT clear localStorage here, allowing the user to return to their progress using "Resume Current Path"
    setRoadmap(null);
  };

  // 7. Navigation: Resume cached path if one exists
  const handleResumePath = () => {
    const savedRoadmap = localStorage.getItem('skillpath_roadmap');
    if (savedRoadmap) {
      setRoadmap(JSON.parse(savedRoadmap));
    }
  };

  const hasCachedRoadmap = !!localStorage.getItem('skillpath_roadmap');
  const cachedSkillName = hasCachedRoadmap 
    ? JSON.parse(localStorage.getItem('skillpath_roadmap') || '{}').skill_name 
    : '';

  return (
    <div className="app-container">
      {/* Navigation Header */}
      <header className="navbar">
        <div className="nav-brand" onClick={handleBackToSearch}>
          <Compass className="nav-logo-glow" size={26} />
          <span>SkillPath <span className="gradient-text">AI</span></span>
        </div>
        <div className="nav-links">
          {hasCachedRoadmap && !roadmap && (
            <button onClick={handleResumePath} className="nav-link-btn flex-center gap-2">
              <Sparkles size={14} className="text-amber-400" />
              <span>Resume current: <strong>{cachedSkillName}</strong></span>
            </button>
          )}
        </div>
      </header>

      {/* Main Container */}
      <main className="main-content">
        {/* Error Notification Alert */}
        {error && (
          <div className="active-phase-practice animate-slide-down" style={{ background: 'rgba(244, 63, 94, 0.08)', border: '1px solid rgba(244, 63, 94, 0.2)', color: '#fda4af', marginBottom: '2rem' }}>
            <AlertCircle size={18} />
            <div style={{ flex: 1 }}>{error}</div>
            <button onClick={() => setError(null)} style={{ background: 'transparent', border: 'none', color: '#fda4af', cursor: 'pointer', fontWeight: 'bold' }}>✕</button>
          </div>
        )}

        {/* Conditional Component Rendering */}
        {isLoading ? (
          <SkeletonLoader />
        ) : roadmap ? (
          <RoadmapView
            roadmap={roadmap}
            progress={progress}
            onToggleSubtopic={handleToggleSubtopic}
            onDownloadPdf={handleDownloadPdf}
            isDownloadingPdf={isDownloadingPdf}
            onBack={handleBackToSearch}
          />
        ) : (
          <RoadmapInput
            onGenerate={handleGenerateRoadmap}
            isLoading={isLoading}
          />
        )}
      </main>

      {/* Footer Branding */}
      <footer className="footer">
        <p>&copy; {new Date().getFullYear()} SkillPath AI. Guided study blueprints powered by smart local generation.</p>
      </footer>
    </div>
  );
}

export default App;

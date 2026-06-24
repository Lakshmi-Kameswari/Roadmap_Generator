import React, { useState, useMemo } from 'react';
import { 
  ArrowLeft, Download, Clock, Calendar, CheckSquare, Square, 
  ChevronRight, Terminal, Award, BookOpen, Layers, CheckCircle2, ChevronDown 
} from 'lucide-react';
import type { SkillRoadmap, UserProgress } from '../types';

interface RoadmapViewProps {
  roadmap: SkillRoadmap;
  progress: UserProgress;
  onToggleSubtopic: (phaseIdx: number, topicIdx: number, subtopicIdx: number) => void;
  onDownloadPdf: () => void;
  isDownloadingPdf: boolean;
  onBack: () => void;
}

export const RoadmapView: React.FC<RoadmapViewProps> = ({
  roadmap,
  progress,
  onToggleSubtopic,
  onDownloadPdf,
  isDownloadingPdf,
  onBack,
}) => {
  const [activePhaseIdx, setActivePhaseIdx] = useState<number>(0);
  const [expandedTopicIdxs, setExpandedTopicIdxs] = useState<Record<string, boolean>>({});

  // 1. Calculate overall progress stats
  const stats = useMemo(() => {
    let totalSubtopics = 0;
    let completedCount = 0;

    roadmap.phases.forEach((phase, pIdx) => {
      phase.topics.forEach((topic, tIdx) => {
        topic.subtopics.forEach((_, sIdx) => {
          totalSubtopics++;
          const id = `${pIdx}-${tIdx}-${sIdx}`;
          if (progress.completedSubtopics.includes(id)) {
            completedCount++;
          }
        });
      });
    });

    const percent = totalSubtopics > 0 ? Math.round((completedCount / totalSubtopics) * 100) : 0;
    return { totalSubtopics, completedCount, percent };
  }, [roadmap, progress]);

  // 2. Calculate phase-specific progress stats
  const phaseStats = useMemo(() => {
    return roadmap.phases.map((phase, pIdx) => {
      let total = 0;
      let completed = 0;
      phase.topics.forEach((topic, tIdx) => {
        topic.subtopics.forEach((_, sIdx) => {
          total++;
          const id = `${pIdx}-${tIdx}-${sIdx}`;
          if (progress.completedSubtopics.includes(id)) {
            completed++;
          }
        });
      });
      const percent = total > 0 ? Math.round((completed / total) * 100) : 0;
      return { total, completed, percent };
    });
  }, [roadmap, progress]);

  const toggleTopicExpand = (tKey: string) => {
    setExpandedTopicIdxs(prev => ({
      ...prev,
      [tKey]: !prev[tKey]
    }));
  };

  const activePhase = roadmap.phases[activePhaseIdx] || roadmap.phases[0];

  return (
    <div className="roadmap-dashboard">
      {/* Top Controls & Navigation Bar */}
      <div className="dashboard-header animate-fade-in">
        <button onClick={onBack} className="btn-back">
          <ArrowLeft size={16} />
          <span>New Skill</span>
        </button>

        <div className="header-actions">
          <button 
            onClick={onDownloadPdf} 
            className="btn-download" 
            disabled={isDownloadingPdf}
          >
            {isDownloadingPdf ? (
              <>
                <span className="spinner-sm"></span>
                <span>Generating PDF...</span>
              </>
            ) : (
              <>
                <Download size={16} />
                <span>Download PDF Guide</span>
              </>
            )}
          </button>
        </div>
      </div>

      {/* Roadmap Title Banner */}
      <div className="roadmap-banner animate-fade-in">
        <div className="banner-details">
          <h1 className="banner-title">{roadmap.skill_name} Roadmap</h1>
          <p className="banner-subtitle">
            Your customized path to skill mastery. Complete topics, tackle projects, and unlock milestones.
          </p>
        </div>
        
        {/* Core Metadata Indicators */}
        <div className="banner-metadata">
          <div className="meta-badge">
            <Calendar size={18} className="meta-icon duration-icon" />
            <div className="meta-text">
              <span className="meta-label">Duration</span>
              <span className="meta-value">{roadmap.estimated_duration}</span>
            </div>
          </div>
          <div className="meta-badge">
            <Clock size={18} className="meta-icon schedule-icon" />
            <div className="meta-text">
              <span className="meta-label">Daily Study</span>
              <span className="meta-value">{roadmap.daily_study_time}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Progress Metric Bar */}
      <div className="progress-section-card animate-fade-in">
        <div className="progress-text-wrapper">
          <div className="progress-label">
            <Layers size={18} />
            <span>Overall Roadmap Progress</span>
          </div>
          <span className="progress-percentage">{stats.percent}% Completed</span>
        </div>
        <div className="progress-bar-container">
          <div 
            className="progress-bar-fill" 
            style={{ width: `${stats.percent}%` }}
          ></div>
        </div>
        <div className="progress-details">
          <span>{stats.completedCount} of {stats.totalSubtopics} topics completed</span>
        </div>
      </div>

      {/* Split Dashboard Content */}
      <div className="dashboard-grid">
        {/* Left Side: Phase Navigation Tree */}
        <div className="dashboard-sidebar">
          <h2 className="sidebar-heading">Learning Phases</h2>
          <div className="phase-navigation-list">
            {roadmap.phases.map((phase, pIdx) => {
              const isActive = activePhaseIdx === pIdx;
              const pStat = phaseStats[pIdx];
              return (
                <button
                  key={phase.phase_number}
                  onClick={() => setActivePhaseIdx(pIdx)}
                  className={`phase-nav-item ${isActive ? 'active' : ''}`}
                >
                  <div className="phase-nav-index">
                    {pStat.percent === 100 ? (
                      <CheckCircle2 size={18} className="text-emerald-400" />
                    ) : (
                      <span>{phase.phase_number}</span>
                    )}
                  </div>
                  <div className="phase-nav-info">
                    <span className="phase-nav-title">{phase.title}</span>
                    <span className="phase-nav-progress">{pStat.percent}% complete</span>
                  </div>
                  <ChevronRight size={16} className="phase-nav-arrow" />
                </button>
              );
            })}
          </div>

          {/* Final Outcome Card */}
          <div className="final-outcome-card">
            <div className="outcome-icon-wrapper">
              <Award size={24} />
            </div>
            <h3 className="outcome-title">Ultimate Mastery Goal</h3>
            <p className="outcome-desc">{roadmap.final_outcome}</p>
          </div>
        </div>

        {/* Right Side: Focus Area for Selected Phase */}
        <div className="dashboard-content-panel animate-slide-up">
          {/* Active Phase Info */}
          <div className="active-phase-header">
            <div className="active-phase-badge">Phase {activePhase.phase_number}</div>
            <h2 className="active-phase-title">{activePhase.title}</h2>
          </div>

          <div className="active-phase-practice">
            <Clock size={16} />
            <span><strong>Recommended Practice Plan:</strong> {activePhase.practice_schedule}</span>
          </div>

          {/* Topics & Checklist */}
          <div className="topics-section">
            <h3 className="section-title">
              <BookOpen size={18} />
              <span>Core Topics & Lessons</span>
            </h3>

            <div className="topics-list">
              {activePhase.topics.map((topic, tIdx) => {
                const topicKey = `${activePhaseIdx}-${tIdx}`;
                const isExpanded = expandedTopicIdxs[topicKey] !== false; // Default expanded
                
                // Calculate completion for this specific topic
                const topicSubtopics = topic.subtopics;
                const completedTopicSubs = topicSubtopics.filter((_, sIdx) => 
                  progress.completedSubtopics.includes(`${activePhaseIdx}-${tIdx}-${sIdx}`)
                ).length;
                const topicPercent = topicSubtopics.length > 0 
                  ? Math.round((completedTopicSubs / topicSubtopics.length) * 100) 
                  : 0;

                return (
                  <div key={tIdx} className={`topic-card ${isExpanded ? 'expanded' : ''}`}>
                    <div 
                      onClick={() => toggleTopicExpand(topicKey)}
                      className="topic-card-header"
                    >
                      <div className="topic-title-wrapper">
                        <span className="topic-name">{topic.name}</span>
                        <span className="topic-badge">{completedTopicSubs}/{topicSubtopics.length} done</span>
                      </div>
                      <div className="topic-header-right">
                        <div className="mini-progress-pill">{topicPercent}%</div>
                        {isExpanded ? <ChevronDown size={18} /> : <ChevronRight size={18} />}
                      </div>
                    </div>

                    {isExpanded && (
                      <div className="topic-subtopics-list">
                        {topic.subtopics.map((subtopic, sIdx) => {
                          const id = `${activePhaseIdx}-${tIdx}-${sIdx}`;
                          const isCompleted = progress.completedSubtopics.includes(id);
                          return (
                            <button
                              key={sIdx}
                              onClick={() => onToggleSubtopic(activePhaseIdx, tIdx, sIdx)}
                              className={`subtopic-row ${isCompleted ? 'completed' : ''}`}
                            >
                              <div className="checkbox-wrapper">
                                {isCompleted ? (
                                  <CheckSquare size={18} className="checkbox-icon checked" />
                                ) : (
                                  <Square size={18} className="checkbox-icon" />
                                )}
                              </div>
                              <span className="subtopic-name">{subtopic}</span>
                            </button>
                          );
                        })}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>

          {/* Phase Projects */}
          <div className="projects-section">
            <h3 className="section-title">
              <Terminal size={18} />
              <span>Hands-on Projects</span>
            </h3>
            
            <div className="projects-grid">
              {/* Mini Project Card */}
              {activePhase.mini_project && (
                <div className="project-card border-left-accent">
                  <div className="project-badge">Mini Project</div>
                  <h4 className="project-card-title">{activePhase.mini_project.title}</h4>
                  <p className="project-card-desc">{activePhase.mini_project.description}</p>
                  <div className="skills-tags">
                    {activePhase.mini_project.skills_used.map((skill, idx) => (
                      <span key={idx} className="skill-tag">{skill}</span>
                    ))}
                  </div>
                </div>
              )}

              {/* Major Capstone Card */}
              {activePhase.major_project && (
                <div className="project-card border-left-emerald">
                  <div className="project-badge bg-emerald-500">Major Capstone</div>
                  <h4 className="project-card-title">{activePhase.major_project.title}</h4>
                  <p className="project-card-desc">{activePhase.major_project.description}</p>
                  <div className="skills-tags">
                    {activePhase.major_project.skills_used.map((skill, idx) => (
                      <span key={idx} className="skill-tag bg-emerald-950/40 text-emerald-300 border-emerald-900">{skill}</span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Milestones Checklist */}
          {activePhase.milestones && activePhase.milestones.length > 0 && (
            <div className="milestones-section">
              <h3 className="section-title">
                <Award size={18} />
                <span>Phase Milestones</span>
              </h3>
              <div className="milestones-card">
                <p className="milestones-card-header-desc">
                  To complete this phase, you should confidently be able to demonstrate:
                </p>
                <ul className="milestone-list">
                  {activePhase.milestones.map((milestone, idx) => (
                    <li key={idx} className="milestone-item">
                      <div className="milestone-bullet"></div>
                      <span>{milestone}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

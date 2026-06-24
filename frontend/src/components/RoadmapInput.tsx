import React, { useState } from 'react';
import { Search, Sparkles, Terminal, Cpu, Shield, Cloud, Database } from 'lucide-react';

interface RoadmapInputProps {
  onGenerate: (skill: string) => void;
  isLoading: boolean;
}

const SAMPLE_SKILLS = [
  { name: 'Python Programming', icon: Terminal, color: 'from-blue-500 to-cyan-500', desc: 'From basic scripting to OOP and data structures.' },
  { name: 'Machine Learning & AI', icon: Cpu, color: 'from-purple-500 to-indigo-500', desc: 'Math foundation, Scikit-Learn, Deep Learning, and LLMs.' },
  { name: 'Full Stack Web Dev', icon: Database, color: 'from-emerald-500 to-teal-500', desc: 'HTML/CSS, React, Node.js, databases, and deployment.' },
  { name: 'Cybersecurity Analyst', icon: Shield, color: 'from-rose-500 to-red-500', desc: 'Networking, Linux, pen-testing, and threat intelligence.' },
  { name: 'Cloud DevOps Architect', icon: Cloud, color: 'from-amber-500 to-orange-500', desc: 'Docker, Kubernetes, CI/CD, AWS, and IaC.' },
];

export const RoadmapInput: React.FC<RoadmapInputProps> = ({
  onGenerate,
  isLoading,
}) => {
  const [skill, setSkill] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!skill.trim()) return;
    onGenerate(skill.trim());
  };

  const handleSampleClick = (sampleName: string) => {
    setSkill(sampleName);
    onGenerate(sampleName);
  };

  return (
    <div className="landing-container">
      {/* Hero Header */}
      <div className="hero-section">
        <div className="badge animate-fade-in">
          <Sparkles size={14} className="icon-pulse" />
          <span>Next-Generation Career Planner</span>
        </div>
        <h1 className="hero-title">
          Master Any Skill with <span className="gradient-text">SkillPath AI</span>
        </h1>
        <p className="hero-subtitle">
          Generate structured, step-by-step learning paths complete with study schedules, 
          practical projects, and downloadable guides. Track your progress dynamically as you learn.
        </p>
      </div>

      {/* Main Search/Input Form */}
      <form onSubmit={handleSubmit} className="search-form-card">
        <div className="search-input-wrapper">
          <Search className="search-icon" size={22} />
          <input
            type="text"
            placeholder="What skill do you want to learn? (e.g., React, Go Language, Piano...)"
            value={skill}
            onChange={(e) => setSkill(e.target.value)}
            className="search-input"
            disabled={isLoading}
            required
          />
          <button type="submit" className="btn-generate" disabled={isLoading || !skill.trim()}>
            {isLoading ? (
              <span className="flex-center gap-2">
                <span className="spinner-sm"></span> Analyzing...
              </span>
            ) : (
              <span className="flex-center gap-2">
                <Sparkles size={18} /> Generate Roadmap
              </span>
            )}
          </button>
        </div>


      </form>

      {/* Suggestion Cards */}
      <div className="suggestions-section">
        <h2 className="suggestions-title">Popular Learning Paths</h2>
        <div className="suggestions-grid">
          {SAMPLE_SKILLS.map((sample) => {
            const IconComponent = sample.icon;
            return (
              <button
                key={sample.name}
                onClick={() => handleSampleClick(sample.name)}
                className={`sample-card group`}
                disabled={isLoading}
              >
                <div className={`icon-container bg-gradient-to-br ${sample.color}`}>
                  <IconComponent size={24} className="sample-icon" />
                </div>
                <div className="sample-card-text">
                  <h3 className="sample-card-title">{sample.name}</h3>
                  <p className="sample-card-desc">{sample.desc}</p>
                </div>
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
};

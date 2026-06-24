export interface Project {
  title: string;
  description: string;
  skills_used: string[];
}

export interface Topic {
  name: string;
  subtopics: string[];
}

export interface Phase {
  phase_number: number;
  title: string;
  topics: Topic[];
  practice_schedule: string;
  mini_project: Project;
  major_project?: Project;
  milestones: string[];
}

export interface SkillRoadmap {
  skill_name: string;
  estimated_duration: string;
  daily_study_time: string;
  phases: Phase[];
  final_outcome: string;
}

export interface UserProgress {
  completedSubtopics: string[]; // Format: "phase_idx-topic_idx-subtopic_idx"
  completedPhases: number[];    // List of phase numbers (1-indexed)
}

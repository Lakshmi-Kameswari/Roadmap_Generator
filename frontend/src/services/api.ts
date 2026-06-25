const API_URL = 'https://roadmap-generator-bjlo.onrender.com';
export interface Skill {
  id: string;
  name: string;
  duration: string;
  daily_study_time: string;
}

export interface Topic {
  name: string;
  subtopics: string[];
}

export interface MiniProject {
  title: string;
  description: string;
}

export interface Phase {
  phase_title: string;
  duration: string;
  topics: Topic[];
  practice_schedule: string;
  mini_project?: MiniProject;
  milestone: string;
}

export interface MajorProject {
  title: string;
  description: string;
}

export interface Roadmap {
  skill_name: string;
  estimated_duration: string;
  daily_study_time: string;
  expected_outcome: string;
  phases: Phase[];
  major_projects: MajorProject[];
}

export async function fetchSkills(): Promise<Skill[]> {
  const response = await fetch(`${API_URL}/api/skills`);
  if (!response.ok) {
    throw new Error('Failed to fetch available skills.');
  }
  return response.json();
}

export async function fetchRoadmap(skill: string): Promise<Roadmap> {
  const response = await fetch(`${API_URL}/api/roadmaps/${encodeURIComponent(skill)}`);
  if (!response.ok) {
    if (response.status === 404) {
      throw new Error('LAnguage not Found ');
    }
    throw new Error('Failed to load roadmap.');
  }
  return response.json();
}

export function getPDFDownloadUrl(skill: string): string {
  return `${API_URL}/api/roadmaps/${encodeURIComponent(skill)}/pdf`;
}

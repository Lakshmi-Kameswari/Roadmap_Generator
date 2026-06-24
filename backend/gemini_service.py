import os
import json
from typing import List, Optional
from pydantic import BaseModel, Field
from mock_data import MOCK_ROADMAPS

# Define Structured Output Schemas using Pydantic (kept for interface compatibility)
class Project(BaseModel):
    title: str = Field(description="Title of the project")
    description: str = Field(description="Brief description of the project and what they will build")
    skills_used: List[str] = Field(description="Key skills or concepts practiced in this project")

class Topic(BaseModel):
    name: str = Field(description="Name of the topic, e.g., Variables, Conditions, OOP")
    subtopics: List[str] = Field(description="Detailed subtopics under this topic")

class Phase(BaseModel):
    phase_number: int = Field(description="Phase number, starting from 1")
    title: str = Field(description="Title of the learning phase, e.g., Programming Fundamentals")
    topics: List[Topic] = Field(description="Key topics to cover in this phase")
    practice_schedule: str = Field(description="Practice schedule recommendation, e.g., 1 Hour Daily")
    mini_project: Project = Field(description="Mini project for this phase to consolidate learning")
    major_project: Optional[Project] = Field(description="Major project for this phase (optional, recommended for advanced phases)")
    milestones: List[str] = Field(description="Learning milestones or outcomes for this phase")

class SkillRoadmap(BaseModel):
    skill_name: str = Field(description="The name of the skill")
    estimated_duration: str = Field(description="Estimated overall completion duration, e.g., 4-6 Months")
    daily_study_time: str = Field(description="Recommended daily study time, e.g., 2 Hours")
    phases: List[Phase] = Field(description="Sequential learning phases to reach expert level")
    final_outcome: str = Field(description="The final outcome or capability the learner will achieve")


def generate_roadmap_data(skill: str, api_key: Optional[str] = None) -> dict:
    """
    Generates a structured learning roadmap for the given skill without requiring API keys.
    Checks our high-quality hand-crafted repository first, otherwise constructs a smart
    dynamic template.
    """
    skill_clean = skill.strip()
    normalized = skill_clean.lower()
    
    # 1. Check for exact/fuzzy matches in high-quality pre-defined database
    if "python" in normalized:
        return MOCK_ROADMAPS["python programming"]
    elif "machine learning" in normalized or "ml" in normalized or "ai" in normalized or "artificial intelligence" in normalized:
        return MOCK_ROADMAPS["machine learning & ai"]
    elif "full stack" in normalized or "fullstack" in normalized or "web dev" in normalized or "web development" in normalized:
        return MOCK_ROADMAPS["full stack web dev"]
    elif "cyber" in normalized or "security" in normalized or "hacking" in normalized or "penetration" in normalized:
        return MOCK_ROADMAPS["cybersecurity analyst"]
    elif "devops" in normalized or "cloud" in normalized or "aws" in normalized or "kubernetes" in normalized or "docker" in normalized:
        return MOCK_ROADMAPS["cloud devops architect"]
    elif "react" in normalized:
        return MOCK_ROADMAPS["react.js"]
    elif "go language" in normalized or "golang" in normalized or normalized == "go":
        return MOCK_ROADMAPS["go language"]
    elif "ui/ux" in normalized or "ui" in normalized or "ux" in normalized or "design" in normalized:
        return MOCK_ROADMAPS["ui/ux design"]
        
    # 2. Build a highly-customized dynamic roadmap if no preset match exists
    return generate_dynamic_roadmap(skill_clean)


def generate_dynamic_roadmap(skill: str) -> dict:
    normalized = skill.lower()
    
    # Define category keywords
    coding_keywords = [
        "programming", "code", "coder", "language", "script", "sql", "java", "c++", 
        "c#", "ruby", "rust", "swift", "kotlin", "php", "typescript", "javascript", 
        "html", "css", "database", "backend", "frontend", "git", "bash", "linux"
    ]
    
    music_keywords = [
        "piano", "guitar", "violin", "music", "singing", "art", "drawing", "paint", 
        "photography", "dance", "cooking", "chess", "instrument"
    ]
    
    # Determine the category of the skill
    is_coding = any(kw in normalized for kw in coding_keywords)
    is_creative = any(kw in normalized for kw in music_keywords)
    
    if is_coding:
        return {
            "skill_name": f"{skill} Mastery",
            "estimated_duration": "3-4 Months",
            "daily_study_time": "2 Hours",
            "final_outcome": f"Proficiency in {skill}, enabling you to write clean syntax, modularize structures, and deploy real-world {skill} applications.",
            "phases": [
                {
                    "phase_number": 1,
                    "title": f"{skill} Syntax & Environment Setup",
                    "practice_schedule": "1 Hour Daily",
                    "topics": [
                        {
                            "name": f"Foundations of {skill}",
                            "subtopics": [f"Basic syntax and primitives in {skill}", f"Variables and constant assignments", f"Setting up the development workspace for {skill}", f"Running your first {skill} programs"]
                        },
                        {
                            "name": "Control Flow & Logic",
                            "subtopics": [f"Conditional structures (if-else, switch) in {skill}", f"Loops and iterations", f"Simple logical operations and formatting"]
                        }
                    ],
                    "mini_project": {
                        "title": f"Simple {skill} CLI Utility",
                        "description": f"Construct an interactive terminal/console application demonstrating basic syntax and logical flow using {skill}.",
                        "skills_used": [f"{skill} foundations", "Control Flow", "Console I/O"]
                    },
                    "milestones": [
                        f"Install and verify the compiler/runtime environment for {skill}",
                        f"Declare variables, structures, and use control flows in {skill}",
                        f"Write working console inputs and output parsers successfully"
                    ]
                },
                {
                    "phase_number": 2,
                    "title": f"Intermediate {skill} Concepts & Modularization",
                    "practice_schedule": "1.5 Hours Daily",
                    "topics": [
                        {
                            "name": f"Functions & Data Collections in {skill}",
                            "subtopics": [f"Creating custom reusable functions in {skill}", f"Understanding scope and parameter values", f"Managing data arrays, slices, or lists"]
                        },
                        {
                            "name": f"Object-Oriented/Modular {skill}",
                            "subtopics": [f"Structuring components or classes in {skill}", f"Method associations and interfaces", f"Error catching and standard exception flows"]
                        }
                    ],
                    "mini_project": {
                        "title": "Object-Oriented Model Directory",
                        "description": f"Build a local console contact or book management directory that handles records in memory using {skill} structures.",
                        "skills_used": [f"Functions in {skill}", "Structs/Classes", "Error Handling"]
                    },
                    "milestones": [
                        f"Decouple code patterns into separate modules and custom functions",
                        f"Model user objects and establish associations inside {skill}",
                        f"Handle runtime exceptions to prevent execution crashes"
                    ]
                },
                {
                    "phase_number": 3,
                    "title": f"Files, Libraries & Asynchronous workflows",
                    "practice_schedule": "2 Hours Daily",
                    "topics": [
                        {
                            "name": "File Systems & Local Files",
                            "subtopics": [f"Reading and writing files locally using {skill}", f"Handling structured CSV or JSON templates", f"Managing path cross-compatibility"]
                        },
                        {
                            "name": f"API Requests & Network in {skill}",
                            "subtopics": [f"Performing HTTP requests and consuming responses", f"Parsing JSON API payloads", f"Managing asynchronous threading or tasks"]
                        }
                    ],
                    "mini_project": {
                        "title": "Automated Weather Parser",
                        "description": f"Write a script that queries a public weather API, retrieves current coordinates, parses details, and writes a Markdown report to a local folder.",
                        "skills_used": [f"HTTP requests in {skill}", "JSON Parsing", "Local File Writes"]
                    },
                    "milestones": [
                        f"Connect to remote REST APIs using {skill} network clients",
                        f"Save and parse local records (JSON/CSV) onto host filesystems",
                        f"Manipulate data streams using intermediate async logic"
                    ]
                },
                {
                    "phase_number": 4,
                    "title": f"Databases & Full Scale {skill} Applications",
                    "practice_schedule": "2 Hours Daily",
                    "topics": [
                        {
                            "name": "Database Drivers & Integration",
                            "subtopics": [f"Connecting {skill} to relational databases (SQLite/PostgreSQL)", f"Executing secure parameterized queries", f"Designing schema tables and migrations"]
                        },
                        {
                            "name": "Production APIs & Cloud Handoff",
                            "subtopics": [f"Exposing REST HTTP routes or UI dashboards", f"Containerizing your {skill} codebase using Docker", f"Securing environment parameters and endpoints"]
                        }
                    ],
                    "major_project": {
                        "title": f"Comprehensive {skill} Case Tracker Hub",
                        "description": f"Design and build a multi-phase system using {skill}. Connects to a local database to store logs, provides a REST API backend, validates inputs, and is containerized via Docker.",
                        "skills_used": [f"{skill} APIs", "SQLite/PostgreSQL", "Environment Config", "Docker"]
                    },
                    "milestones": [
                        f"Configure secure database connections and handle SQL schemas from {skill}",
                        f"Dockerize and deploy your {skill} codebase package to cloud platforms",
                        f"Expose working HTTP routes with auth headers and input checks"
                    ]
                }
            ]
        }
    elif is_creative:
        return {
            "skill_name": f"{skill} Blueprints",
            "estimated_duration": "3-4 Months",
            "daily_study_time": "1.5 Hours",
            "final_outcome": f"Gain the technical mastery and muscle memory needed to perform, sketch, or execute {skill} pieces, progressing from foundations to creative expression.",
            "phases": [
                {
                    "phase_number": 1,
                    "title": f"Basic Mechanics & Notation of {skill}",
                    "practice_schedule": "30 Mins Daily",
                    "topics": [
                        {
                            "name": f"Understanding {skill} Instruments/Tools",
                            "subtopics": [f"Identifying parts of your {skill} setup", f"Proper posture, grip, or placement guidelines", f"Configuring and maintaining your equipment"]
                        },
                        {
                            "name": "Notation & Simple Exercises",
                            "subtopics": [f"Reading notes, scales, or basic styling tags", f"Performing simple 4-bar rhythms or outlines", f"Developing hand-eye coordination for {skill}"]
                        }
                    ],
                    "mini_project": {
                        "title": f"Simple 4-Bar {skill} Routine",
                        "description": f"Create and execute a short, basic 4-bar performance or outline sketch demonstrating clean alignment and posture.",
                        "skills_used": ["Posture setup", "Basic scale / line drawings", "Timing / spacing"]
                    },
                    "milestones": [
                        f"Set up and configure your workspace or instrument for {skill}",
                        f"Recognize and execute fundamental notes, colors, or postures",
                        f"Perform simple introductory practices continuously without stopping"
                    ]
                },
                {
                    "phase_number": 2,
                    "title": f"Intermediate Controls & Harmony in {skill}",
                    "practice_schedule": "1 Hour Daily",
                    "topics": [
                        {
                            "name": "Scale Shifts & Shading Dynamics",
                            "subtopics": [f"Transitioning between different notes or shading levels in {skill}", f"Developing tempo controls and rhythmic precision", f"Ear training / visual analysis practices"]
                        },
                        {
                            "name": "Combining Elements",
                            "subtopics": [f"Playing chords or blending complex colors in {skill}", f"Applying syncopation or perspective depths", f"Learning popular classical structures"]
                        }
                    ],
                    "mini_project": {
                        "title": f"Intermediate {skill} Performance",
                        "description": f"Perform or render a full intermediate-level classical study piece or detailed artwork, utilizing proper timing and tone control.",
                        "skills_used": ["Transitions", "Tone adjustment", "Hand synchronization"]
                    },
                    "milestones": [
                        f"Smoothly shift between chords, keys, or canvas coordinates in {skill}",
                        f"Maintain consistent rhythm, timing, or lighting values throughout a piece",
                        f"Replicate intermediate exercises with accurate feedback loops"
                    ]
                },
                {
                    "phase_number": 3,
                    "title": f"Advanced Creative Expressions of {skill}",
                    "practice_schedule": "1.5 Hours Daily",
                    "topics": [
                        {
                            "name": f"Advanced Patterns in {skill}",
                            "subtopics": [f"Minor scales, advanced chords, or complex textures", f"Improvisation and self-expression methods", f"Speed and accuracy optimization exercises"]
                        },
                        {
                            "name": "Professional Project Assembly",
                            "subtopics": [f"Structuring a full performance list or portfolio", f"Recording, editing, or packaging your work", f"Critique and community alignment systems"]
                        }
                    ],
                    "mini_project": {
                        "title": f"Original {skill} Arrangement",
                        "description": f"Arrange or create an original variation of a popular piece or compose a portfolio-level design demonstrating individual style.",
                        "skills_used": ["Improvisation", "Advanced mechanics", "Creative styling"]
                    },
                    "major_project": {
                        "title": f"Public Solo {skill} Showcase",
                        "description": f"Compile a complete showcase containing 3 distinct pieces or a digital gallery, record the performance or photograph the works, and document the project journey.",
                        "skills_used": ["Portfolio building", "Project recording", "Aesthetic styling"]
                    },
                    "milestones": [
                        f"Perform or design an original piece incorporating advanced {skill} techniques",
                        f"Improvise variations over generic chord structures or canvas layouts",
                        f"Publish or showcase your creative works in public portfolios"
                    ]
                }
            ]
        }
    else:
        # Generic category
        return {
            "skill_name": f"{skill} Mastery Guide",
            "estimated_duration": "3-4 Months",
            "daily_study_time": "2 Hours",
            "final_outcome": f"Comprehensive capability and deep knowledge in {skill}, going from core foundations to advanced optimization and practical implementation.",
            "phases": [
                {
                    "phase_number": 1,
                    "title": f"Introduction & Core Concepts of {skill}",
                    "practice_schedule": "1 Hour Daily",
                    "topics": [
                        {
                            "name": f"Foundations of {skill}",
                            "subtopics": [f"Basic concepts and terminology of {skill}", f"Core tools, resources, and environment settings", f"Understanding the industry landscape of {skill}"]
                        },
                        {
                            "name": "Core Processes & Vocabulary",
                            "subtopics": [f"Fundamental operations in {skill}", f"Configuring variables, plans, or attributes", f"Common introductory exercises"]
                        }
                    ],
                    "mini_project": {
                        "title": f"Simple {skill} Starter Assessment",
                        "description": f"A basic project applying core setup, environment checks, and introductory syntax or guidelines of {skill}.",
                        "skills_used": [f"{skill} setup", "Basic configuration", "Goal mapping"]
                    },
                    "milestones": [
                        f"Configure development environment or study workspace for {skill}",
                        f"Explain core vocabulary and concepts of {skill} successfully",
                        f"Complete first set of introductory templates or exercises"
                    ]
                },
                {
                    "phase_number": 2,
                    "title": f"Intermediate {skill} Workflows & Application",
                    "practice_schedule": "1.5 Hours Daily",
                    "topics": [
                        {
                            "name": f"Standard Workflows in {skill}",
                            "subtopics": [f"Working with intermediate data streams in {skill}", f"Common structures, styles, and patterns", f"Applying standard operating methods"]
                        },
                        {
                            "name": "Integration & Troubleshooting",
                            "subtopics": [f"Connecting {skill} concepts to external scenarios", f"Error catching, validation, and correction in {skill}", f"Best practices and standard methodologies"]
                        }
                    ],
                    "mini_project": {
                        "title": f"Intermediate {skill} Dashboard",
                        "description": f"Build or design a project that utilizes intermediate patterns and handles common scenarios in {skill}.",
                        "skills_used": ["Advanced patterns", "Error handling", "Workflow design"]
                    },
                    "milestones": [
                        f"Implement intermediate features or workflows of {skill} successfully",
                        f"Handle standard errors, edge cases, and troubleshooting in project setups",
                        f"Formulate comprehensive plans for resolving intermediate challenges"
                    ]
                },
                {
                    "phase_number": 3,
                    "title": f"Advanced {skill} & Optimization",
                    "practice_schedule": "2 Hours Daily",
                    "topics": [
                        {
                            "name": f"Performance Tuning & Scaling in {skill}",
                            "subtopics": [f"Memory management or performance parameters in {skill}", f"Concurrency, scale, and resource optimization", f"Profiling bottlenecks and refactoring methods"]
                        },
                        {
                            "name": "Production Operations & Deployment",
                            "subtopics": [f"Security compliance and safety checks for {skill}", f"Testing suites and quality assurance audits", f"Hosting, deployment, and cloud setups"]
                        }
                    ],
                    "mini_project": {
                        "title": f"Optimized {skill} Sandbox Refactoring",
                        "description": f"Refactor an existing pipeline, checklist, or script to optimize performance under load conditions.",
                        "skills_used": ["Performance tuning", "Profiling tools", "Refactoring"]
                    },
                    "major_project": {
                        "title": f"End-to-End {skill} Production Case Study",
                        "description": f"A comprehensive final project integrating intermediate and advanced workflows, databases, APIs, or portfolios for {skill}.",
                        "skills_used": ["Integration", "Performance tuning", "Database storage", "Deployment"]
                    },
                    "milestones": [
                        f"Deploy a production-grade or portfolio-ready {skill} application",
                        f"Identify and resolve scale or design bottlenecks under stress tests",
                        f"Configure automated testing, verification, and monitoring alerts"
                    ]
                }
            ]
        }

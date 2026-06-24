import sys
import os

# Ensure the parent directory is in the import path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pdf_service import generate_roadmap_pdf

mock_roadmap = {
    "skill_name": "Python Programming",
    "estimated_duration": "4-6 Months",
    "daily_study_time": "2 Hours",
    "final_outcome": "Capable of building full-stack web applications and automating scripts.",
    "phases": [
        {
            "phase_number": 1,
            "title": "Python Fundamentals",
            "practice_schedule": "1 Hour Daily",
            "topics": [
                {
                    "name": "Variables & Basic Types",
                    "subtopics": ["Integer", "Float", "String", "Boolean", "Type Conversion"]
                },
                {
                    "name": "Control Flow structures",
                    "subtopics": ["if-else conditions", "for loops", "while loops", "break and continue"]
                }
            ],
            "mini_project": {
                "title": "Command-Line Calculator",
                "description": "Build a command line calculator that supports continuous math operations.",
                "skills_used": ["Variables", "Operators", "While loops"]
            },
            "major_project": {
                "title": "Student Database Directory",
                "description": "Create a console database where details can be added, updated, searched, and stored in JSON files.",
                "skills_used": ["File I/O", "Dictionaries", "Functions"]
            },
            "milestones": [
                "Declare variables and perform data type operations",
                "Construct conditional loops and handle nesting logic",
                "Write functions and execute clean error structures"
            ]
        },
        {
            "phase_number": 2,
            "title": "Object-Oriented Programming (OOP)",
            "practice_schedule": "1.5 Hours Daily",
            "topics": [
                {
                    "name": "Classes & Attributes",
                    "subtopics": ["__init__ constructor", "Self keyword", "Instance attributes", "Class attributes"]
                },
                {
                    "name": "Pillars of OOP",
                    "subtopics": ["Inheritance", "Polymorphism", "Encapsulation", "Abstraction"]
                }
            ],
            "mini_project": {
                "title": "Library Cataloging Application",
                "description": "Develop a class-based catalog structure supporting checkout states and book lists.",
                "skills_used": ["Classes", "Inheritance", "Lists of objects"]
            },
            "milestones": [
                "Understand abstraction and build child classes using inheritance",
                "Manage complex code flows by organizing methods dynamically"
            ]
        }
    ]
}

def test_generation():
    print("Testing PDF creation...")
    try:
        pdf_stream = generate_roadmap_pdf(mock_roadmap)
        
        output_filename = "test_output.pdf"
        with open(output_filename, "wb") as f:
            f.write(pdf_stream.getbuffer())
        
        print(f"Success! PDF has been generated and saved to: {os.path.abspath(output_filename)}")
    except Exception as e:
        print(f"Error during PDF generation: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    test_generation()

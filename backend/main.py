import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel
import tempfile

# Import the PDF generator
from pdf_generator import generate_roadmap_pdf

app = FastAPI(title="SkillPath AI Backend API")

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ROADMAPS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "roadmaps")

# Ensure roadmaps directory exists
os.makedirs(ROADMAPS_DIR, exist_ok=True)

def get_normalized_skills_map():
    """Scans the roadmaps folder and returns a map of lowercased keys to their filename/path."""
    skills_map = {}
    if not os.path.exists(ROADMAPS_DIR):
        return skills_map
        
    for filename in os.listdir(ROADMAPS_DIR):
        if filename.endswith(".json"):
            skill_key = os.path.splitext(filename)[0].lower()
            skills_map[skill_key] = filename
    return skills_map

ALIASES = {
    "data science": "datascience",
    "cyber security": "cybersecurity",
    "mern stack": "mern",
    "mernstack": "mern",
    "cloud computing": "cloud",
    "cloudcomputing": "cloud",
    "artificial intelligence": "ai",
    "artificialintelligence": "ai",
    "java script": "javascript",
    "node js": "nodejs",
    "play write": "playwright",
    "playwrite": "playwright",
    "java full stack": "javafullstack",
    "javafull stack": "javafullstack",
    "next js": "nextjs",
    "spring boot": "springboot",
    "type script": "typescript",
    "mongo db": "mongodb"
}

def resolve_skill_key(query: str, skills_map: dict) -> str:
    """Resolves a raw query string to a valid key in skills_map using aliases and fallback checks."""
    normalized = query.strip().lower()
    
    # 1. Direct match
    if normalized in skills_map:
        return normalized
        
    # 2. Alias mapping match
    if normalized in ALIASES and ALIASES[normalized] in skills_map:
        return ALIASES[normalized]
        
    # 3. Space-removed match (e.g. "datascience" or "cybersecurity")
    spaceless = normalized.replace(" ", "")
    if spaceless in skills_map:
        return spaceless
        
    # 4. Partial/substring matching
    for key in skills_map.keys():
        if key in normalized or normalized in key:
            return key
            
    return None

@app.get("/api/skills")
async def list_skills():
    """Lists all available skills in the database with metadata."""
    skills_map = get_normalized_skills_map()
    skills_list = []
    
    for key, filename in skills_map.items():
        filepath = os.path.join(ROADMAPS_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                skills_list.append({
                    "id": key,
                    "name": data.get("skill_name", key.capitalize()),
                    "duration": data.get("estimated_duration", ""),
                    "daily_study_time": data.get("daily_study_time", "")
                })
        except Exception:
            # Skip invalid JSON files
            continue
            
    return skills_list

@app.get("/api/roadmaps/{skill}")
async def get_roadmap(skill: str):
    """Retrieves a specific roadmap by name (case-insensitive)."""
    skills_map = get_normalized_skills_map()
    resolved_key = resolve_skill_key(skill, skills_map)
    
    if not resolved_key:
        raise HTTPException(status_code=404, detail=f"Skill '{skill}' is not available in the database.")
        
    filepath = os.path.join(ROADMAPS_DIR, skills_map[resolved_key])
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading roadmap data: {str(e)}")

@app.get("/api/roadmaps/{skill}/pdf")
async def download_pdf(skill: str):
    """Generates and streams a PDF for the requested roadmap."""
    skills_map = get_normalized_skills_map()
    resolved_key = resolve_skill_key(skill, skills_map)
    
    if not resolved_key:
        raise HTTPException(status_code=404, detail=f"Skill '{skill}' is not available in the database.")
        
    filepath = os.path.join(ROADMAPS_DIR, skills_map[resolved_key])
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            skill_data = json.load(f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading roadmap database: {str(e)}")
        
    # Generate the PDF to a temporary file
    try:
        # Create a temporary file that will persist long enough to be sent
        fd, temp_file_path = tempfile.mkstemp(suffix=".pdf")
        os.close(fd) # Close file descriptor so pdf_generator can write to it
        
        generate_roadmap_pdf(skill_data, temp_file_path)
        
        # Clean up utility that can delete the file after response completes
        # FastAPI's FileResponse supports background tasks, or we can serve it directly.
        # To avoid keeping files, we can read it into memory, delete it, and return a Response.
        with open(temp_file_path, "rb") as f:
            pdf_content = f.read()
            
        try:
            os.remove(temp_file_path)
        except OSError:
            pass # ignore clean up issue
            
        skill_filename = skill_data.get('skill_name', skill).replace(" ", "_")
        return Response(
            content=pdf_content,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f'attachment; filename="{skill_filename}_Roadmap.pdf"'
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate PDF: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

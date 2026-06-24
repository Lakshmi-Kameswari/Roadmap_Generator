import os
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException, Header, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# Import our custom services
from gemini_service import generate_roadmap_data
from pdf_service import generate_roadmap_pdf

# Load environment variables from .env if present
load_dotenv()

app = FastAPI(
    title="SkillPath AI Backend",
    description="FastAPI service to generate custom learning roadmaps using Gemini and export them to PDF",
    version="1.0.0"
)

# Configure CORS so our React frontend can query the APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev simplicity, configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    skill: str

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "SkillPath AI"}

@app.post("/api/generate")
async def generate_roadmap(request: GenerateRequest):
    """
    Generates a structured learning roadmap for a given skill locally.
    """
    skill = request.skill.strip()
    if not skill:
        raise HTTPException(status_code=400, detail="Skill name cannot be empty.")
    
    try:
        roadmap_data = generate_roadmap_data(skill)
        return roadmap_data
    except ValueError as val_err:
        raise HTTPException(status_code=400, detail=str(val_err))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while generating the roadmap: {str(e)}"
        )

@app.post("/api/download-pdf")
async def download_pdf(roadmap: Dict[str, Any]):
    """
    Accepts a roadmap JSON object and returns a downloadable PDF stream.
    """
    try:
        # Generate the PDF file in memory
        pdf_buffer = generate_roadmap_pdf(roadmap)
        
        # Clean skill name for filename
        skill_name = roadmap.get("skill_name", "skill").lower().replace(" ", "_")
        filename = f"{skill_name}_roadmap.pdf"
        
        return StreamingResponse(
            pdf_buffer,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f'attachment; filename="{filename}"'
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate PDF document: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    # Read host and port from environment, or use defaults
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8000))
    
    uvicorn.run("main:app", host=host, port=port, reload=True)

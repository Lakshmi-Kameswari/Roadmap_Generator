import os
import json
import urllib.request
from pdf_generator import generate_roadmap_pdf

def test_pdf_generation():
    print("Testing PDF generation locally...")
    json_path = os.path.join("roadmaps", "python.json")
    with open(json_path, "r", encoding="utf-8") as f:
        skill_data = json.load(f)
        
    output_pdf = "test_python_roadmap.pdf"
    try:
        generate_roadmap_pdf(skill_data, output_pdf)
        assert os.path.exists(output_pdf), "PDF file was not created!"
        print(f"[SUCCESS] PDF generated successfully at {output_pdf}")
        # Clean up
        os.remove(output_pdf)
    except Exception as e:
        print(f"[FAILURE] PDF generation failed: {e}")
        raise e

def test_api_endpoints():
    print("Testing API endpoints on running server...")
    try:
        # Test /api/skills
        with urllib.request.urlopen("http://127.0.0.1:8000/api/skills") as response:
            skills = json.loads(response.read().decode())
            print(f"[SUCCESS] Found {len(skills)} skills:")
            for s in skills:
                print(f" - {s['name']} ({s['duration']}, {s['daily_study_time']})")
            
        # Test /api/roadmaps/python
        with urllib.request.urlopen("http://127.0.0.1:8000/api/roadmaps/python") as response:
            roadmap = json.loads(response.read().decode())
            assert roadmap["skill_name"] == "Python", "Skill name mismatch!"
            print(f"[SUCCESS] Successfully retrieved Python roadmap data.")
            
    except Exception as e:
        print(f"[FAILURE] API endpoints test failed: {e}")
        raise e

if __name__ == "__main__":
    test_pdf_generation()
    test_api_endpoints()
    print("All backend checks passed successfully!")

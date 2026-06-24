# SkillPath AI 🧭

SkillPath AI is a premium, full-stack web application that leverages artificial intelligence to generate personalized, multi-phase learning roadmaps for any skill. The application provides an interactive learning dashboard where users can check off completed topics, track their visual progress in real-time, view hands-on milestones, and export a styled, multi-page PDF guide.

---

## Technical Stack

- **Frontend**: React, TypeScript, Vite, Vanilla CSS (custom glassmorphic theme).
- **Backend**: FastAPI (Python), Uvicorn.
- **AI Engine**: Google Gemini API via official `google-generativeai` SDK.
- **PDF Engine**: ReportLab.

---

## Project Structure

```text
RoadMap Generator/
├── backend/
│   ├── main.py              # FastAPI app setup, routes, and CORS config
│   ├── gemini_service.py    # Gemini AI integration using structured schemas
│   ├── pdf_service.py       # Custom ReportLab PDF compiler
│   ├── requirements.txt     # Python requirements
│   └── .env.example         # Template for environment configuration
├── frontend/
│   ├── src/
│   │   ├── components/      
│   │   │   ├── RoadmapInput.tsx   # Landing UI & search form
│   │   │   ├── RoadmapView.tsx    # Interactive dashboard & progress tracker
│   │   │   └── SkeletonLoader.tsx # Animated layout placeholder
│   │   ├── App.tsx          # State manager & API client
│   │   ├── index.css        # Premium custom CSS stylesheets
│   │   ├── types.ts         # Shared TS interface definitions
│   │   └── main.tsx         
│   ├── index.html           
│   ├── package.json         
│   └── vite.config.ts       
└── README.md                # System setup & startup manual
```

---

## Setup & Running Instructions

### Prerequisites
1. **Python**: Version 3.8 or higher.
2. **NodeJS & NPM**: Node version 18.0 or higher.
3. **Gemini API Key**: Obtain one from [Google AI Studio](https://aistudio.google.com/).

---

### Step 1: Run the Backend Server

1. Open a new terminal in the `backend` directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # Activate virtualenv on Windows:
   .\venv\Scripts\activate
   # Activate virtualenv on macOS/Linux:
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your environment:
   - Create a `.env` file copying `.env.example`:
     ```bash
     copy .env.example .env
     ```
   - Edit the `.env` file and insert your `GEMINI_API_KEY`:
     ```text
     GEMINI_API_KEY=AIzaSy...
     ```
     *(Note: If you leave this blank, you will need to input your Gemini key in the frontend settings panel).*

5. Run the FastAPI development server:
   ```bash
   python main.py
   ```
   The backend server will launch at `http://127.0.0.1:8000`.

---

### Step 2: Run the Frontend Server

1. Open a new terminal in the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install dependencies (if not already done):
   ```bash
   npm install
   ```

3. Start the Vite React development server:
   ```bash
   npm run dev
   ```
   The frontend application will be hosted at `http://localhost:5173`. Open this URL in your web browser.

---

## How to Use the Application

1. **Enter Skill**: Type any skill you want to learn (e.g., "Docker", "Machine Learning", "Go Programming", "Oil Painting") in the search input and click **Generate Roadmap**. Or, click one of the pre-configured popular paths.
2. **Dynamic Progress Tracking**: As you complete topics, click on the subtopic checklist inside each phase card. The overall roadmap progress indicator will update automatically.
3. **Persist State**: Your progress is stored locally. You can close the tab or refresh the page, and clicking **Resume current path** on the landing page will load your exact roadmap and checklist state.
4. **PDF Download**: Click the **Download PDF Guide** button at the top-right of your dashboard. The backend will compile the current roadmap JSON into a publication-quality multi-page PDF formatted with phase dividers, project tables, and milestone checklists.

# SkillPath AI - Predefined Roadmap Generator

SkillPath AI is a modern production-ready web application designed to help users learn any skill through a structured, phase-by-phase learning path. It retrieves learning paths from a local JSON database and provides an option to download a professional PDF curriculum vector format.

---

## Technical Stack

* **Frontend**: React (Vite + TypeScript), Tailwind CSS, React Router, Lucide Icons
* **Backend**: Python FastAPI, FPDF2 (PDF generation)
* **Database**: Local JSON Database files
* **State Management**: React Hooks (useState, useEffect, useRef)

---

## Project Structure

```text
SkillPathAI/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Layout.tsx          # Main layout header, footer, dark mode toggle
│   │   │   └── SkeletonLoader.tsx  # Pulse skeletons for premium loading transition
│   │   ├── pages/
│   │   │   ├── Home.tsx            # Autocomplete search & popular path tags
│   │   │   └── RoadmapView.tsx     # Timeline visualizer & PDF trigger
│   │   ├── services/
│   │   │   └── api.ts              # API fetch networking calls and TS interfaces
│   │   ├── App.tsx                 # Route declarations
│   │   └── index.css               # Styling definitions & Google Fonts import
│   ├── tailwind.config.js          # Tailwind styling scanning configs
│   ├── .env                        # Local port mapping env definition
│   └── package.json                # Frontend dependencies
│
├── backend/
│   ├── roadmaps/                   # Predefined Roadmap Database Files
│   │   ├── python.json
│   │   ├── java.json
│   │   ├── ai.json
│   │   ├── datascience.json
│   │   ├── cybersecurity.json
│   │   ├── devops.json
│   │   ├── cloud.json
│   │   └── mern.json
│   ├── main.py                     # FastAPI server with CORS & alias-lookup mappings
│   ├── pdf_generator.py            # FPDF2 custom vector document compiling engine
│   ├── test_backend.py             # Local sanity verification script
│   └── requirements.txt            # Python dependencies
│
├── README.md                       # Comprehensive setup guide
└── .gitignore                      # Git tracking exclude file
```

---

## Setup & Running Locally

### Prerequisites
Make sure you have **Node.js (v24+)** and **Python (3.12+)** installed on your system.

---

### 1. Run the Python FastAPI Backend

1. Navigate to the `backend/` directory in your terminal.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   * **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   * **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the server using Uvicorn:
   ```bash
   python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```
   The backend API will be live at: `http://localhost:8000`. You can inspect the interactive swagger docs at `http://localhost:8000/docs`.

---

### 2. Run the React Frontend

1. Navigate to the `frontend/` directory in a new terminal window.
2. Install the required packages:
   ```bash
   npm install
   ```
3. Create a `.env` file in the `frontend/` folder (if it doesn't already exist) and define the backend URL:
   ```env
   VITE_API_URL=http://localhost:8000
   ```
4. Start the development server:
   ```bash
   npm run dev
   ```
   Open your browser and navigate to `http://localhost:5173/` to view the application!

---

## Predefined Roadmap Catalog

The local database currently holds robust, production-ready syllabuses for:
1. **Python** (Basic variables, control flows, OOP, database REST configurations)
2. **Java** (JDK architectures, OOP encapsulation, lists/streams, Spring Boot web backend)
3. **Artificial Intelligence** (Linear Algebra/Statistics, classical ML, deep CNN/transformer networks, MLOps)
4. **Data Science** (SQL querying, pandas data wrangling, Scikit-learn models, Streamlit dashboard reporting)
5. **Cyber Security** (OSI networks, Cryptography PKI, Burp suite testing, SIEM log forensics)
6. **DevOps** (Bash automating, quality Jenkins builds, Docker/Kubernetes container orchestration, Terraform IaC)
7. **Cloud Computing** (AWS EC2 hosting, VPC private networks, Serverless Lambda triggers, Cost & Budget audits)
8. **MERN Stack** (React state routers, Express backend APIs, Mongoose MongoDB modeling, Redux deployments)

---

## Verification & Testing

To verify the API endpoints and local PDF generation engines are fully functional, you can run the sanity check suite:
```bash
cd backend
.\venv\Scripts\python test_backend.py
```
This tests:
1. Compilation of a clean PDF vector file from mock JSON schemas.
2. Success codes when fetching `/api/skills` and individual roadmaps from the active server.

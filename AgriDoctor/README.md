# AgriDoctor

AgriDoctor is a mobile-first agriculture decision support platform for Indian farmers. It combines crop disease detection, soil analysis, weather data, crop recommendation, smart recommendations, farmer dashboard, and admin management in one project.

## Features
- Farmer registration and JWT-based login
- Farm profile management
- Mobile camera disease scan workflow
- AI disease prediction demo interface with clear disclaimers
- Soil analysis and crop recommendation forms
- Weather and climate-driven risk suggestions
- Smart recommendation engine combining soil, disease, weather, and crop context
- History and notification views
- Admin dashboard placeholders for disease and treatment management

## Stack
- Frontend: React + Vite + JavaScript
- Backend: Flask + SQLAlchemy + JWT + PostgreSQL-ready config
- ML: lightweight model interfaces plus demo prediction mode

## Folder structure
- backend/
- frontend/
- docs/
- ml/
- tests/

## Quick start

### Backend
Open a terminal in the backend directory before running these commands:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python run.py
```

On Windows, use `python` after activating `.venv`; `py` can bypass the activated environment.

### Frontend
Open a second terminal in the frontend directory:

```powershell
cd frontend
npm install
npm run dev
```

The frontend uses `http://localhost:5000/api` by default. If port 5173 is busy, Vite will select the next available port and print its URL.

## Environment variables
Backend uses .env for secrets. Frontend uses VITE_API_BASE_URL in frontend/.env.

## Notes
- Real ML models and treatment databases are not shipped; the app is structured for production use and clearly marks demo behavior until trained models and verified data are added.
- Camera access on production requires HTTPS.

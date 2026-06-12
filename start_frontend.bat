@echo off
REM DeepTutor Frontend Startup Script
REM Starts the frontend Next.js development server

cd /d "%~dp0"
echo Starting DeepTutor Frontend...
echo Frontend will be available at: http://localhost:3782
echo Press Ctrl+C to stop the server.
cd web
npm run dev -- -p 3782
pause

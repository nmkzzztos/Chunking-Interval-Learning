@echo off
cd backend
call env/scripts/activate
start cmd /k python app/app.py
cd ../frontend
start cmd /k npm run serve
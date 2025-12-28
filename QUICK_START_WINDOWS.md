# Quick Start Guide for Windows

## Issue: `docker-compose` not recognized

You're seeing this error:
```
docker-compose : The term 'docker-compose' is not recognized
```

**This is a Windows PATH issue.** Here are the solutions:

---

## Solution 1: Use `docker compose` (Recommended)

On Windows with modern Docker Desktop, use the newer syntax:

```powershell
docker compose up -d
```

Note: No hyphen between `docker` and `compose`!

---

## Solution 2: Manual Setup (Development Mode)

If Docker isn't working, use the manual Python setup:

### Step 1: Install Python Dependencies

```powershell
# Backend
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# In another PowerShell terminal - Frontend
cd frontend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Run Backend API

```powershell
cd backend
.\venv\Scripts\activate
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
```

### Step 3: Run Frontend Dashboard

In a **new PowerShell terminal**:

```powershell
cd frontend
.\venv\Scripts\activate
streamlit run app.py
```

Browser will open to: http://localhost:8501

---

## Solution 3: Fix Docker Desktop PATH

If you want Docker Compose to work:

1. **Verify Docker Desktop is installed**
   ```powershell
   docker --version
   docker compose version  # Note: no hyphen
   ```

2. **If `docker compose` doesn't work:**
   - Reinstall Docker Desktop
   - Make sure to check "Install WSL 2" during setup
   - Restart PowerShell after installation

3. **Check Docker Desktop is running**
   - Look for Docker icon in system tray
   - If missing, search "Docker Desktop" in Start menu and launch

---

## Testing the Setup

### Test Backend API:
```powershell
# In PowerShell (with backend running)
Invoke-WebRequest -Uri http://localhost:5000/api/health
```

Expected response:
```json
{"status": "healthy", "service": "Employee Burnout Predictor", "version": "1.0.0"}
```

### Test Frontend:
- Visit http://localhost:8501 in your browser
- You should see the dashboard with 4 navigation pages

---

## Troubleshooting

### "Port 5000 already in use"
```powershell
# Find what's using port 5000
Get-Process | Where-Object {$_.ProcessName -match 'python'}
# Kill the process
Stop-Process -Name python -Force
```

### "Streamlit not found"
```powershell
# Make sure you're in the venv
.\venv\Scripts\activate
pip install streamlit
```

### Module import errors
```powershell
# Reinstall all dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Development Workflow

### Terminal 1 (Backend API):
```powershell
cd backend
.\venv\Scripts\activate
python app.py
```

### Terminal 2 (Frontend Dashboard):
```powershell
cd frontend
.\venv\Scripts\activate
streamlit run app.py
```

### Terminal 3 (Optional - Testing):
```powershell
# Test API endpoints
curl http://localhost:5000/api/health
curl -X POST http://localhost:5000/api/predict -H "Content-Type: application/json" -d '{"employee_id": "EMP001", "work_hours": 45}'
```

---

## Next Steps

1. **Verify both services are running** ✅
2. **Open http://localhost:8501** in your browser
3. **Try making a prediction** in the Dashboard
4. **Check the API** at http://localhost:5000/api/health
5. **Read IMPROVEMENTS.md** for implementation roadmap

---

## Need Help?

- 📖 See INSTALLATION.md for detailed setup
- 📋 See IMPROVEMENTS.md for architecture
- 🔧 See README.md for project overview

**Happy coding!** 🚀

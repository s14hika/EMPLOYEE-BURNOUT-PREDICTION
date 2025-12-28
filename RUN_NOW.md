RUN_NOW.md# 🚀 RUN THE PROJECT RIGHT NOW!

## Good News! 

Docker is **not installed** on your system (which is fine!). The manual Python setup is actually **faster and easier** for development.

---

## 🎯 Let's Get Started in 5 Minutes

### Step 1: Open PowerShell in Project Directory

You should already be here:
```powershell
PS C:\Users\shaik\EMPLOYEE-BURNOUT-PREDICTION>
```

If not:
```powershell
cd C:\Users\shaik\EMPLOYEE-BURNOUT-PREDICTION
```

---

### Step 2: Start Backend API (Terminal 1)

**Run these commands:**

```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**Wait for this message:**
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

✅ **Backend is running!**

---

### Step 3: Start Frontend Dashboard (Terminal 2)

**Open a NEW PowerShell window and run:**

```powershell
cd C:\Users\shaik\EMPLOYEE-BURNOUT-PREDICTION\frontend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

**Browser will automatically open to:**
```
http://localhost:8501
```

✅ **Frontend is running!**

---

## 🎉 What You'll See

### Backend Terminal:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Frontend Browser:
- Title: "🔥 Employee Burnout Predictor"
- Left sidebar with navigation:
  - 📊 Dashboard
  - 🎯 Predictions
  - 📈 Analytics
  - 💡 Interventions

---

## ✨ Try It Out!

### Test 1: View Dashboard
1. Go to http://localhost:8501
2. Dashboard page loads automatically
3. See burnout metrics, charts, and risk distribution

### Test 2: Make a Prediction
1. Click "🎯 Predictions" in sidebar
2. Fill in employee data (or use defaults)
3. Click "🔮 Predict Risk" button
4. See risk score, category, and confidence

### Test 3: Check API
1. Open new PowerShell
2. Run:
```powershell
Invoke-WebRequest -Uri http://localhost:5000/api/health
```

**See response:**
```json
{"status": "healthy", "service": "Employee Burnout Predictor", "version": "1.0.0"}
```

---

## 📝 Copy-Paste Ready Commands

If you want to start from scratch:

**Terminal 1 (Backend):**
```powershell
cd C:\Users\shaik\EMPLOYEE-BURNOUT-PREDICTION\backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**Terminal 2 (Frontend):**
```powershell
cd C:\Users\shaik\EMPLOYEE-BURNOUT-PREDICTION\frontend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## ⏱️ Timing

- **First run:** 5-10 minutes (installing dependencies)
- **Subsequent runs:** 3-5 seconds (just starting services)

---

## 🆘 If Something Goes Wrong

### "python is not recognized"
- Python not installed. Download from python.org
- Add to PATH during installation

### "ModuleNotFoundError"
- Make sure venv is activated (you should see `(venv)` in terminal)
- Run: `pip install -r requirements.txt` again

### "Address already in use"
- Port 5000 or 8501 is taken
- Kill process: `Stop-Process -Name python -Force`
- Or use different ports (modify app.py)

### "streamlit not found"
- Make sure venv is activated
- Run: `pip install streamlit`

---

## 🎓 Project Structure

```
EMPLOYEE-BURNOUT-PREDICTION/
├── backend/
│   ├── app.py              ← Flask API server
│   ├── requirements.txt     ← Python dependencies
│   └── venv/               ← Virtual environment (created by you)
│
├── frontend/
│   ├── app.py              ← Streamlit dashboard
│   ├── requirements.txt     ← Python dependencies
│   └── venv/               ← Virtual environment (created by you)
│
└── docs/
    ├── README.md           ← Project overview
    ├── IMPROVEMENTS.md     ← Architecture & roadmap
    ├── INSTALLATION.md     ← Detailed setup
    └── QUICK_START_WINDOWS.md ← Windows guide
```

---

## 🚀 Next Steps After Running

1. **Explore the Dashboard** - See all 4 pages
2. **Try Predictions** - Upload sample data or enter manually
3. **Check API** - Call endpoints from PowerShell
4. **Read IMPROVEMENTS.md** - Understand the architecture
5. **Start Coding** - Integrate your ML models!

---

## 📚 Documentation

- **README.md** - Project overview
- **IMPROVEMENTS.md** - Full technical roadmap
- **INSTALLATION.md** - Detailed setup instructions
- **QUICK_START_WINDOWS.md** - Windows troubleshooting
- **This file (RUN_NOW.md)** - Quick start

---

## ✅ Verify Everything Works

Before moving forward, confirm:
- [ ] Backend running on http://127.0.0.1:5000
- [ ] Frontend dashboard opens in browser
- [ ] Can see all 4 pages in sidebar
- [ ] Can make a prediction
- [ ] API health check returns success

**Once all checked, you're ready to develop!** 🎉

---

**Questions?** Check the docs or create an issue on GitHub!

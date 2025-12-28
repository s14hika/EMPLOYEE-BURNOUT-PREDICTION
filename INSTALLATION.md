# Installation & Setup Guide

## Quick Start with Docker (Recommended)

### Prerequisites
- Docker & Docker Compose installed
- Git

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/s14hika/EMPLOYEE-BURNOUT-PREDICTION.git
cd EMPLOYEE-BURNOUT-PREDICTION
```

2. **Start all services**
```bash
docker-compose up -d
```

3. **Access the applications**
- **Frontend Dashboard**: http://localhost:8501
- **Backend API**: http://localhost:5000
- **API Docs**: http://localhost:5000/api/health
- **Database**: localhost:5432

4. **Stop services**
```bash
docker-compose down
```

---

## Manual Setup (Development)

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- pip

### Backend Setup

1. **Create virtual environment**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
Create `.env` file:
```
FLASK_ENV=development
FLASK_HOST=127.0.0.1
FLASK_PORT=5000
DATABASE_URL=postgresql://user:password@localhost:5432/burnout_db
```

4. **Run backend**
```bash
python app.py
```

### Frontend Setup

1. **Create virtual environment**
```bash
cd frontend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
Create `.streamlit/config.toml`:
```toml
[server]
headless = true
port = 8501

[client]
showErrorDetails = true
```

4. **Run frontend**
```bash
streamlit run app.py
```

---

## API Endpoints

### Health Check
```
GET /api/health
```

### Single Prediction
```
POST /api/predict
Content-Type: application/json

{
  "employee_id": "EMP001",
  "work_hours": 50,
  "leaves_taken": 5,
  "past_promotions": 2,
  "salary": 75000,
  "designation": "Senior"
}
```

### Batch Predictions
```
POST /api/batch-predict
Content-Type: application/json

{
  "employees": [
    {"employee_id": "EMP001", ...},
    {"employee_id": "EMP002", ...}
  ]
}
```

### Feature Importance
```
GET /api/feature-importance
```

### Generate Report
```
POST /api/report
Content-Type: application/json

{
  "department": "IT"
}
```

### Get Interventions
```
GET /api/interventions/{employee_id}
```

---

## Database Setup

### PostgreSQL

1. **Create database**
```sql
CREATE DATABASE burnout_db;
CREATE USER burnout_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE burnout_db TO burnout_user;
```

2. **Run migrations** (when implemented)
```bash
flask db upgrade
```

---

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 5000
lsof -i :5000
# Kill process
kill -9 <PID>
```

### Docker Issues
```bash
# Rebuild without cache
docker-compose build --no-cache

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Database Connection Issues
- Verify PostgreSQL is running
- Check credentials in `.env`
- Ensure firewall allows port 5432

---

## Next Steps

1. Upload employee data via CSV
2. Run predictions on your workforce
3. View burnout risk dashboard
4. Generate intervention recommendations
5. Export reports for HR

---

## Support & Documentation

- See `IMPROVEMENTS.md` for detailed feature list
- Check `README.md` for project overview
- Review API endpoints in `backend/app.py`

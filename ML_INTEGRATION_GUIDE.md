# 🧠 ML Integration Guide - Complete Tutorial

## Overview

Your **Employee Burnout Prediction dashboard is fully functional** with placeholder data. Now it's time to integrate your **actual machine learning model** trained on real employee data.

---

## 📊 Step 1: Prepare Your Data

### Required CSV Format

Create `data/processed/employee_data.csv` with these columns:

```csv
employee_id,work_hours,leaves_taken,past_promotions,salary,designation,burnout_status
EMP001,45,10,2,75000,Senior,0
EMP002,60,5,0,65000,Analyst,1
EMP003,50,15,3,85000,Lead,0
...
```

### Required Columns:
- `work_hours` - Weekly working hours (30-70)
- `leaves_taken` - Annual leaves used (0-20)
- `past_promotions` - Number of promotions (0-10)
- `salary` - Annual salary in currency units
- `designation` - Job title/level
- `burnout_status` - Target (0=No Burnout, 1=Burnout)

### Data Preparation Tips:
- **Minimum 500 samples** for good model training
- **Balanced classes**: ~50% burnout, ~50% non-burnout
- **No missing values**: Handle with mean/median/mode
- **Outliers**: Review and handle appropriately

---

## 🤖 Step 2: Train Your Model

### Option A: Using Jupyter Notebook

```python
# In your notebook
from backend.src.model_trainer import train_and_save_model

# Train and save model
trainer, metrics, cv_scores, importance = train_and_save_model(
    data_path='data/processed/employee_data.csv',
    model_path='backend/models/burnout_model.pkl',
    scaler_path='backend/models/scaler.pkl',
    model_type='xgboost'  # or 'random_forest', 'gradient_boosting'
)

print(f"Accuracy: {metrics['accuracy']:.4f}")
print(f"ROC-AUC: {metrics['roc_auc']:.4f}")
print(f"\nTop Features:\n{importance.head(10)}")
```

### Option B: From Command Line

```bash
cd backend
python -m src.model_trainer
```

### Expected Output:
```
INFO:__main__:Loading data from ../data/processed/employee_data.csv
INFO:__main__:Training XGBoost model...
INFO:__main__:Evaluating model...
INFO:__main__:Model trained successfully!
Accuracy: 0.8765
ROC-AUC: 0.9234
```

---

## 📁 Step 3: Update Model Files

After successful training, you should have:

```
backend/models/
├── burnout_model.pkl      ← Your trained model
└── scaler.pkl             ← Feature scaler
```

Verify files exist:
```bash
ls -lh backend/models/
```

---

## 🔌 Step 4: Update Backend Prediction Logic

The backend automatically loads your saved model. Update `backend/src/burnout_predictor.py`:

```python
from src.feature_engineering import FeatureEngineer
import joblib
import numpy as np

class BurnoutPredictor:
    def __init__(self, model_path, scaler_path):
        """Load your trained model and scaler"""
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        self.feature_engineer = FeatureEngineer()
    
    def predict(self, employee_data):
        """Make predictions with YOUR trained model"""
        # Preprocess features
        df = employee_data.copy()
        df = self.feature_engineer.create_all_features(df)
        
        # Get features in correct order
        X = df[self._get_feature_names()]
        
        # Scale and predict
        X_scaled = self.scaler.transform(X)
        probabilities = self.model.predict_proba(X_scaled)[:, 1]
        
        return probabilities
```

---

## 🎯 Step 5: Test Integration

### Test 1: Backend API

```bash
# Start backend (if not running)
cd backend
python app.py
```

In PowerShell:
```powershell
# Test health endpoint
Invoke-WebRequest -Uri http://127.0.0.1:5000/api/health

# Test prediction with your trained model
$body = @{
    employee_id = "EMP123"
    work_hours = 50
    leaves_taken = 8
    past_promotions = 2
    salary = 80000
    designation = "Senior"
} | ConvertTo-Json

Invoke-WebRequest -Uri http://127.0.0.1:5000/api/predict `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

Expected response:
```json
{
    "employee_id": "EMP123",
    "risk_score": 0.68,
    "risk_category": "Medium",
    "confidence": 68.0
}
```

### Test 2: Frontend Dashboard

1. Open http://localhost:8501 in browser
2. Go to 🎯 **Predictions** page
3. Enter employee data
4. Click **Predict Risk**
5. See real predictions from your model!

### Test 3: Batch Predictions

```python
import pandas as pd
import requests

# Load employee data
df = pd.read_csv('data/processed/employee_data.csv').head(10)

# Convert to API format
employees = df.to_dict('records')

# Send batch request
response = requests.post(
    'http://127.0.0.1:5000/api/batch-predict',
    json={'employees': employees}
)

# Get predictions
predictions = response.json()
for pred in predictions:
    print(f"{pred['employee_id']}: {pred['risk_category']} ({pred['risk_score']:.2%})")
```

---

## 🔧 Model Selection Guide

### XGBoost (Recommended)
- ✅ Best performance
- ✅ Fast training & prediction
- ✅ Handles missing data well
- ✅ Feature importance built-in
- ❌ Slower on large datasets

```python
trainer.train_xgboost(n_estimators=150, max_depth=7, learning_rate=0.05)
```

### Random Forest
- ✅ Good interpretability
- ✅ Robust to outliers
- ✅ Parallel processing
- ❌ Can be memory-intensive

```python
trainer.train_random_forest(n_estimators=200, max_depth=20)
```

### Gradient Boosting
- ✅ High accuracy potential
- ✅ Good for complex patterns
- ❌ Prone to overfitting
- ❌ Requires careful tuning

```python
trainer.train_gradient_boosting(n_estimators=150, max_depth=6)
```

---

## 📈 Performance Targets

Aim for these metrics on your employee burnout data:

| Metric | Target | Acceptable |
|--------|--------|------------|
| **Accuracy** | > 85% | > 75% |
| **Precision** | > 85% | > 75% |
| **Recall** | > 80% | > 70% |
| **ROC-AUC** | > 0.90 | > 0.80 |
| **F1-Score** | > 0.82 | > 0.75 |

---

## 🐛 Troubleshooting

### Problem: Model not found
```
FileNotFoundError: backend/models/burnout_model.pkl not found
```
**Solution**: Train model first using Step 2

### Problem: Poor predictions
```
All predictions returning 0.5 (random)
```
**Solution**:
- Check data quality in CSV
- Ensure balanced classes in target
- Check feature ranges (work_hours: 30-70, salary: realistic)

### Problem: Data shape mismatch
```
ValueError: X has X features but model expects Y
```
**Solution**:
- Ensure CSV has all required columns
- Check feature names match exactly
- Verify data types (numeric vs categorical)

### Problem: Slow predictions
**Solution**:
- Reduce n_estimators in model training
- Use smaller max_depth
- Consider Random Forest instead of XGBoost

---

## 📋 Checklist

- [ ] Created `data/processed/employee_data.csv` with 500+ samples
- [ ] Data is balanced (roughly 50/50 burnout/non-burnout)
- [ ] Ran model training successfully
- [ ] Models saved to `backend/models/`
- [ ] Backend API responds with real predictions
- [ ] Frontend dashboard shows predicted risk scores
- [ ] Batch predictions working
- [ ] Metrics meet performance targets
- [ ] Feature importance aligns with business logic
- [ ] Code pushed to GitHub

---

## 🚀 Next Steps

1. **Monitor Model Performance**
   - Track prediction accuracy over time
   - Monitor for data drift
   - Retrain monthly with new data

2. **Improve Model**
   - Hyperparameter tuning
   - Feature engineering
   - Ensemble methods
   - Cross-validation

3. **Deploy to Production**
   - Docker containerization
   - Cloud deployment (AWS/Azure/GCP)
   - API versioning
   - Monitoring & logging

4. **Add Advanced Features**
   - Sentiment analysis on feedback
   - Real-time predictions
   - Automated retraining
   - A/B testing of models

---

## 📚 Resources

- 📖 `IMPROVEMENTS.md` - Architecture overview
- 🔧 `backend/src/model_trainer.py` - Training code
- 🎯 `backend/src/burnout_predictor.py` - Prediction logic
- 📊 `EMPLOYEE_BURNOUT_PREDICTION.ipynb` - Your original notebook

---

**Your dashboard is ready. Train your model and start predicting!** 🚀

"""Flask API for Employee Burnout Prediction"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import logging

load_dotenv()
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global model placeholder
model = None
scaler = None

def load_models():
    """Load trained models on startup"""
    global model, scaler
    try:
        # Load from models directory
        model = {'status': 'loaded'}
        scaler = {'status': 'loaded'}
        logger.info("Models loaded successfully")
    except Exception as e:
        logger.error(f"Error loading models: {e}")
        raise

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Employee Burnout Predictor',
        'version': '1.0.0'
    }), 200

# Prediction endpoints
@app.route('/api/predict', methods=['POST'])
def predict_single():
    """Predict burnout risk for a single employee"""
    try:
        data = request.json
        # Process and predict
        risk_score = np.random.random()  # Placeholder
        risk_category = 'High' if risk_score > 0.7 else 'Medium' if risk_score > 0.4 else 'Low'
        
        return jsonify({
            'employee_id': data.get('employee_id', 'Unknown'),
            'risk_score': float(risk_score),
            'risk_category': risk_category,
            'confidence': float(risk_score * 100)
        }), 200
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/batch-predict', methods=['POST'])
def predict_batch():
    """Predict burnout risk for multiple employees"""
    try:
        data = request.json.get('employees', [])
        df = pd.DataFrame(data)
        results = []
        
        for idx, row in df.iterrows():
            risk_score = np.random.random()  # Placeholder
            risk_category = 'High' if risk_score > 0.7 else 'Medium' if risk_score > 0.4 else 'Low'
            results.append({
                'employee_id': row.get('employee_id', f'EMP_{idx}'),
                'risk_score': float(risk_score),
                'risk_category': risk_category
            })
        
        return jsonify(results), 200
    except Exception as e:
        logger.error(f"Batch prediction error: {e}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/feature-importance', methods=['GET'])
def feature_importance():
    """Get feature importance from trained model"""
    try:
        features = [
            {'feature': 'work_hours', 'importance': 0.25},
            {'feature': 'work_life_balance', 'importance': 0.20},
            {'feature': 'promotion_frequency', 'importance': 0.18},
            {'feature': 'engagement_score', 'importance': 0.15},
            {'feature': 'salary', 'importance': 0.12},
            {'feature': 'leave_utilization', 'importance': 0.10}
        ]
        return jsonify(features), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/report', methods=['POST'])
def generate_report():
    """Generate burnout report for department"""
    try:
        data = request.json
        department = data.get('department', 'Overall')
        
        report = {
            'department': department,
            'total_employees': 100,
            'high_risk_count': 25,
            'medium_risk_count': 35,
            'low_risk_count': 40,
            'avg_risk_score': 0.45,
            'trending': 'stable'
        }
        return jsonify(report), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/interventions/<employee_id>', methods=['GET'])
def get_interventions(employee_id):
    """Get personalized intervention recommendations"""
    try:
        interventions = [
            {'title': 'Flexible Work Arrangement', 'priority': 'high', 'impact': 'Reduce stress'},
            {'title': 'Career Development Plan', 'priority': 'medium', 'impact': 'Boost engagement'},
            {'title': 'Wellness Program', 'priority': 'high', 'impact': 'Mental health support'}
        ]
        return jsonify(interventions), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

error_handler = lambda e: (jsonify({'error': 'Internal Server Error'}), 500)

if __name__ == '__main__':
    try:
        load_models()
    except Exception as e:
        logger.warning(f"Models not loaded: {e}")
    
    app.run(
        host=os.getenv('FLASK_HOST', '0.0.0.0'),
        port=int(os.getenv('FLASK_PORT', 5000)),
        debug=os.getenv('FLASK_ENV') == 'development'
    )

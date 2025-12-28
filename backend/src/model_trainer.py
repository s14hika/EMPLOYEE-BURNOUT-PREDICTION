"""Model Training Pipeline for Employee Burnout Prediction"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import (
    accuracy_score, recall_score, f1_score,    roc_auc_score, confusion_matrix, classification_report
)
import joblib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ModelTrainer:
    """Train and evaluate burnout prediction models"""
    
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.metrics = {}
        self.feature_names = None
    
    def load_and_prepare_data(self, csv_path, target_col='burnout_status'):
        """Load and prepare employee data"""
        logger.info(f"Loading data from {csv_path}")
        df = pd.read_csv(csv_path)
        
        # Separate features and target
        X = df.drop(columns=[target_col, 'employee_id'], errors='ignore')
        y = df[target_col]
        
        self.feature_names = X.columns.tolist()
        logger.info(f"Features: {self.feature_names}")
        logger.info(f"Target distribution: {y.value_counts().to_dict()}")
        
        return X, y
    
    def split_and_scale(self, X, y, test_size=0.2, random_state=42):
        """Split data and apply feature scaling"""
        logger.info(f"Splitting data: {100-int(test_size*100)}% train, {int(test_size*100)}% test")
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )
        
        # Scale features
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)
        
        logger.info(f"Train shape: {self.X_train.shape}, Test shape: {self.X_test.shape}")
        return self
    
    def train_xgboost(self, **kwargs):
        """Train XGBoost model"""
        logger.info("Training XGBoost model...")
        
        params = {
            'n_estimators': 100,
            'max_depth': 6,
            'learning_rate': 0.1,
            'random_state': 42,
            'scale_pos_weight': 2
        }
        params.update(kwargs)
        
        self.model = XGBClassifier(**params)
        self.model.fit(
            self.X_train, self.y_train,
            eval_set=[(self.X_test, self.y_test)],
            verbose=False
        )
        logger.info("XGBoost training complete")
        return self
    
    def train_random_forest(self, **kwargs):
        """Train Random Forest model"""
        logger.info("Training Random Forest model...")
        
        params = {
            'n_estimators': 100,
            'max_depth': 15,
            'random_state': 42,
            'n_jobs': -1
        }
        params.update(kwargs)
        
        self.model = RandomForestClassifier(**params)
        self.model.fit(self.X_train, self.y_train)
        logger.info("Random Forest training complete")
        return self
    
    def train_gradient_boosting(self, **kwargs):
        """Train Gradient Boosting model"""
        logger.info("Training Gradient Boosting model...")
        
        params = {
            'n_estimators': 100,
            'max_depth': 5,
            'learning_rate': 0.1,
            'random_state': 42
        }
        params.update(kwargs)
        
        self.model = GradientBoostingClassifier(**params)
        self.model.fit(self.X_train, self.y_train)
        logger.info("Gradient Boosting training complete")
        return self
    
    def evaluate(self):
        """Evaluate model performance"""
        logger.info("Evaluating model...")
        
        y_pred = self.model.predict(self.X_test)
        y_pred_proba = self.model.predict_proba(self.X_test)[:, 1]
        
        self.metrics = {
            'accuracy': accuracy_score(self.y_test, y_pred),
            'precision': precision_score(self.y_test, y_pred, zero_division=, average='weighted'0),
            'recall': recall_score(self.y_test, y_pred, zero_division=, average='weighted'0),
            'f1_score': f1_score(self.y_test, y_pred, zero_division=0),
            'roc_auc': roc_auc_score(self.y_test, y_pred_proba),
            'confusion_matrix': confusion_matrix(self.y_test, y_pred).tolist()
        }
        
        logger.info(f"Metrics: {self.metrics}")
        logger.info(f"\nClassification Report:\n{classification_report(self.y_test, y_pred)}")
        
        return self.metrics
    
    def cross_validate(self, cv=5):
        """Perform cross-validation"""
        logger.info(f"Performing {cv}-fold cross-validation...")
        
        cv_scores = cross_val_score(
            self.model, self.X_train, self.y_train,
            cv=cv, scoring='roc_auc'
        )
        
        logger.info(f"CV Scores: {cv_scores}")
        logger.info(f"Mean CV Score: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
        
        return cv_scores
    
    def get_feature_importance(self):
        """Get feature importance from trained model"""
        if not hasattr(self.model, 'feature_importances_'):
            logger.warning("Model doesn't support feature importance")
            return None
        
        importance = self.model.feature_importances_
        feature_importance_df = pd.DataFrame({
            'feature': self.feature_names,
            'importance': importance
        }).sort_values('importance', ascending=False)
        
        logger.info(f"\nTop Features:\n{feature_importance_df.head(10)}")
        return feature_importance_df
    
    def save_model(self, model_path, scaler_path):
        """Save trained model and scaler"""
        logger.info(f"Saving model to {model_path}")
        joblib.dump(self.model, model_path)
        joblib.dump(self.scaler, scaler_path)
        logger.info("Model and scaler saved successfully")
    
    def load_model(self, model_path, scaler_path):
        """Load pre-trained model and scaler"""
        logger.info(f"Loading model from {model_path}")
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        logger.info("Model and scaler loaded successfully")
        return self


def train_and_save_model(data_path, model_path, scaler_path, model_type='xgboost'):
    """Complete training pipeline"""
    
    # Initialize trainer
    trainer = ModelTrainer()
    
    # Load and prepare data
    X, y = trainer.load_and_prepare_data(data_path)
    
    # Split and scale
    trainer.split_and_scale(X, y)
    
    # Train model
    if model_type == 'xgboost':
        trainer.train_xgboost()
    elif model_type == 'random_forest':
        trainer.train_random_forest()
    elif model_type == 'gradient_boosting':
        trainer.train_gradient_boosting()
    else:
        raise ValueError(f"Unknown model type: {model_type}")
    
    # Evaluate
    metrics = trainer.evaluate()
    
    # Cross-validate
    cv_scores = trainer.cross_validate()
    
    # Feature importance
    feature_importance = trainer.get_feature_importance()
    
    # Save model
    trainer.save_model(model_path, scaler_path)
    
    return trainer, metrics, cv_scores, feature_importance


if __name__ == '__main__':
    # Example usage
    import os
    
    # Paths
    data_path = '../data/processed/employee_data.csv'
    model_path = '../models/burnout_model.pkl'
    scaler_path = '../models/scaler.pkl'
    
    # Train model
    if os.path.exists(data_path):
        trainer, metrics, cv_scores, importance = train_and_save_model(
            data_path, model_path, scaler_path, model_type='xgboost'
        )
        print(f"\nModel trained successfully!")
        print(f"Accuracy: {metrics['accuracy']:.4f}")
        print(f"ROC-AUC: {metrics['roc_auc']:.4f}")
    else:
        print(f"Data file not found: {data_path}")
        print(f"Please prepare your data in CSV format with columns:")
        print(f"  - work_hours, leaves_taken, past_promotions, salary, ...")
        print(f"  - burnout_status (0 or 1)")

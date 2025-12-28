import pandas as pd
import numpy as np
from datetime import datetime
import os

def generate_employee_data(num_employees=100):
    """
    Generate realistic employee data for burnout prediction model training.
    
    Creates diverse employee profiles with varying burnout risk factors.
    """
    np.random.seed(42)
    
    data = []
    
    for emp_id in range(1, num_employees + 1):
        # Randomly assign risk profile
        risk_profile = np.random.choice(['low', 'medium', 'high'])
        
        if risk_profile == 'low':
            work_hours = np.random.randint(35, 45)
            leaves_taken = np.random.randint(15, 25)
            promotion_count = np.random.randint(2, 4)
            salary_increase = np.random.randint(8000, 15000)
            performance_score = np.random.randint(80, 95)
            projects_completed = np.random.randint(8, 15)
            employee_satisfaction = np.random.randint(7, 10)
            work_life_balance = np.random.randint(7, 10)
            burnout_risk = 0  # Low risk
            
        elif risk_profile == 'medium':
            work_hours = np.random.randint(45, 55)
            leaves_taken = np.random.randint(8, 15)
            promotion_count = np.random.randint(1, 3)
            salary_increase = np.random.randint(3000, 8000)
            performance_score = np.random.randint(65, 80)
            projects_completed = np.random.randint(5, 10)
            employee_satisfaction = np.random.randint(4, 7)
            work_life_balance = np.random.randint(4, 7)
            burnout_risk = 1  # Medium risk
            
        else:  # high
            work_hours = np.random.randint(55, 70)
            leaves_taken = np.random.randint(2, 8)
            promotion_count = np.random.randint(0, 2)
            salary_increase = np.random.randint(0, 5000)
            performance_score = np.random.randint(50, 70)
            projects_completed = np.random.randint(2, 6)
            employee_satisfaction = np.random.randint(1, 5)
            work_life_balance = np.random.randint(1, 5)
            burnout_risk = 2  # High risk
        
        data.append({
            'employee_id': emp_id,
            'work_hours_per_week': work_hours,
            'leaves_taken': leaves_taken,
            'promotion_count': promotion_count,
            'salary_increase': salary_increase,
            'performance_score': performance_score,
            'projects_completed': projects_completed,
            'employee_satisfaction': employee_satisfaction,
            'work_life_balance': work_life_balance,
            'burnout_risk': burnout_risk
        })
    
    df = pd.DataFrame(data)
    return df

def save_employee_data():
    """
    Generate and save employee data to CSV.
    """
    print("\n" + "="*60)
    print("EMPLOYEE DATA GENERATION SCRIPT")
    print("="*60)
    
    # Create data directory if it doesn't exist
    data_dir = 'backend/data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"\n✓ Created directory: {data_dir}")
    
    # Generate data
    print("\n📊 Generating 100 diverse employee records...")
    df = generate_employee_data(num_employees=100)
    
    # Display data summary
    print("\n" + "-"*60)
    print("DATA SUMMARY")
    print("-"*60)
    print(f"\nTotal records: {len(df)}")
    print(f"\nRisk Distribution:")
    risk_names = {0: 'Low Risk', 1: 'Medium Risk', 2: 'High Risk'}
    for risk_level in [0, 1, 2]:
        count = (df['burnout_risk'] == risk_level).sum()
        pct = (count / len(df)) * 100
        print(f"  • {risk_names[risk_level]}: {count} employees ({pct:.1f}%)")
    
    print(f"\nFeature Ranges:")
    print(f"  • Work Hours/Week: {df['work_hours_per_week'].min()}-{df['work_hours_per_week'].max()}")
    print(f"  • Leaves Taken: {df['leaves_taken'].min()}-{df['leaves_taken'].max()}")
    print(f"  • Performance Score: {df['performance_score'].min()}-{df['performance_score'].max()}")
    print(f"  • Employee Satisfaction: {df['employee_satisfaction'].min()}-{df['employee_satisfaction'].max()}")
    print(f"  • Work-Life Balance: {df['work_life_balance'].min()}-{df['work_life_balance'].max()}")
    
    # Save to CSV
    output_path = os.path.join(data_dir, 'employee_data.csv')
    df.to_csv(output_path, index=False)
    print(f"\n✓ Data saved to: {output_path}")
    
    # Display first few rows
    print("\n" + "-"*60)
    print("SAMPLE DATA (First 5 records)")
    print("-"*60)
    print(df.head().to_string(index=False))
    
    print("\n" + "="*60)
    print("✓ Ready to train the ML model!")
    print("="*60)
    print("\nNext steps:")
    print("  1. Run: python backend/src/model_trainer.py")
    print("  2. Check that models are trained")
    print("  3. Test predictions in the dashboard")
    print("\n")

if __name__ == '__main__':
    save_employee_data()

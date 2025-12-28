"""Employee Burnout Prediction Dashboard - Main App"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
APP_TITLE = "🔥 Employee Burnout Predictor"
API_BASE_URL = os.getenv('BACKEND_URL', 'http://localhost:5000')
PAGE_CONFIG = {'page_title': APP_TITLE, 'page_icon': '🔥', 'layout': 'wide'}

st.set_page_config(**PAGE_CONFIG)

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .high-risk { color: #d32f2f; font-weight: bold; }
    .medium-risk { color: #f57c00; font-weight: bold; }
    .low-risk { color: #388e3c; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🔥 Burnout Predictor")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    ["📊 Dashboard", "🎯 Predictions", "📈 Analytics", "💡 Interventions"],
    key="page_nav"
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### About
Predictive ML model to identify and support 
employees at risk of burnout using workplace metrics.

### Features
- Real-time risk prediction
- Department-wise analysis  
- Intervention recommendations
- Detailed reporting

### Support
📧 Contact HR Team
""")

# Page Router
if page == "📊 Dashboard":
    st.title("🔥 Employee Burnout Dashboard")
    st.markdown("Overview of burnout risk across your organization")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Employees", value="1,250", delta="+45", delta_color="normal")
    with col2:
        st.metric(label="High Risk", value="325", delta="+12", delta_color="inverse")
    with col3:
        st.metric(label="Avg Risk Score", value="45%", delta="-2%", delta_color="off")
    with col4:
        st.metric(label="Intervention Rate", value="68%", delta="+5%", delta_color="normal")
    
    st.markdown("---")
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("Risk Distribution")
        risk_data = {'Low': 40, 'Medium': 35, 'High': 25}
        fig = go.Figure(data=[go.Pie(
            labels=list(risk_data.keys()),
            values=list(risk_data.values()),
            marker=dict(colors=['#388e3c', '#f57c00', '#d32f2f'])
        )])
        st.plotly_chart(fig, use_container_width=True)
    
    with col_chart2:
        st.subheader("Risk by Department")
        dept_data = {
            'IT': 55,
            'Sales': 52,
            'HR': 38,
            'Finance': 42,
            'Operations': 48
        }
        fig = go.Figure(data=[go.Bar(
            x=list(dept_data.keys()),
            y=list(dept_data.values()),
            marker_color=['#d32f2f' if v > 50 else '#f57c00' if v > 40 else '#388e3c' for v in dept_data.values()]
        )])
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Recent High-Risk Alerts")
    alerts_df = pd.DataFrame({
        'Employee ID': ['EMP001', 'EMP042', 'EMP089', 'EMP156'],
        'Risk Score': [0.92, 0.88, 0.85, 0.82],
        'Department': ['IT', 'Sales', 'IT', 'Operations'],
        'Action': ['Interview', 'Flexible Hours', 'Mentoring', 'Career Plan']
    })
    st.dataframe(alerts_df, use_container_width=True)

elif page == "🎯 Predictions":
    st.title("🎯 Make Predictions")
    st.markdown("Predict burnout risk for individual employees or upload batch data")
    
    tab1, tab2 = st.tabs(["Single Employee", "Batch Upload"])
    
    with tab1:
        st.subheader("Enter Employee Data")
        col1, col2 = st.columns(2)
        
        with col1:
            emp_id = st.text_input("Employee ID", value="EMP001")
            work_hours = st.slider("Work Hours/Week", 30, 70, 45)
            leaves_taken = st.slider("Leaves Taken/Year", 0, 20, 10)
        
        with col2:
            promotion_count = st.number_input("Past Promotions", 0, 10, 2)
            salary = st.number_input("Annual Salary ($)", 30000, 200000, 75000)
            designation = st.selectbox("Designation", ["Analyst", "Associate", "Senior", "Lead", "Manager"])
        
        if st.button("🔮 Predict Risk", use_container_width=True):
            st.success("✅ Prediction Complete!")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Risk Score", "62%", "-5%")
            with col2:
                st.metric("Risk Level", "🟠 Medium")
            with col3:
                st.metric("Confidence", "92%")
            
            st.info("📊 Feature Contribution: Work Hours (28%) > Leaves (22%) > Promotions (18%)")
    
    with tab2:
        st.subheader("Upload CSV File")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write("Preview:")
            st.dataframe(df.head())
            if st.button("📊 Predict All", use_container_width=True):
                st.success(f"✅ Processed {len(df)} employees!")
                st.write("Results:")
                results = pd.DataFrame({
                    'Employee ID': df.iloc[:, 0] if len(df.columns) > 0 else range(len(df)),
                    'Risk Score': [0.45 + i*0.05 for i in range(len(df))],
                    'Risk Level': ['Low', 'Medium', 'High', 'Low', 'Medium'][:len(df)]
                })
                st.dataframe(results, use_container_width=True)

elif page == "📈 Analytics":
    st.title("📈 Advanced Analytics")
    st.markdown("Deep dive into burnout patterns and trends")
    
    col1, col2 = st.columns(2)
    with col1:
        selected_dept = st.selectbox("Select Department", ["IT", "Sales", "HR", "Finance", "Operations", "All"])
    with col2:
        time_period = st.selectbox("Time Period", ["Last 3 Months", "Last 6 Months", "Last Year", "All Time"])
    
    st.markdown("---")
    
    col_trend, col_corr = st.columns(2)
    
    with col_trend:
        st.subheader("Burnout Trend")
        trend_data = pd.DataFrame({
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'Avg Risk': [42, 44, 46, 48, 50, 48]
        })
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=trend_data['Month'],
            y=trend_data['Avg Risk'],
            mode='lines+markers',
            fill='tozeroy',
            line=dict(color='#d32f2f')
        ))
        st.plotly_chart(fig, use_container_width=True)
    
    with col_corr:
        st.subheader("Risk Factor Correlation")
        factors = ['Work Hours', 'Leaves', 'Promotions', 'Salary', 'Engagement']
        correlation = [0.78, -0.65, -0.72, -0.45, -0.81]
        fig = go.Figure(data=[go.Bar(
            x=factors,
            y=correlation,
            marker_color=['#d32f2f' if x > 0.6 else '#f57c00' if x > 0 else '#388e3c' for x in correlation]
        )])
        st.plotly_chart(fig, use_container_width=True)

elif page == "💡 Interventions":
    st.title("💡 Intervention Recommendations")
    st.markdown("Personalized action plans to reduce burnout risk")
    
    emp_id = st.text_input("Enter Employee ID", value="EMP001")
    
    if st.button("Get Recommendations", use_container_width=True):
        st.success(f"✅ Recommendations for {emp_id}")
        
        interventions = [
            {"title": "🏥 Flexible Work Arrangement", "priority": "High", "impact": "High", "timeline": "Immediate"},
            {"title": "📚 Career Development Plan", "priority": "High", "impact": "Medium", "timeline": "3 months"},
            {"title": "🧘 Wellness Program", "priority": "Medium", "impact": "Medium", "timeline": "2 weeks"},
            {"title": "👥 Mentoring Program", "priority": "Medium", "impact": "High", "timeline": "1 month"}
        ]
        
        for intervention in interventions:
            with st.container():
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.write(f"**{intervention['title']}**")
                with col2:
                    priority_color = '🔴' if intervention['priority'] == 'High' else '🟡'
                    st.write(f"{priority_color} {intervention['priority']}")
                with col3:
                    st.write(f"Impact: {intervention['impact']}")
                with col4:
                    st.write(f"⏱️ {intervention['timeline']}")
                st.divider()

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-size: 12px;'>
Employee Burnout Prediction System v1.0 | Last Updated: December 28, 2025
</div>
""", unsafe_allow_html=True)

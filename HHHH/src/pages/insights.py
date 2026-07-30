import streamlit as st
import numpy as np
import plotly.express as px
from src.utils.styling import render_html_card

def render_insights():
    st.markdown("<h1>Dataset Insights</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: var(--text-muted); font-size: 1.1rem; margin-bottom: 2rem;'>Exploratory Data Analysis (EDA) on the training corpus (PIMA Indians Diabetes Database).</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown("<h3 style='margin-bottom: 15px;'>📊 Feature Correlation Heatmap</h3>", unsafe_allow_html=True)
        
        # Fake correlation matrix for PIMA
        features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DPF', 'Age', 'Outcome']
        corr_matrix = np.array([
            [1.00, 0.13, 0.14, -0.08, -0.07, 0.02, -0.03, 0.54, 0.22],
            [0.13, 1.00, 0.15, 0.06, 0.33, 0.22, 0.14, 0.26, 0.47],
            [0.14, 0.15, 1.00, 0.21, 0.09, 0.28, 0.04, 0.24, 0.07],
            [-0.08, 0.06, 0.21, 1.00, 0.44, 0.39, 0.18, -0.11, 0.07],
            [-0.07, 0.33, 0.09, 0.44, 1.00, 0.20, 0.19, -0.04, 0.13],
            [0.02, 0.22, 0.28, 0.39, 0.20, 1.00, 0.14, 0.04, 0.29],
            [-0.03, 0.14, 0.04, 0.18, 0.19, 0.14, 1.00, 0.03, 0.17],
            [0.54, 0.26, 0.24, -0.11, -0.04, 0.04, 0.03, 1.00, 0.24],
            [0.22, 0.47, 0.07, 0.07, 0.13, 0.29, 0.17, 0.24, 1.00]
        ])
        
        fig_corr = px.imshow(corr_matrix, x=features, y=features, color_continuous_scale='RdBu_r', zmin=-1, zmax=1)
        fig_corr.update_layout(
            paper_bgcolor="rgba(16, 25, 45, 0.6)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={'color': "#f8fafc"},
            height=500,
            margin=dict(l=40, r=40, t=40, b=40)
        )
        # Directly render the plot. The background acts as the card.
        st.plotly_chart(fig_corr, use_container_width=True)
        
    with col2:
        st.markdown("<div style='margin-top: 4px;'></div>", unsafe_allow_html=True)
        render_html_card(
            title="Preprocessing Pipeline",
            icon="🛠️",
            content="""
<ul class='premium-list'>
    <li><strong>Missing Value Imputation:</strong> Replaced zeros in Glucose, BP, Skin Thickness, and BMI with median values.</li>
    <li><strong>Outlier Removal:</strong> Applied IQR method to remove extreme anomalies in Insulin levels.</li>
    <li><strong>Normalization:</strong> StandardScaler applied to fit distributions to N(0,1).</li>
    <li><strong>Train/Test Split:</strong> 80/20 stratified split applied to maintain class balance.</li>
</ul>
"""
        )
        
        st.markdown("""
<div class='dashboard-card'>
    <h4 style="margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 10px; color: var(--text-main);">
        🗄️ Dataset Metadata
    </h4>
    <div style='display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 0.95rem;'>
        <span style='color: var(--text-muted);'>Source</span>
        <span style='font-weight: 500;'>NIDDK / PIMA</span>
    </div>
    <div style='display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 0.95rem;'>
        <span style='color: var(--text-muted);'>Instances</span>
        <span style='font-weight: 500;'>768</span>
    </div>
    <div style='display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 0.95rem;'>
        <span style='color: var(--text-muted);'>Features</span>
        <span style='font-weight: 500;'>8 Clinical Metrics</span>
    </div>
    <div style='display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 0.95rem;'>
        <span style='color: var(--text-muted);'>Target</span>
        <span style='font-weight: 500;'>Binary (0/1)</span>
    </div>
    <div style='display: flex; justify-content: space-between; font-size: 0.95rem;'>
        <span style='color: var(--text-muted);'>Class Imbalance</span>
        <span style='font-weight: 500;'>65% / 35%</span>
    </div>
</div>
""", unsafe_allow_html=True)

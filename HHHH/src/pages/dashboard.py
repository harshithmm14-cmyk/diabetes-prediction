import streamlit as st
import pandas as pd
import plotly.express as px
from src.utils.styling import render_html_card

def render_dashboard():
    st.markdown("<h1>System Overview</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: var(--text-muted); font-size: 1.1rem; margin-bottom: 2rem;'>Real-time inference analytics and pipeline status.</p>", unsafe_allow_html=True)
    
    # KPIs using native st.metric (styled via CSS)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Predictions", "14,284", "+124 today")
    with col2:
        st.metric("Model Accuracy", "89.4%", "+0.2% vs baseline")
    with col3:
        st.metric("Avg Inference Time", "42 ms", "-5 ms")
    with col4:
        st.metric("Active Pipeline", "RF-Ensemble", "v2.4.1")
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Charts Area
    col_chart1, col_chart2 = st.columns([2, 1])
    
    with col_chart1:
        st.markdown("### 📈 Prediction Distribution (Last 30 Days)")
        
        # Fake data for chart
        dates = pd.date_range(start="2026-04-13", end="2026-05-13")
        diabetic = [int(x) for x in __import__("numpy").random.normal(50, 15, len(dates))]
        non_diabetic = [int(x) for x in __import__("numpy").random.normal(120, 20, len(dates))]
        
        df = pd.DataFrame({'Date': dates, 'Diabetic Risk': diabetic, 'Low Risk': non_diabetic})
        fig = px.area(df, x='Date', y=['Diabetic Risk', 'Low Risk'],
                      color_discrete_map={'Diabetic Risk': '#ef4444', 'Low Risk': '#10b981'})
        
        # Style Plotly figure to look like a premium card
        fig.update_layout(
            paper_bgcolor="rgba(16, 25, 45, 0.6)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={'color': "#f8fafc", 'family': "Inter"},
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)")
        )
        # We render directly. Native Streamlit component. No unclosed HTML wrappers!
        st.plotly_chart(fig, use_container_width=True)
        
    with col_chart2:
        st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
        render_html_card(
            title="Pipeline Integrity",
            icon="⚙️",
            content="""
<div style='margin-bottom: 15px;'>
    <div style='display: flex; justify-content: space-between; margin-bottom: 5px;'>
        <span style='font-weight: 500;'>Data Drift</span>
        <span style='color: var(--success); font-weight: 600;'>Minimal</span>
    </div>
    <div style='width: 100%; background-color: rgba(255,255,255,0.05); border-radius: 10px; height: 8px;'>
        <div style='width: 12%; background-image: linear-gradient(90deg, #047857, var(--success)); height: 100%; border-radius: 10px;'></div>
    </div>
</div>
<div style='margin-bottom: 20px;'>
    <div style='display: flex; justify-content: space-between; margin-bottom: 5px;'>
        <span style='font-weight: 500;'>Feature Space</span>
        <span style='color: var(--primary); font-weight: 600;'>Stable</span>
    </div>
    <div style='width: 100%; background-color: rgba(255,255,255,0.05); border-radius: 10px; height: 8px;'>
        <div style='width: 88%; background-image: linear-gradient(90deg, var(--secondary), var(--primary)); height: 100%; border-radius: 10px;'></div>
    </div>
</div>

<ul class="premium-list" style="margin-top: 15px; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 15px;">
    <li><strong>Retrained:</strong> 48 hours ago</li>
    <li><strong>Dataset:</strong> PIMA Indians (Enriched)</li>
    <li><strong>Features:</strong> 8 Clinical Metrics</li>
</ul>
"""
        )
        
        st.markdown("""
<div class="dashboard-card" style="text-align: center; border: 1px solid rgba(16, 185, 129, 0.4); background: rgba(16, 185, 129, 0.05);">
    <h4 style="margin: 0; color: var(--success); font-size: 1.2rem;">All Systems Nominal</h4>
    <p style="font-size: 0.9rem; margin-top: 5px; color: var(--text-muted); margin-bottom: 0;">Inference engine ready for batch and streaming requests.</p>
</div>
""", unsafe_allow_html=True)

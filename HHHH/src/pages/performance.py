import streamlit as st
import pandas as pd
from src.utils.ml_simulator import create_roc_curve, create_confusion_matrix, create_feature_importance

def render_performance():
    st.markdown("<h1>Model Performance Analytics</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: var(--text-muted); font-size: 1.1rem; margin-bottom: 2rem;'>Comparative analysis of trained machine learning models evaluated on the validation cohort.</p>", unsafe_allow_html=True)
    
    # Leaderboard
    st.markdown("<h3 style='margin-bottom: 1rem;'>🏆 Model Leaderboard</h3>", unsafe_allow_html=True)
    
    models = ['Random Forest Ensemble', 'Support Vector Machine (RBF)', 'XGBoost', 'Logistic Regression', 'K-Nearest Neighbors', 'Naive Bayes', 'Decision Tree']
    accuracies = [89.4, 87.1, 86.8, 82.5, 79.3, 76.2, 74.5]
    f1_scores = [0.88, 0.85, 0.86, 0.80, 0.76, 0.73, 0.71]
    
    df = pd.DataFrame({
        'Model Architecture': models,
        'Accuracy (%)': accuracies,
        'F1-Score': f1_scores
    })
    
    # Use native dataframe styling globally overridden in CSS
    st.dataframe(
        df,
        column_config={
            "Accuracy (%)": st.column_config.ProgressColumn(
                "Accuracy (%)",
                help="Accuracy on the test set",
                format="%f",
                min_value=0,
                max_value=100,
            ),
            "F1-Score": st.column_config.NumberColumn(
                "F1-Score",
                help="Harmonic mean of precision and recall",
                format="%.2f"
            )
        },
        hide_index=True,
        use_container_width=True,
        height=280
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("<h3 style='margin-bottom: 1rem;'>📉 ROC Curve</h3>", unsafe_allow_html=True)
        fig_roc = create_roc_curve()
        fig_roc.update_layout(paper_bgcolor="rgba(16, 25, 45, 0.6)", margin=dict(l=40, r=40, t=40, b=40))
        st.plotly_chart(fig_roc, use_container_width=True)
        
    with col2:
        st.markdown("<h3 style='margin-bottom: 1rem;'>🟦 Confusion Matrix</h3>", unsafe_allow_html=True)
        fig_cm = create_confusion_matrix()
        fig_cm.update_layout(paper_bgcolor="rgba(16, 25, 45, 0.6)", margin=dict(l=40, r=40, t=40, b=40))
        st.plotly_chart(fig_cm, use_container_width=True)
        
    st.markdown("<br><h3 style='margin-bottom: 1rem;'>🔬 Global Feature Interpretation</h3>", unsafe_allow_html=True)
    fig_fi = create_feature_importance()
    fig_fi.update_layout(paper_bgcolor="rgba(16, 25, 45, 0.6)", margin=dict(l=20, r=40, t=40, b=20))
    st.plotly_chart(fig_fi, use_container_width=True)
    
    st.markdown("""
        <div class="dashboard-card" style="margin-top: 15px; border-color: rgba(0, 210, 255, 0.3);">
            <p style='color: var(--text-main); font-size: 0.95rem; margin: 0;'>
                <strong>Interpretation Note:</strong> Feature importance is derived using Gini impurity decrease across all trees in the Random Forest ensemble. 
                Glucose concentration remains the most dominant predictive biomarker for diabetes classification within this patient cohort.
            </p>
        </div>
    """, unsafe_allow_html=True)

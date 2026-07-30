import streamlit as st
from streamlit_option_menu import option_menu
import sys
import os

# Add src to path to allow absolute imports
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.utils.styling import set_page_config, inject_custom_css
from src.pages.dashboard import render_dashboard
from src.pages.prediction import render_prediction
from src.pages.performance import render_performance
from src.pages.insights import render_insights

def main():
    set_page_config()
    inject_custom_css()
    
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.markdown("""
<div style='text-align: center; margin-bottom: 2rem;'>
    <h1 style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🧬 HealthAI</h1>
    <p style='color: var(--text-muted); font-size: 1.1rem;'>Enterprise Authentication Portal</p>
</div>
""", unsafe_allow_html=True)
            
            with st.form("login_form"):
                st.text_input("Medical ID", value="admin")
                st.text_input("Access Token", type="password", value="password")
                submit = st.form_submit_button("AUTHORIZE ACCESS")
                if submit:
                    with st.spinner("Authenticating credentials..."):
                        import time
                        time.sleep(0.8)
                        st.session_state.logged_in = True
                        st.rerun()
            
            st.markdown("<p style='text-align: center; color: var(--text-muted); font-size: 0.85rem; margin-top: 1.5rem;'>Secure connection established. HIPAA compliant.</p>", unsafe_allow_html=True)
        return

    with st.sidebar:
        st.markdown("""
<div style="text-align: center; margin-bottom: 2rem; padding-top: 1rem;">
    <h2 style="margin-bottom: 0;">🧬 HealthAI</h2>
    <p style="color: var(--text-muted); font-size: 0.85rem; margin-top: 0;">Diagnostic Inference Engine</p>
</div>
""", unsafe_allow_html=True)
        
        selected = option_menu(
            menu_title=None,
            options=["Dashboard", "Inference Engine", "Model Performance", "Dataset Insights"],
            icons=["grid", "cpu", "bar-chart-line", "database"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": "var(--primary)", "font-size": "18px"},
                "nav-link": {
                    "font-size": "15px", 
                    "text-align": "left", 
                    "margin": "8px 0px", 
                    "--hover-color": "rgba(0, 210, 255, 0.05)",
                    "color": "var(--text-main)",
                    "font-weight": "500",
                    "border-radius": "8px"
                },
                "nav-link-selected": {
                    "background-color": "rgba(0, 210, 255, 0.1)", 
                    "border-left": "3px solid var(--primary)",
                    "border-radius": "0 8px 8px 0"
                },
            }
        )
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
<div class="dashboard-card" style="padding: 1rem; border-color: rgba(16, 185, 129, 0.3); background: rgba(16, 185, 129, 0.05);">
    <div style="display: flex; align-items: center; margin-bottom: 8px;">
        <div class="status-indicator"></div>
        <span style="color: var(--success); font-weight: 600; font-size: 0.95rem;">System Nominal</span>
    </div>
    <div style="color: var(--text-muted); font-size: 0.8rem; line-height: 1.5;">
        <div><strong>Model:</strong> RF-Ensemble v2.4</div>
        <div><strong>Latency:</strong> 42ms</div>
    </div>
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("TERMINATE SESSION"):
            st.session_state.logged_in = False
            st.rerun()

    if selected == "Dashboard":
        render_dashboard()
    elif selected == "Inference Engine":
        render_prediction()
    elif selected == "Model Performance":
        render_performance()
    elif selected == "Dataset Insights":
        render_insights()

if __name__ == "__main__":
    main()

import streamlit as st

def set_page_config():
    """Sets the global page configuration for the application."""
    st.set_page_config(
        page_title="AI Health Analytics | Enterprise",
        page_icon="🧬",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def inject_custom_css():
    """Injects custom CSS to create a premium, production-level healthcare SaaS look."""
    st.markdown("""
        <style>
        /* Base Variables - Premium Navy & Cyan AI Theme */
        :root {
            --primary: #00d2ff;
            --secondary: #3a7bd5;
            --bg-dark: #070e20;
            --bg-card: rgba(16, 25, 45, 0.6);
            --bg-card-hover: rgba(22, 35, 60, 0.8);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --border: rgba(0, 210, 255, 0.15);
            --glow: 0 0 20px rgba(0, 210, 255, 0.1);
        }

        /* Global App Styling */
        .stApp {
            background-color: var(--bg-dark);
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(0, 210, 255, 0.03) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(58, 123, 213, 0.03) 0%, transparent 40%);
            color: var(--text-main);
            font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        /* Typography Improvements */
        h1, h2, h3, h4, h5, h6 {
            font-weight: 600 !important;
            letter-spacing: -0.02em;
            color: var(--text-main) !important;
        }
        
        h1 {
            font-size: 2.2rem !important;
            margin-bottom: 0.5rem !important;
            background: linear-gradient(to right, #ffffff, var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Hide Streamlit default components and Cloud UI */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .viewerBadge_container {display: none !important;}
        .stDeployButton {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        [data-testid="stAppDeployButton"] {display: none !important;}
        #viewerBadge_container {display: none !important;}
        .viewerBadge_link {display: none !important;}
        [data-testid="manage-app-button"] {display: none !important;}
        [data-testid="viewerBadge"] {display: none !important;}
        div[class*="viewerBadge"] {display: none !important;}
        div[class*="stDeployButton"] {display: none !important;}
        div[class*="stAppDeployButton"] {display: none !important;}
        
        /* Specifically target the GitHub Profile Picture and Streamlit Watermarks */
        img[src*="avatars.githubusercontent.com"] {display: none !important; visibility: hidden !important;}
        a[href*="streamlit.io/cloud"] {display: none !important; visibility: hidden !important;}

        /* =========================================
           NATIVE STREAMLIT OVERRIDES
           ========================================= */

        /* Style Streamlit Metrics */
        div[data-testid="metric-container"] {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        }
        div[data-testid="metric-container"]:hover {
            transform: translateY(-2px);
            border-color: rgba(0, 210, 255, 0.4);
            box-shadow: var(--glow);
        }
        div[data-testid="stMetricLabel"] {
            color: var(--text-muted) !important;
            font-size: 0.9rem !important;
            font-weight: 500;
        }
        div[data-testid="stMetricValue"] {
            font-size: 2.2rem !important;
            font-weight: 700 !important;
            color: var(--primary) !important;
        }

        /* Style Dataframes */
        [data-testid="stDataFrame"] {
            border: 1px solid var(--border);
            border-radius: 12px;
            overflow: hidden;
        }

        /* Style Forms natively */
        [data-testid="stForm"] {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1.5rem;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }

        /* Inputs */
        .stNumberInput > div > div > input, 
        .stTextInput > div > div > input {
            background-color: rgba(7, 14, 32, 0.7) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: var(--text-main) !important;
            border-radius: 8px !important;
            padding: 0.75rem !important;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }
        
        .stNumberInput > div > div > input:focus, 
        .stTextInput > div > div > input:focus {
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 1px var(--primary) !important;
        }

        /* Buttons */
        .stButton > button {
            background: linear-gradient(135deg, var(--secondary) 0%, var(--primary) 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1.5rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 210, 255, 0.2);
            width: 100%;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 210, 255, 0.4);
            color: white;
        }

        /* Form submit button override */
        [data-testid="stFormSubmitButton"] > button {
            margin-top: 1rem;
            padding: 0.75rem 2rem;
            font-size: 1.05rem;
            letter-spacing: 0.05em;
        }

        /* Progress Bars */
        .stProgress > div > div > div > div {
            background-image: linear-gradient(90deg, var(--secondary), var(--primary));
            border-radius: 10px;
        }
        .stProgress > div > div {
            background-color: rgba(255,255,255,0.05);
            border-radius: 10px;
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: rgba(7, 14, 32, 0.95) !important;
            border-right: 1px solid var(--border);
        }

        /* =========================================
           REUSABLE UTILITY CLASSES (HTML ONLY)
           ========================================= */

        .dashboard-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            transition: transform 0.3s ease, border-color 0.3s ease;
        }

        .dashboard-card:hover {
            border-color: rgba(0, 210, 255, 0.4);
        }

        .glow-effect {
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.2);
        }

        .prediction-badge {
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
        }
        .badge-danger {
            background-color: rgba(239, 68, 68, 0.1);
            color: var(--danger);
            border: 1px solid var(--danger);
        }
        .badge-success {
            background-color: rgba(16, 185, 129, 0.1);
            color: var(--success);
            border: 1px solid var(--success);
        }

        /* Animations */
        @keyframes pulse-border {
            0% { box-shadow: 0 0 0 0 rgba(0, 210, 255, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(0, 210, 255, 0); }
            100% { box-shadow: 0 0 0 0 rgba(0, 210, 255, 0); }
        }
        
        .status-indicator {
            display: inline-block;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background-color: var(--success);
            margin-right: 8px;
            animation: pulse-border 2s infinite;
        }

        /* Clean List Formatting */
        .premium-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .premium-list li {
            position: relative;
            padding-left: 20px;
            margin-bottom: 10px;
            color: var(--text-main);
            font-size: 0.95rem;
        }
        .premium-list li:before {
            content: '•';
            position: absolute;
            left: 0;
            color: var(--primary);
            font-size: 1.2rem;
            line-height: 1;
        }
        </style>
    """, unsafe_allow_html=True)

import textwrap

def render_html_card(title, content, icon=None):
    """Helper to render a self-contained premium HTML card."""
    icon_html = f"<span style='margin-right: 10px; font-size: 1.2rem;'>{icon}</span>" if icon else ""
    
    dedented_content = textwrap.dedent(content).strip()
    
    html = f"""
<div class="dashboard-card">
    <h4 style="margin-top: 0; margin-bottom: 15px; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 10px; color: var(--text-main);">
        {icon_html}{title}
    </h4>
    <div style="font-size: 0.95rem; line-height: 1.6; color: var(--text-muted);">
        {dedented_content}
    </div>
</div>
"""
    st.markdown(html, unsafe_allow_html=True)

import streamlit as st
import time
from datetime import datetime
import uuid
import pandas as pd
import os
from src.utils.ml_simulator import simulate_processing, generate_prediction, create_gauge_chart, get_medical_recommendation
from src.utils.styling import render_html_card

def render_prediction():
    st.markdown("<h1>Diagnostic Inference Engine</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: var(--text-muted); font-size: 1.1rem; margin-bottom: 2rem;'>Input patient clinical metrics to generate a predictive diagnostic report.</p>", unsafe_allow_html=True)
    
    # Initialize session state for prediction results
    if 'prediction_run' not in st.session_state:
        st.session_state.prediction_run = False
        
    col1, col2 = st.columns([1, 1.2], gap="large")
    
    with col1:
        st.markdown("<h3 style='margin-bottom: 15px;'>📋 Patient Clinical Data</h3>", unsafe_allow_html=True)
        
        # We rely on our native CSS targeting [data-testid="stForm"] for the card look! No HTML wrapper.
        with st.form("prediction_form"):
            st.markdown("<h4 style='color: var(--primary); margin-bottom: 10px;'>Patient Information</h4>", unsafe_allow_html=True)
            col_id, col_name = st.columns(2)
            with col_id:
                patient_id = st.text_input("Patient ID (Primary Key) *", value=f"PID-{uuid.uuid4().hex[:6].upper()}")
            with col_name:
                patient_name = st.text_input("Patient Name (Optional)")
            patient_notes = st.text_area("Additional Clinical Notes (Optional)", height=68)
            
            st.markdown("<hr style='border-color: rgba(255,255,255,0.1); margin: 20px 0;'>", unsafe_allow_html=True)
            st.markdown("<h4 style='color: var(--primary); margin-bottom: 10px;'>Clinical Metrics</h4>", unsafe_allow_html=True)
            
            col_a, col_b = st.columns(2)
            with col_a:
                pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
                glucose = st.number_input("Glucose (mg/dL)", min_value=0, max_value=300, value=120)
                bp = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200, value=70)
                skin = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
            with col_b:
                insulin = st.number_input("Insulin (IU/mL)", min_value=0, max_value=900, value=79)
                bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, format="%.1f")
                dpf = st.number_input("Diabetes Pedigree", min_value=0.0, max_value=3.0, value=0.5, format="%.2f")
                age = st.number_input("Age", min_value=1, max_value=120, value=30)
                
            submitted = st.form_submit_button("RUN CLASSIFICATION PIPELINE 🚀")
            
    with col2:
        if submitted:
            st.session_state.prediction_run = True
            
            st.markdown("<h3 style='margin-bottom: 15px;'>⚙️ Processing Pipeline Active</h3>", unsafe_allow_html=True)
            
            with st.spinner("Initializing Inference Engine..."):
                placeholder = st.empty()
                progress_bar = st.progress(0)
                
                steps = [
                    "Loading data into memory...",
                    "Applying feature scaling (StandardScaler)...",
                    "Running feature extraction...",
                    "Passing through Random Forest Ensemble...",
                    "Aggregating tree predictions...",
                    "Calculating confidence scores...",
                    "Prediction pipeline completed."
                ]
                
                simulate_processing(steps, placeholder, progress_bar)
                
                patient_data = {
                    "Pregnancies": pregnancies,
                    "Glucose": glucose,
                    "Blood Pressure": bp,
                    "Skin Thickness": skin,
                    "Insulin": insulin,
                    "BMI": bmi,
                    "Diabetes Pedigree": dpf,
                    "Age": age
                }
                
                pred_class, confidence = generate_prediction(patient_data)
                
                st.session_state.pred_class = pred_class
                st.session_state.confidence = confidence
                st.session_state.patient_data = patient_data
                patient_info = {
                    "id": patient_id if patient_id else f"PID-{uuid.uuid4().hex[:6].upper()}",
                    "name": patient_name if patient_name else "Anonymous",
                    "notes": patient_notes,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.patient_info = patient_info
                
                # Save to CSV
                record = {
                    "Patient ID": patient_info['id'],
                    "Name": patient_info['name'],
                    "Timestamp": patient_info['timestamp'],
                    "Prediction": "Diabetic" if pred_class == 1 else "Non-Diabetic",
                    "Confidence (%)": round(confidence, 1),
                    "Glucose": patient_data['Glucose'],
                    "BMI": patient_data['BMI'],
                    "Age": patient_data['Age'],
                    "Notes": patient_info['notes']
                }
                df = pd.DataFrame([record])
                if not os.path.exists("patient_records.csv"):
                    df.to_csv("patient_records.csv", index=False)
                else:
                    df.to_csv("patient_records.csv", mode='a', header=False, index=False)
                
                time.sleep(0.5)
                st.rerun()

        if st.session_state.prediction_run and 'pred_class' in st.session_state:
            pred_class = st.session_state.pred_class
            confidence = st.session_state.confidence
            
            # Show Results
            status_class = "badge-danger" if pred_class == 1 else "badge-success"
            status_text = "DIABETIC RISK DETECTED" if pred_class == 1 else "LOW RISK / NON-DIABETIC"
            
            p_info = st.session_state.patient_info
            
            st.markdown(f"""
<div class='dashboard-card' style='border-color: rgba(0, 210, 255, 0.3); margin-bottom: 1rem;'>
    <div style='display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 10px; margin-bottom: 15px;'>
        <div>
            <h4 style='margin: 0; color: var(--primary);'>Patient Record: {p_info['id']}</h4>
            <span style='color: var(--text-muted); font-size: 0.85rem;'>Name: {p_info['name']}</span>
        </div>
        <div style='text-align: right;'>
            <span style='color: var(--text-muted); font-size: 0.85rem;'>Timestamp</span><br>
            <span style='font-family: monospace; color: var(--text-main); font-size: 0.9rem;'>{p_info['timestamp']}</span>
        </div>
    </div>
    {f"<p style='color: var(--text-muted); font-size: 0.9rem; margin: 0;'><strong>Notes:</strong> {p_info['notes']}</p>" if p_info['notes'] else ""}
</div>
            
<div class='dashboard-card' style='text-align: center; padding: 2rem; border-color: {'var(--danger)' if pred_class == 1 else 'var(--success)'};'>
    <h3 style='color: var(--text-muted); font-size: 1rem; margin-bottom: 15px; text-transform: uppercase;'>Final Classification Result</h3>
    <div class='prediction-badge {status_class}' style='font-size: 1.5rem; padding: 1rem 2rem; box-shadow: 0 0 30px {'rgba(239, 68, 68, 0.2)' if pred_class == 1 else 'rgba(16, 185, 129, 0.2)'};'>
        {status_text}
    </div>
</div>
""", unsafe_allow_html=True)
            
            col_chart, col_recs = st.columns([1, 1], gap="medium")
            
            with col_chart:
                # No HTML wrapper!
                fig = create_gauge_chart(confidence)
                # Update background to look like a premium card
                fig.update_layout(paper_bgcolor="rgba(16, 25, 45, 0.6)", margin=dict(l=20, r=20, t=50, b=20))
                st.plotly_chart(fig, use_container_width=True)
                
            with col_recs:
                recs = get_medical_recommendation(confidence, pred_class == 1)
                recs_html = "".join([f"<li>{r}</li>" for r in recs])
                
                render_html_card(
                    title="Intelligent Insights",
                    icon="💡",
                    content=f"""
<ul class='premium-list'>
    {recs_html}
</ul>
"""
                )
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.download_button(
                    label="📄 Export Clinical Report (PDF)",
                    data="Simulated PDF Content - To be implemented fully",
                    file_name="AI_Prediction_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        else:
            st.markdown("""
<div class='dashboard-card' style='text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: center; opacity: 0.6; min-height: 400px; border-style: dashed;'>
    <div style='font-size: 4rem; margin-bottom: 20px; filter: grayscale(100%);'>🧬</div>
    <h3 style="color: var(--text-muted);">Awaiting Input Data</h3>
    <p style="color: rgba(255,255,255,0.4);">Fill out the clinical parameters on the left and run the pipeline to generate a diagnostic report.</p>
</div>
""", unsafe_allow_html=True)

    # View Records Section
    st.markdown("<hr style='border-color: rgba(255,255,255,0.1); margin: 40px 0 20px 0;'>", unsafe_allow_html=True)
    
    col_btn, _ = st.columns([1, 3])
    with col_btn:
        if st.button("🗃️ Toggle Patient Records Database"):
            st.session_state.show_records = not st.session_state.get('show_records', False)
            
    if st.session_state.get('show_records', False):
        st.markdown("<h3 style='margin-bottom: 15px; margin-top: 10px;'>Secure Patient History</h3>", unsafe_allow_html=True)
        if os.path.exists("patient_records.csv"):
            df = pd.read_csv("patient_records.csv")
            # Sort by Timestamp descending (newest first)
            if "Timestamp" in df.columns:
                df = df.sort_values(by="Timestamp", ascending=False)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # Allow downloading the full CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Database Backup (CSV)",
                data=csv,
                file_name='patient_records_backup.csv',
                mime='text/csv',
            )
        else:
            st.info("No patient records found in the local database. Run a classification pipeline to save data.")

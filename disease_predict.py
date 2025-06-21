import streamlit as st

def run():
    st.subheader("🧠 Disease Prediction")
    symptoms = st.text_area("Enter your symptoms (comma-separated):", "")

    if st.button("Predict Disease"):
        if symptoms:
            # Simulated response (replace with real IBM Granite call)
            response = f"Based on symptoms like {symptoms}, possible conditions include:\n- Migraine\n- Viral Fever\n- Fatigue Syndrome"
            st.success(response)
        else:
            st.warning("Please enter some symptoms.")
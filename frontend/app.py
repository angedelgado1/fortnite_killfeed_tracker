import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/kills"

st.set_page_config(page_title="Fortnite Kill Feed Tracker", layout="wide")
st.title("🏆 Fortnite Kill Feed Tracker")

response = requests.get(API_URL)
kill_data = response.json() if response.status_code == 200 else []

col1, col2 = st.columns([2, 1])  # Left = Summary, Right = Timeline

with col1:
    st.subheader("🔥 Top Players This Match")
    for kill in kill_data:
        st.write(f"{kill['killer']} eliminated {kill['victim']} with {kill['weapon']}")

with col2:
    st.subheader("📜 Kill Feed Timeline")
    for kill in reversed(kill_data):
        st.markdown(f"**[{kill['timestamp']}] {kill['killer']} eliminated {kill['victim']}** ({kill['weapon']})")

st.rerun()


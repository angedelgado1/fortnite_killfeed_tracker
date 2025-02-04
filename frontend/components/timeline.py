import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/kills"

def render_kill_feed():
    """Fetch and display the running kill feed timeline."""
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        kill_feed_data = response.json()
    else:
        kill_feed_data = []

    st.subheader("📜 Kill Feed Timeline")

    # Show latest kills first (reverse order)
    for kill in reversed(kill_feed_data):
        killer = kill["killer"]
        victim = kill["victim"]
        weapon = kill["weapon"]
        crown_status = kill.get("crown_dropped", "")
        timestamp = kill.get("timestamp", "Unknown Time")

        st.markdown(f"**[{timestamp}] {killer} eliminated {victim}** ({weapon}) {crown_status}")

# Run the function when the script is executed
if __name__ == "__main__":
    render_kill_feed()

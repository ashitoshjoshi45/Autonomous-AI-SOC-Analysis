import streamlit as st
import pandas as pd
import plotly.express as px
import time
import json
import os

st.set_page_config(page_title="AI SOC Dashboard", page_icon="🛡️", layout="wide")

st.title("🛡️ Autonomous AI SOC Analysis")
st.markdown("Monitoring **Ghost Sensor** hits and **Gemini AI** assessments.")

def load_security_data():
    log_file = "sensor_logs.json"
    if not os.path.exists(log_file):
        return pd.DataFrame()
    
    try:
        with open(log_file, "r") as f:
            data = json.load(f)
        return pd.DataFrame(data)
    except:
        return pd.DataFrame()

# Sidebar Refresh
refresh_rate = st.sidebar.slider("Refresh Rate (sec)", 5, 60, 5)

# Data Display
df = load_security_data()

if not df.empty:
    # Top Stats
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Hits", len(df))
    col2.metric("Malicious", len(df[df['verdict'] == 'MALICIOUS']))
    col3.metric("Avg Confidence", f"{df['confidence'].mean():.1f}%")

    # Chart
    fig = px.pie(df, names='verdict', title="Threat Distribution", color_discrete_map={'SAFE':'green', 'MALICIOUS':'red'})
    st.plotly_chart(fig)

    # Table
    st.subheader("Recent Activity")
    st.dataframe(df.sort_values(by="timestamp", ascending=False), use_container_width=True)
else:
    st.info("Waiting for incoming sensor data... (Start listener.py and send a request)")

time.sleep(refresh_rate)
st.rerun()
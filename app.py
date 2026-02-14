import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(page_title="SpineHealth AI", page_icon="🧘", layout="wide")

st.title("🧘 Personal Posture Analytics")

if 'posture_data' not in st.session_state:
    st.session_state.posture_data = pd.DataFrame(columns=['Time', 'Angle', 'Status'])

placeholder = st.empty()

for _ in range(100):
    # Simulated angle from MPU6050 (0 is straight, >20 is slouching)
    current_angle = round(np.random.normal(10, 5) if _ < 50 else np.random.normal(30, 5), 1)
    status = "Good" if current_angle < 20 else "Slouching"
    
    new_entry = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), current_angle, status]], 
                             columns=st.session_state.posture_data.columns)
    st.session_state.posture_data = pd.concat([st.session_state.posture_data, new_entry]).tail(20)

    with placeholder.container():
        c1, c2 = st.columns([1, 2])
        
        with c1:
            color = "green" if status == "Good" else "red"
            st.markdown(f"### Current Status: <span style='color:{color}'>{status}</span>", unsafe_allow_html=True)
            st.metric("Spine Angle", f"{current_angle}°", delta=f"{current_angle-15}°" if current_angle > 15 else "Stable")
            
            # Progress bar for time spent slouching
            slouch_pct = (st.session_state.posture_data['Status'] == 'Slouching').mean() * 100
            st.write(f"Daily Slouching Ratio: {round(slouch_pct)}%")
            st.progress(int(slouch_pct))

        with c2:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=st.session_state.posture_data['Time'], 
                                     y=st.session_state.posture_data['Angle'],
                                     mode='lines+markers', line_color='#636EFA'))
            fig.add_hline(y=20, line_dash="dash", line_color="red", annotation_text="Slouch Threshold")
            fig.update_layout(title="Spinal Alignment Timeline", yaxis_title="Angle (Degrees)")
            st.plotly_chart(fig, use_container_width=True)

    time.sleep(1)

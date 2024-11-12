import streamlit as st
import pandas as pd
import threading
import time
from monitoring import start_traffic_monitor, traffic_data, detect_ddos_traffic
from vulnerability_scanner import vulnerability_scan
from database import save_ddos_event, save_traffic_log

# Dashboard Title
st.title("Security Monitoring Dashboard")
st.sidebar.header("Options")

# Traffic Monitoring Controls
if st.sidebar.button("Start Traffic Monitor"):
    st.sidebar.success("Traffic monitoring started.")
    threading.Thread(target=start_traffic_monitor).start()

# Real-Time Traffic Data Display
st.subheader("Real-Time Traffic Data")
real_time_placeholder = st.empty()
traffic_display_duration = 10  # Number of refreshes in the UI for real-time data

for _ in range(traffic_display_duration):
    if traffic_data:
        traffic_df = pd.DataFrame(traffic_data)
        real_time_placeholder.write(traffic_df.tail(10))  # Display the latest 10 packets
        # Save each traffic record to the database
        for log in traffic_data[-10:]:  # Save only recent data to avoid redundancy
            save_traffic_log(log)
    else:
        real_time_placeholder.write("No traffic data captured yet.")
    time.sleep(1)

# DDoS Detection Section
st.subheader("DDoS Detection")
if st.sidebar.button("Check for DDoS Attacks"):
    if traffic_data:
        traffic_df = pd.DataFrame(traffic_data)
        anomalies = detect_ddos_traffic(traffic_data)
        attack_df = pd.DataFrame([data for i, data in enumerate(traffic_data) if anomalies[i] == -1])

        if not attack_df.empty:
            st.warning("DDoS attack detected!")
            for _, row in attack_df.iterrows():
                save_ddos_event(row.to_dict())  # Save detected DDoS events
            st.write("Detected DDoS Events:")
            st.write(attack_df)  # Display detected DDoS events
        else:
            st.success("No DDoS attacks detected.")
    else:
        st.write("No traffic data available to analyze.")

# View DDoS History Section
st.subheader("DDoS History")
if st.sidebar.button("View DDoS History"):
    conn = sqlite3.connect('security_app.db')
    history_df = pd.read_sql_query("SELECT * FROM ddos_history", conn)
    conn.close()
    st.write(history_df) if not history_df.empty else st.write("No DDoS events recorded.")

# Vulnerability Scanner
st.subheader("Website Vulnerability Scanner")
url = st.text_input("Enter the URL to scan for vulnerabilities")
if st.button("Scan Website"):
    if url:
        results = vulnerability_scan(url)
        st.write("Scan Results:")
        for result in results:
            st.write(result)
    else:
        st.write("Please enter a URL to scan.")

# Logout Button
if st.button("Logout"):
    st.session_state['logged_in'] = False
    st.session_state.pop('username', None)
    st.write("You have been logged out. Please return to the main page to log in again.")

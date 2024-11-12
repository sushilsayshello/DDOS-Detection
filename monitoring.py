import pandas as pd
from scapy.all import sniff
from sklearn.ensemble import IsolationForest
from datetime import datetime
from database import save_ddos_event, save_traffic_log

traffic_data = []

def capture_traffic(packet):
    if packet.haslayer('IP'):
        packet_info = {
            "src": packet['IP'].src,
            "dst": packet['IP'].dst,
            "length": len(packet),
            "timestamp": datetime.now()
        }
        traffic_data.append(packet_info)
        save_traffic_log(packet_info)
        if len(traffic_data) > 10000:
            traffic_data.pop(0)

def start_traffic_monitor():
    sniff(prn=capture_traffic, store=False, iface="lo0")  # Adjust "lo0" as per your setup

def detect_ddos_traffic(data):
    df = pd.DataFrame(data)
    if df.empty:
        return []
    traffic_features = df[['length']].values
    model = IsolationForest(contamination=0.01)
    model.fit(traffic_features)
    anomalies = model.predict(traffic_features)
    return anomalies

def visualize_traffic():
    df = pd.DataFrame(traffic_data)
    if df.empty:
        return "No traffic data to display."
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

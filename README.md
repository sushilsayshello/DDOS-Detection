# 🛡️ DDOS Monitoring and Security System

A robust, real-time security solution for monitoring network traffic, detecting DDoS attacks, and scanning web vulnerabilities. This application combines the power of Streamlit, machine learning, and user-friendly features to provide comprehensive protection and analysis of network and web security.

## 🌟 Features

- **🔐 User Authentication**: Register and login securely with hashed passwords.
- **📈 Real-Time Traffic Monitoring**: Track incoming and outgoing traffic live.
- **🚨 DDoS Attack Detection**: Detect potential DDoS attacks using machine learning (Isolation Forest & XGBoost).
- **🔍 Website Vulnerability Scanner**: Scan URLs for common vulnerabilities like SQL injection and XSS.
- **📲 Alert System**: Send SMS and email alerts upon detecting suspicious activities.
- **📊 Admin Dashboard**: View traffic, DDoS detections, and scan vulnerabilities all in one place.

## 🗂️ Project Structure

```plaintext
├── main.py                 # Main landing page for login and registration
├── dashboard.py            # Dashboard page for logged-in users
├── auth.py                 # User authentication functions
├── database.py             # Database connection and schema setup
├── monitoring.py           # Real-time traffic monitoring and DDoS detection
├── vulnerability_scanner.py # Vulnerability scanning functions
├── utils.py                # Utility functions (e.g., hashing)
├── logs.py                 # Logging setup for user and system events
├── models
│   └── tuned_xgboost_model.pkl # Pretrained model for DDoS detection
└── README.md               # Project documentation

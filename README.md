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


# DDOS - APP

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Libraries listed in `requirements.txt`
- Twilio account for SMS alerts
- Gmail account or SMTP settings for email verification

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sushilsayshello/DDOS-App.git
    cd DDOS-App
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## 🔧 Configuration

### Twilio Setup (for SMS alerts):

1. Set up your Twilio account to get the Account SID and Auth Token.
2. Update `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` in `main.py`.

### Email Setup (for email verification):

1. Configure `SMTP_SERVER`, `SMTP_PORT`, `EMAIL_ADDRESS`, and `EMAIL_PASSWORD` in `main.py`.

### Database:

1. Ensure the `security_app.db` SQLite database is created using the `init_db()` function in `database.py`.

## 🎬 Running the Application

To start the application, run:

```bash
streamlit run main.py
# DDOS - APP

The application will be available at [http://localhost:8501](http://localhost:8501).

## 📖 Usage

- **Register and Login**: Create an account and log in to access the dashboard.
- **Traffic Monitoring**: Start real-time traffic monitoring from the dashboard.
- **DDoS Detection**: Identify any potential DDoS attacks.
- **Vulnerability Scanner**: Enter a URL to scan for common vulnerabilities.
- **DDoS History**: View a record of past detected DDoS events and anomalies.

## 🧠 Machine Learning Model

The application includes a pre-trained XGBoost model (`tuned_xgboost_model.pkl`) for advanced DDoS detection. If you want to train a custom model, you can do so and replace the file in the `models/` directory.

## ⚙️ Technologies Used

- **Python & Streamlit**: Backend and UI.
- **SQLite**: Database for user data and traffic logs.
- **Twilio API**: SMS alerts.
- **SMTP**: Email verification.
- **Scikit-learn & XGBoost**: Machine learning-based DDoS detection.

## 📁 Example .gitignore

To keep sensitive and unnecessary files out of your repository, add a `.gitignore` file like below:

```plaintext
# Python cache
__pycache__/
*.py[cod]

# Virtual environment
venv/

# Config and environment files
.env
security_app.db

## 📝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📫 Contact

If you have any questions, feel free to reach out at [your_email@example.com].



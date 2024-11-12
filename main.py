import streamlit as st
from auth import save_user, login_user
from database import init_db

# Set the page configuration at the very top of main.py
st.set_page_config(page_title="Security Monitoring System", layout="wide")

# Initialize the database (this will create the tables if they don’t exist)
init_db()

# Check if the user is already logged in
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Landing page
if not st.session_state['logged_in']:
    st.title("Welcome to the Security Monitoring System")
    st.write("This system offers real-time DDoS detection and website vulnerability scanning. \
              Please log in or create an account to access the full features.")
    
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Register":
        st.subheader("Create a New Account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Sign Up"):
            if save_user(username, password):
                st.success("Account created successfully! Please log in.")
            else:
                st.warning("Username already exists.")
    
    elif choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login_user(username, password):
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success("Logged in successfully!")
            else:
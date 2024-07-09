import streamlit as st
import re
from database import get_db_connection

def validate_email(email):
    """Validates the format of the email."""
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

def validate_password(password):
    """Validates the length of the password."""
    if len(password) >= 8:
        return True
    return False

def login_user():
    st.header("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not validate_email(email):
            st.error("Invalid email format")
            return False
        if not validate_password(password):
            st.error("Password must be at least 8 characters long")
            return False
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, name, address, payment_method FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            st.session_state.user_id = user[0]
            st.session_state.user_email = email  # Store email in session state
            st.session_state.user_name = user[1]
            st.session_state.user_address = user[2]
            st.session_state.user_payment = user[3]
            st.session_state.loggedin = True
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Invalid email or password")
            return False

def register_user():
    st.header("Register")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    name = st.text_input("Name")
    address = st.text_input("Address")
    payment_method = st.text_input("Payment Method")

    if st.button("Register"):
        if not validate_email(email):
            st.error("Invalid email format")
            return
        if not validate_password(password):
            st.error("Password must be at least 8 characters long")
            return
        
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (email, password, name, address, payment_method) VALUES (%s, %s, %s, %s, %s)",
                           (email, password, name, address, payment_method))
            conn.commit()
            st.success("Account created successfully!")
        except Exception as e:
            st.error(f"Error creating account: {e}")
        finally:
            conn.close()

def account_page():
    if 'loggedin' in st.session_state and st.session_state.loggedin:
        st.header("Account Information")
        st.write(f"**Name:** {st.session_state.user_name}")
        st.write(f"**Email:** {st.session_state.user_email}")
        st.write(f"**Address:** {st.session_state.user_address}")
        st.write(f"**Payment Method:** {st.session_state.user_payment}")

        if st.button("Logout"):
            st.session_state.loggedin = False
            st.session_state.user_id = None
            st.session_state.user_email = None
            st.session_state.user_name = None
            st.session_state.user_address = None
            st.session_state.user_payment = None
            st.success("Logged out successfully!")
            st.experimental_rerun()
    else:
        st.title("Account")
        choice = st.radio("Choose an option", ["Login", "Register"])

        if choice == "Login":
            if login_user():
                st.experimental_rerun()
        elif choice == "Register":
            register_user()

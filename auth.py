import streamlit as st
from database import get_db_connection

def login_user():
    st.header("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            st.session_state.user_id = user[0]
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
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email, password, name, address, payment_method) VALUES (%s, %s, %s, %s, %s)",
                       (email, password, name, address, payment_method))
        conn.commit()
        conn.close()
        st.success("Account created successfully!")

import streamlit as st
from database import get_db_connection

def about_us():
    st.title("About Us")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM about_us")
    about_us_content = cursor.fetchone()
    conn.close()
    st.write(about_us_content[0])

def contact_us():
    st.title("Contact Us")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM contact_us")
    contact_us_content = cursor.fetchone()
    conn.close()
    st.write(contact_us_content[0])

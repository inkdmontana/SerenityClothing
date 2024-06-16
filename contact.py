import streamlit as st
from database import get_db_connection
from datetime import datetime

def contact_form():
    st.title("Contact Us")
    name = st.text_input("Name")
    email = st.text_input("Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message")

    if st.button("Submit"):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contact_form (name, email, subject, message, submission_date) VALUES (%s, %s, %s, %s, %s)",
                       (name, email, subject, message, datetime.now()))
        conn.commit()
        conn.close()
        st.success("Your message has been sent successfully!")

import mysql.connector
import streamlit as st


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="serenity_clothing"
    )


def test_db_connection():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()
        if db_name:
            st.success(f"Successfully connected to the database: {db_name[0]}")
        else:
            st.error("Failed to connect to the database.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

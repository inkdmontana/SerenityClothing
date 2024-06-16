import streamlit as st
from database import get_db_connection
from cart import add_to_cart

def show_promotional_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM promotional_good_reviews")
    products = cursor.fetchall()
    conn.close()

    st.subheader("Promotional Products with Good Reviews")
    for product in products:
        st.image(product[4], width=150)
        st.write(f"**{product[1]}**")
        st.write(f"Price: ${product[3]}")
        st.write(f"Average Rating: {product[5]}")
        if st.button('Add to Cart', key=product[0]):
            add_to_cart(product[0])

def show_about_us():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM about_us")
    about_us_content = cursor.fetchone()
    conn.close()
    st.subheader("About Us")
    st.write(about_us_content[0])

def show_contact_us():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM contact_us")
    contact_us_content = cursor.fetchone()
    conn.close()
    st.subheader("Contact Us")
    st.write(contact_us_content[0])

def homepage():
    st.title("Welcome to Serenity Clothing")
    show_promotional_products()
    show_about_us()
    show_contact_us()

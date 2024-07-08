import streamlit as st
from database import get_db_connection
from cart import add_to_cart
from PIL import Image


def show_promotional_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM promotional_good_reviews")
    products = cursor.fetchall()
    conn.close()

    st.balloons()
    st.header("Check Out Our Latest Promotions")
    image = Image.open('images/b2s.jpg')
    st.image(image)
    st.write("Save %50 off select items in-store until August 7!")

    st.header('Looking for Tips on Style?')
    st.write('Check out these resources and let us know what you think by contacting us!')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader('Basic Styling')
        st.write('Build your basics wardrobe')
        st.button('Read more',
                  on_click='window.open("https://www.dailyinspirato.com/the-complete-guide-creating-a-basics-wardrobe'
                           '-that-works-for-you")')
    with col2:
        st.subheader('Finding Style')
        st.write('Psychology of fashion')
        st.button('Explore',
                  on_click='window.open("https://fashionispsychology.com/trying-on-new-clothes-is-like-trying-on-new'
                           '-selves/")')

    with col3:
        st.subheader('Latest Trends')
        st.write('Stay up to date')
        st.button('Discover',
                  on_click='window.open("https://www.vogue.com/fashion/trends")')

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
    # show_about_us()
    # show_contact_us()

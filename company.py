import streamlit as st
from database import get_db_connection
from PIL import Image


def about_us():
    st.title("About Us")
    image = Image.open('images/promo_stock.jpg')
    st.image(image)
    conn = get_db_connection()
    cursor = conn.cursor()

    st.subheader('Our Style')
    content = 'At Serenity, we believe in the timeless appeal of simplicity and the power of versatility. Our style philosophy centers on crafting high-quality, essential pieces that form the backbone of any wardrobe. ' \
              'By focusing on clean lines, classic silhouettes, and premium materials, we create clothing that transcends trends and stands the test of time. ' \
              'Each item is thoughtfully designed to offer comfort, functionality, and effortless style, ensuring that our customers can seamlessly transition from day to night, from work to play. ' \
              'We celebrate individuality by providing a blank canvas that allows personal expression through endless possibilities of styling. ' \
              'At Serenity, our commitment is to provide you with foundational pieces that you can rely on, season after season.'

    st.write(content)

    st.subheader('Our Purpose')
    content2 = ('Our purpose at Serenity is to create clothing that simplifies and enriches our customers\' lives. We '
                'strive to offer wardrobe staples that are not only stylish but also durable, allowing our customers '
                'to express themselves effortlessly.')

    st.write(content2)

    st.subheader('Meet the Team')

    st.subheader('As a Business')
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

import streamlit as st
from database import get_db_connection


def submit_review(product_id):
    st.title("Submit Review")
    rating = st.slider("Rating", 1, 5, 1)
    review_text = st.text_area("Review")

    if st.button("Submit"):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reviews (product_id, user_id, rating, review) VALUES (%s, %s, %s, %s)",
                       (product_id, st.session_state.user_id, rating, review_text))
        conn.commit()
        conn.close()
        st.success("Review submitted successfully!")

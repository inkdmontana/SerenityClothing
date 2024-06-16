import streamlit as st
from database import get_db_connection

def view_wishlist():
    st.title("Wishlist")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT products.product_id, products.name, products.price, products.image_url 
        FROM wishlist 
        JOIN products ON wishlist.product_id = products.product_id 
        WHERE wishlist.user_id = %s
    """, (st.session_state.user_id,))
    wishlist_items = cursor.fetchall()
    conn.close()

    for item in wishlist_items:
        st.image(item[3], width=150)
        st.write(f"**{item[1]}**")
        st.write(f"Price: ${item[2]}")
        if st.button('Remove from Wishlist', key=item[0]):
            remove_from_wishlist(item[0])

def remove_from_wishlist(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM wishlist WHERE user_id = %s AND product_id = %s",
                   (st.session_state.user_id, product_id))
    conn.commit()
    conn.close()
    st.success("Removed from wishlist!")
    st.experimental_rerun()

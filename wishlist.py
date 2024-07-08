import streamlit as st
from database import get_db_connection


def view_wishlist():
    st.title("Wishlist")

    if "loggedin" in st.session_state and st.session_state.loggedin:
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

    else:
        st.warning('You must be logged in to utilize the Wishlist feature.')



def add_to_wishlist(product_id):
    if 'user_id' not in st.session_state:
        st.error("You must be logged in to add items to the wishlist.")
        return

    user_id = st.session_state.user_id

    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the item is already in the wishlist
    cursor.execute("SELECT product_id FROM wishlist WHERE user_id = %s AND product_id = %s", (user_id, product_id))
    item = cursor.fetchone()
    print('ITEM: ' + str(item))

    if item:
        # If item is already in the wishlist, warn user
        show_popup()
    else:
        # If item is not in the wishlist, add it
        cursor.execute("INSERT INTO wishlist (user_id, product_id) VALUES (%s, %s)", (user_id, product_id))

    conn.commit()
    conn.close()
    st.success("Item added to wishlist!")


def remove_from_wishlist(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM wishlist WHERE user_id = %s AND product_id = %s",
                   (st.session_state.user_id, product_id))
    conn.commit()
    conn.close()
    st.success("Removed from wishlist!")
    st.experimental_rerun()


def show_popup():
    with st.expander("Warning", expanded=True):
        st.write("Item already in Wishlist.")

import streamlit as st
from database import get_db_connection


def add_to_cart(product_id):
    if 'user_id' not in st.session_state:
        st.error("You need to be logged in to add items to the cart.")
        return

    user_id = st.session_state.user_id

    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the item is already in the cart
    cursor.execute("SELECT quantity FROM cart WHERE user_id = %s AND product_id = %s", (user_id, product_id))
    item = cursor.fetchone()

    if item:
        # If item is already in the cart, update the quantity
        new_quantity = item[0] + 1
        cursor.execute("UPDATE cart SET quantity = %s WHERE user_id = %s AND product_id = %s",
                       (new_quantity, user_id, product_id))
    else:
        # If item is not in the cart, add it with quantity 1
        cursor.execute("INSERT INTO cart (user_id, product_id, quantity) VALUES (%s, %s, %s)", (user_id, product_id, 1))

    conn.commit()
    conn.close()
    st.success("Item added to cart!")


def remove_from_cart(product_id):
    if 'user_id' not in st.session_state:
        st.error("You need to be logged in to remove items from the cart.")
        return

    user_id = st.session_state.user_id

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cart WHERE user_id = %s AND product_id = %s", (user_id, product_id))
    conn.commit()
    conn.close()
    st.success("Item removed from cart!")
    st.experimental_rerun()


def view_cart():
    st.title("Shopping Cart")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT products.product_id, products.name, products.price, cart.quantity 
        FROM cart 
        JOIN products ON cart.product_id = products.product_id 
        WHERE cart.user_id = %s
    """, (st.session_state.user_id,))
    cart_items = cursor.fetchall()
    conn.close()

    total_price = 0
    for item in cart_items:
        st.write(f"**{item[1]}**")
        st.write(f"Price: ${item[2]}")
        st.write(f"Quantity: {item[3]}")
        total_price += item[2] * item[3]
        if st.button('Remove', key=item[0]):
            remove_from_cart(item[0])

    st.write(f"**Total Price: ${total_price}**")
    if st.button("Checkout"):
        confirm_order(total_price)


def confirm_order(total_price):
    import random
    order_confirmation_number = random.randint(100000, 999999)
    st.success(f"Order placed successfully! Your confirmation number is {order_confirmation_number}.")
    # Clear the cart after confirmation
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cart WHERE user_id = %s", (st.session_state.user_id,))
    conn.commit()
    conn.close()

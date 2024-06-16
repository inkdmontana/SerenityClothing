import streamlit as st
from database import get_db_connection
from cart import add_to_cart

def browse_products():
    st.title("Browse Products")
    search_query = st.text_input("Search for products")
    category = st.selectbox("Category", ["All", "Men", "Women"])  # Add actual categories
    min_price = st.number_input("Min Price", min_value=0.0)
    max_price = st.number_input("Max Price", min_value=0.0)
    min_rating = st.slider("Min Rating", 1, 5, 1)

    query = "SELECT * FROM products WHERE 1=1"
    params = []
    if search_query:
        query += " AND name LIKE %s"
        params.append(f"%{search_query}%")
    if category != "All":
        query += " AND category = %s"
        params.append(category)
    if min_price:
        query += " AND price >= %s"
        params.append(min_price)
    if max_price:
        query += " AND price <= %s"
        params.append(max_price)
    if min_rating:
        query += """
        AND product_id IN (
            SELECT product_id FROM reviews 
            GROUP BY product_id 
            HAVING AVG(rating) >= %s
        )
        """
        params.append(min_rating)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    products = cursor.fetchall()
    conn.close()

    for product in products:
        st.image(product[4], width=150)
        st.write(f"**{product[1]}**")
        st.write(f"Price: ${product[3]}")
        st.write(f"{product[2]}")
        if st.button('Add to Cart', key=product[0]):
            add_to_cart(product[0])

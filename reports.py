import streamlit as st
from database import get_db_connection
import pandas as pd


def generate_report():
    st.title("Generate Report")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

    if st.button("Generate"):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        SELECT p.name, SUM(oi.quantity) AS units_sold, SUM(oi.price * oi.quantity) AS total_sales, AVG(r.rating) AS average_rating, COUNT(r.review_id) AS customer_reviews
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        LEFT JOIN reviews r ON p.product_id = r.product_id
        JOIN orders o ON oi.order_id = o.order_id
        WHERE o.order_date BETWEEN %s AND %s
        GROUP BY p.product_id
        """
        cursor.execute(query, (start_date, end_date))
        report_data = cursor.fetchall()
        conn.close()

        report_df = pd.DataFrame(report_data, columns=["Product Name", "Units Sold", "Total Sales", "Average Rating",
                                                       "Customer Reviews"])
        st.write(report_df)

        st.bar_chart(report_df.set_index("Product Name")["Units Sold"])
        st.line_chart(report_df.set_index("Product Name")["Total Sales"])

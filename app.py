import streamlit as st
from auth import login_user, register_user
from homepage import homepage
from product import browse_products
from cart import view_cart
from review import submit_review
from wishlist import view_wishlist
from company import about_us, contact_us
from contact import contact_form
from reports import generate_report
from database import test_db_connection


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "Browse", "Cart", "Account", "Submit Review", "Wishlist",
                                          "Promotional Products", "About Us", "Contact Us", "Reports"])

    # Test database connection on app start
    test_db_connection()

    if page == "Home":
        homepage()
    elif page == "Browse":
        browse_products()
    elif page == "Cart":
        if 'loggedin' in st.session_state and st.session_state.loggedin:
            view_cart()
        else:
            st.warning('You must be logged in to view the Cart.')
    elif page == "Account":
        account_page()
    elif page == "Submit Review":
        if 'loggedin' in st.session_state and st.session_state.loggedin:
            product_id = st.number_input("Product ID", min_value=1)
            submit_review(product_id)
        else:
            st.warning('You must be logged in to submit a review.')
    elif page == "Wishlist":
        view_wishlist()
    elif page == "Promotional Products":
        homepage()
    elif page == "About Us":
        about_us()
    elif page == "Contact Us":
        contact_us()
        contact_form()
    elif page == "Reports":
        if 'loggedin' in st.session_state and st.session_state.loggedin:
            generate_report()
        else:
            st.warning('You must be logged in to generate reports.')

def account_page():
    st.title("Account")
    choice = st.radio("Choose an option", ["Login", "Register"])

    if choice == "Login":
        if login_user():
            st.experimental_rerun()
    elif choice == "Register":
        register_user()


if __name__ == "__main__":
    main()

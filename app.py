import streamlit as st
from auth import login_user, register_user, account_page
from homepage import homepage
from product import browse_products
from cart import view_cart
from review import submit_review
from wishlist import view_wishlist
from company import about_us, contact_us
from contact import contact_form
from reports import generate_report
from database import test_db_connection

# Initialize session state variables if not already set
if 'loggedin' not in st.session_state:
    st.session_state.loggedin = False
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'user_email' not in st.session_state:
    st.session_state.user_email = None
if 'user_name' not in st.session_state:
    st.session_state.user_name = None
if 'user_address' not in st.session_state:
    st.session_state.user_address = None
if 'user_payment' not in st.session_state:
    st.session_state.user_payment = None

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

if __name__ == "__main__":
    main()

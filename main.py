import streamlit as st

if not st.user.is_logged_in:
    if st.button("Login"):
        st.user.login()
else:
    st.write(f"Hello, {st.user.name}!")
    if st.button("Logout"):
        st.user.logout()
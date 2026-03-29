import streamlit as st
from utils import find_user, check_password

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = find_user(username)
    if user and check_password(password, user["password"]):
        st.session_state.user = user
        st.session_state.role = user["role"]
        st.success("Login successful!")
        # Aquí puedes redirigir o cambiar la página
    else:
        st.error("Invalid username or password")
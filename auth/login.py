import streamlit as st
from utils import find_user, check_password

username = st.text_input()
password = st.text_input(type="password")

if st.button("Login"):

    user = find_user(username)

    if check_password(password):

        st.session_state.user = user
        st.session_state.role = user["role"]
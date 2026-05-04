import streamlit as st
from functions import send_message, load_history
import requests
from config import API_URL

# Estado inicial
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN
if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.post(f"{API_URL}/auth/login", json={
            "user_id": username,
            "password": password
        })

        if response.status_code == 200:
            data = response.json()

            st.session_state.logged_in = True
            st.session_state.user_id = data["user_id"]
            st.session_state.user_type = data["user_type"]

            st.rerun()
        
        if response.status_code == 404:
            st.error("User not found")
        if response.status_code == 401:
            st.error("Incorrect password")

# APP PRINCIPAL
if st.session_state.logged_in:

    # separar paciente / terapeuta
    if st.session_state.user_type == "patient":

        if "messages" not in st.session_state:
            st.session_state.messages = load_history(st.session_state.user_id)

        for msg in st.session_state.messages:
            if isinstance(msg, dict) and "role" in msg and "content" in msg:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])

        user_input = st.chat_input("I'm here to listen...")

        if user_input:
            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })

            response = send_message(st.session_state.user_id, user_input)

            bot_response = response.get("response", "No se pudo generar respuesta.")

            st.session_state.messages.append({
                "role": "assistant",
                "content": bot_response
            })

            st.rerun()

    # Terapeuta
    elif st.session_state.user_type == "therapist":
        st.title("Panel del terapeuta")
        st.write("Aquí irá el dashboard (resúmenes, pacientes, etc.)")

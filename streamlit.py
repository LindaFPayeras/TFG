import streamlit as st
from streamlit_ollama import ollama_chat_user
# Configuración de la página
st.set_page_config(page_title="Chat App", page_icon="💬")

st.title("💬 Chat con Streamlit")

# Inicializar historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
prompt = st.chat_input("Escribe un mensaje...")

if prompt:
    # Guardar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta fake (puedes conectar aquí tu backend)
    response = ollama_chat_user({"message": prompt})["response"]  # Simula la respuesta del bot

    # Guardar respuesta del bot
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Mostrar respuesta del bot
    with st.chat_message("assistant"):
        st.markdown(response)
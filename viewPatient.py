import streamlit as st

st.title("Psico App")
st.session_state.user = {"name": "DemoUser", "role": "patient", "therapist": "Dr. Smith"}  # Simulación de usuario logueado
topbar = st.container()
# Un topbar para poner el menú del usuaio y que se pueda deslogear
with topbar:
    userPanel, titulo = st.columns([1, 3])
    with titulo:
        st.write(f"{st.session_state.user['name']}'s chat")
    with userPanel:
        if st.button("", icon=":material/account_circle:"): # TO-DO: Tengo que poner foto a poder ser
            st.session_state.drawer = not st.session_state.drawer

# Definir el menu desplegable
st.session_state.drawer = st.session_state.get("drawer", False)
if st.session_state.drawer:
    st.sidebar.title(f"{st.session_state.user['name']}'s Profile")
    st.sidebar.write(f"Therapist: {st.session_state.user['therapist']}")
    
    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.session_state.drawer = False


########################
#
# Zona del chat. Comienza con un mensaje de bienvenida del asistente
#
#######################
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your mental health assistant. How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How are you feeling today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)





    
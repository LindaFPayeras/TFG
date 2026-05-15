import streamlit as st
from functions import send_message, load_history
import requests
from config import API_URL

# Estado inicial
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "selected_patient" not in st.session_state:
    st.session_state.selected_patient = None

st.markdown("""
<style>

/* Fondo general */
.stApp {
    background-color: #0e1117;
}

/* Inputs */
.stTextInput input {
    background-color: #1e2230;
    color: white;
    border: 1px solid #313543;
    border-radius: 12px;
    padding: 12px;
}

/* Focus input */
.stTextInput input:focus {
    border: 1px solid #6c63ff;
    box-shadow: 0 0 10px rgba(108,99,255,0.4);
}

/* Labels */
.stTextInput label {
    color: white;
    font-weight: 600;
}

/* Botón */
.stButton {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

.stButton button {
    background-color: #6c63ff;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 30px;
    font-size: 16px;
    transition: 0.2s;
}

/* Hover */
.stButton button:hover {
    background-color: #5848e5;
    transform: scale(1.03);
}

</style>
""", unsafe_allow_html=True)

# LOGIN
if not st.session_state.logged_in:

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        
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
        col1, col2 = st.columns([10, 1])
        with col1:
            st.markdown(
                f"""
                <h1 style="
                    margin-top: 36px;
                    margin-bottom: 36px;
                    padding: 0;
                ">
                    Welcome, {st.session_state.user_id}
                </h1>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown("""
                <style>

                /* Contenedor botón */
                .stButton {

                    display: flex;

                    justify-content: flex-end;
                }

                /* Botón */
                .stButton button {

                    width: 50px;
                    height: 50px;

                    border-radius: 50%;

                    background-color: #6366f1;

                    color: white;

                    border: none;

                    font-size: 24px;

                    padding: 0;

                    transition: 0.2s;
                }

                /* Hover */
                .stButton button:hover {

                    background-color: #4f46e5;

                    transform: scale(1.05);
                }

                </style>
                """, unsafe_allow_html=True)

            st.button(
                "🚪↩",
                on_click=lambda: st.session_state.update({
                    "logged_in": False,
                    "user_id": None,
                    "user_type": None
                })
            )
        
        container = st.container(border=False, height=900)

        with container:
            st.markdown("""
            <style>    

            /* Filas */
            .message-row {

                display: flex;

                width: 100%;

                margin-bottom: 14px;
            }

            /* Usuario */
            .user-row {

                justify-content: flex-end;
            }

            /* Assistant */
            .assistant-row {

                justify-content: flex-start;
            }

            /* Burbuja base */
            .chat-bubble {

                padding: 14px 18px;

                border-radius: 18px;

                max-width: 75%;

                font-size: 16px;

                line-height: 1.5;

                word-wrap: break-word;
            }

            /* Usuario */
            .user-bubble {

                background-color: #6366f1;

                color: white;
            }

            /* Assistant */
            .assistant-bubble {

                background-color: #1e293b;

                color: white;
            }

            </style>
            """, unsafe_allow_html=True)

            if "messages" not in st.session_state:

                st.session_state.messages = load_history(
                    st.session_state.user_id
                )

            st.markdown(
                '<div class="chat-container">',
                unsafe_allow_html=True
            )

            for msg in st.session_state.messages:

                if (
                    isinstance(msg, dict)
                    and "role" in msg
                    and "content" in msg
                ):

                    role = msg["role"]
                    content = msg["content"]

                    bubble_class = (
                        "user-bubble"
                        if role == "user"
                        else "assistant-bubble"
                    )

                    row_class = (
                        "user-row"
                        if role == "user"
                        else "assistant-row"
                    )

                    st.markdown(
                        f"""
                        <div class="message-row {row_class}">
                            <div class="chat-bubble {bubble_class}">
                                {content}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

        user_input = st.chat_input(
            "I'm here to listen..."
        )

        if user_input:

            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })

            response = send_message(
                st.session_state.user_id,
                user_input
            )

            bot_response = response.get(
                "response",
                "No se pudo generar respuesta."
            )

            st.session_state.messages.append({
                "role": "assistant",
                "content": bot_response
            })

            st.rerun()

    # Terapeuta
    elif st.session_state.user_type == "therapist":

        st.markdown("""
        <style>

        .stApp {
            background-color: #0f172a;
        }

        .block-container {
            padding-top: 2rem;
            padding-left: 3rem;
            padding-right: 3rem;
        }

        .patient-card {
            background: #1e293b;
            padding: 20px;
            border-radius: 18px;
            margin-bottom: 15px;
            border: 1px solid rgba(255,255,255,0.05);
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        }

        .report-card {
            background: #1e293b;
            padding: 25px;
            border-radius: 18px;
            margin-top: 20px;
            border: 1px solid rgba(255,255,255,0.05);
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        }

        .small-text {
            color: #94a3b8;
            font-size: 14px;
        }

        </style>
        """, unsafe_allow_html=True)

        with st.sidebar:
            st.title("🧠 MindCare")
            st.write(f"Terapeuta: {st.session_state.user_id}")

        if st.session_state.selected_patient is None:

            st.title(f"Welcome, {st.session_state.user_id}")

            # métricas rápidas
            col1, col2 = st.columns(2)

            response = requests.get(
                f"{API_URL}/data/relation/{st.session_state.user_id}"
            )

            if response.status_code == 200:

                patients = response.json()

                col1.metric("Patients", len(patients))
                col2.metric("Usages", "10")  # mock por ahora

                st.markdown("## Patients' list")

                for patient in patients:

                    emotion = "Happy"  # mock por ahora, luego traer de la API
                    st.markdown(f"""
                    <div class="patient-card">
                        <h4>👤 {patient}</h4>
                        <p class="small-text">Last emotion: {emotion}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    if st.button("See Report", key=patient):
                        st.session_state.selected_patient = patient
                        st.rerun()

            else:
                st.error("No se ha podido cargar la lista de pacientes")

            st.button(
                "🚪↩",
                on_click=lambda: st.session_state.update({
                    "logged_in": False,
                    "user_id": None,
                    "user_type": None
                })
            )
        else:

            st.title(f"📄 {st.session_state.selected_patient}")

            response = requests.get(
                f"{API_URL}/report/{st.session_state.selected_patient}"
            )

            if response.status_code == 200:

                report = response.json()

                col1, col2 = st.columns(2)

                col1.metric("Messages", report["num_messages"])
                col2.metric("Last online", "10 min ago")  # mock por ahora

                st.markdown(f"""
                <div class="report-card">
                    <h3>📝 Summary</h3>
                    <p>{report["summary"]}</p>
                </div>
                """, unsafe_allow_html=True)

            else:
                st.error("No se ha podido cargar el reporte del paciente")

            st.divider()

            st.button(
                "⬅ Back",
                on_click=lambda: st.session_state.update(
                    {"selected_patient": None}
                )
            )

        #  if st.session_state.selected_patient is None:
        #      st.title(f"Bienvenido, {st.session_state.user_id}")
        #      st.subheader("Lista de pacientes")
        #      # Cargar lista de pacientes
        #      response = requests.get(f"{API_URL}/data/relation/{st.session_state.user_id}")
        #      if response.status_code == 200:
        #          patients = response.json()
        #          for patient in patients:
        #              if st.button(patient, key=patient):
        #                  st.session_state.selected_patient = patient
        #                  st.rerun()
        #      else:
        #          st.error("No se ha podido cargar la lista de pacientes")
    
        #  else: # una vez seleccionado paciente
        #      st.title(f"{st.session_state.selected_patient}'s Report")
        #      response = requests.get(f"{API_URL}/report/{st.session_state.selected_patient}")
        #      if response.status_code == 200:
        #          report = response.json()
        #          st.subheader("Summary")
        #          st.write(report["summary"])
        #          st.subheader("Number of messages")
        #          st.write(report["num_messages"])
        #      else:
        #          st.error("No se ha podido cargar el reporte del paciente")
        #      st.button("Back", on_click=lambda: st.session_state.update({"selected_patient": None}))
            

import streamlit as st

st.set_page_config(page_title="Eco Chat", layout="centered")

# =========================
# CSS
# =========================
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background-color: #0e1117;
}

.chat-row {
    display: flex;
    margin: 8px 0;
    width: 100%;
}

.chat-row.user {
    justify-content: flex-end;
}

.chat-row.assistant {
    justify-content: flex-start;
}

.chat-bubble {
    padding: 12px 16px;
    border-radius: 18px;
    max-width: 70%;
    font-size: 15px;
    line-height: 1.5;
    word-wrap: break-word;
}

.user .chat-bubble {
    background-color: #2563eb;
    color: white;
    border-bottom-right-radius: 5px;
}

.assistant .chat-bubble {
    background-color: #262730;
    color: white;
    border-bottom-left-radius: 5px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# STATE
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hola 👋 Soy un chat eco. Todo lo que digas lo repetiré."
        }
    ]

# =========================
# TITLE
# =========================
st.title("💬 Eco Chat")

# =========================
# CHAT
# =========================
for msg in st.session_state.messages:

    role = msg["role"]
    content = msg["content"]

    st.markdown(
        f"""
        <div class="chat-row {role}">
            <div class="chat-bubble">
                {content}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# INPUT
# =========================
prompt = st.chat_input("Escribe algo...")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    st.session_state.messages.append({
        "role": "assistant",
        "content": prompt
    })

    st.rerun()
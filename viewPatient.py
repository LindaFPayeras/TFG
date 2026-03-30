import streamlit as st

st.set_page_config(layout="wide")

################################
# SESSION STATE
################################

if "user" not in st.session_state:
    st.session_state.user = {
        "name": "DemoUser",
        "role": "patient",
        "therapist": "Dr. Smith"
    }

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"assistant",
            "content":"Hello! I'm your mental health assistant. How can I help you today?"
        }
    ]


################################
# TOPBAR
################################

st.title("Psico App")

################################
# MAIN LAYOUT (SIEMPRE FIJO)
################################

info, chat = st.columns([1,3])


################################
# INFO PANEL
################################

with info:

    st.subheader("Patient profile")

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=120
    )

    st.write("**Name:**")
    st.write(st.session_state.user["name"])

    st.write("**Role:**")
    st.write(st.session_state.user["role"])

    st.write("**Therapist:**")
    st.write(st.session_state.user["therapist"])

    st.divider()

    st.subheader("Session")

    st.write("Messages:", len(st.session_state.messages))

    if st.button("Logout"):

        st.session_state.user = None
        st.session_state.messages = []
        st.rerun()


################################
# CHAT PANEL
################################

with chat:

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    if prompt := st.chat_input("How are you feeling today?"):

        st.session_state.messages.append(
            {"role":"user","content":prompt}
        )

        response = "Thank you for sharing that."

        st.session_state.messages.append(
            {"role":"assistant","content":response}
        )

        st.rerun()
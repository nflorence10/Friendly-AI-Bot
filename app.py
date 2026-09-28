import streamlit as st
import ollama

st.set_page_config(
    page_title="Friendly AI Bot",
    page_icon="🤖",
    layout="centered"
)

# ---------- CSS ----------
st.markdown(
    """
    <style>

    /* PAGE BACKGROUND */
    .stApp {
        background:
            radial-gradient(circle at top left, #315fa8 0%, transparent 40%),
            radial-gradient(circle at bottom right, #0d9488 0%, transparent 35%),
            linear-gradient(135deg, #0b1f3a, #123c69, #176b87);

        background-attachment: fixed;
    }


    /* MAIN CHATBOT CARD */
    .block-container {
        max-width: 720px;
        padding: 2.5rem 2.8rem;
        margin-top: 2.5rem;
        margin-bottom: 2rem;

        background: rgba(7, 25, 48, 0.88);

        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 24px;

        box-shadow:
            0 20px 50px rgba(0, 0, 0, 0.45),
            0 0 30px rgba(64, 190, 220, 0.15);

        backdrop-filter: blur(12px);
    }


    /* TITLE */
    h1 {
        text-align: center !important;
        color: #ffffff !important;
        font-size: 3rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.3rem !important;

        text-shadow:
            0 0 10px rgba(109, 213, 237, 0.7),
            0 0 25px rgba(109, 213, 237, 0.35);
    }


    /* SUBTITLE */
    .subtitle {
        text-align: center;
        color: #bdefff;
        font-size: 1.15rem;
        margin-bottom: 1.8rem;
        letter-spacing: 0.3px;
    }


    /* DIVIDER */
    .divider {
        height: 2px;

        background: linear-gradient(
            90deg,
            transparent,
            #6dd5ed,
            #ffffff,
            #6dd5ed,
            transparent
        );

        margin: 1rem 0 1.8rem 0;

        box-shadow: 0 0 10px rgba(109, 213, 237, 0.7);
    }


    /* INPUT LABEL */
    .stTextInput label {
        color: #e8faff !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
    }


    /* TEXT INPUT */
    .stTextInput input {
        background: rgba(3, 18, 35, 0.9) !important;
        color: #ffffff !important;

        border: 2px solid #2a78a8 !important;
        border-radius: 12px !important;

        padding: 0.8rem 1rem !important;
        font-size: 1rem !important;

        transition: all 0.2s ease;
    }


    .stTextInput input::placeholder {
        color: #8fa9ba !important;
    }


    .stTextInput input:focus {
        border-color: #6dd5ed !important;

        box-shadow:
            0 0 8px rgba(109, 213, 237, 0.7),
            0 0 20px rgba(109, 213, 237, 0.25) !important;
    }


    /* ASK AI BUTTON */
    .stButton > button {
        width: 100%;

        margin-top: 0.8rem;

        background: linear-gradient(
            90deg,
            #1677a8,
            #2a9dbe,
            #48c6d9
        );

        color: white !important;

        font-size: 1.1rem;
        font-weight: 700;

        border: none;
        border-radius: 12px;

        padding: 0.7rem 1rem;

        box-shadow:
            0 5px 15px rgba(0, 0, 0, 0.25);

        transition: all 0.2s ease;
    }


    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 8px 22px rgba(72, 198, 217, 0.4);

        background: linear-gradient(
            90deg,
            #2091c4,
            #38b9d0,
            #67d8e8
        );
    }


    /* RESPONSE TITLE */
    .response-title {
        background: rgba(3, 20, 38, 0.95);

        border: 1px solid rgba(109, 213, 237, 0.3);
        border-left: 5px solid #6dd5ed;

        border-radius: 15px;

        padding: 1rem 1.3rem;

        margin-top: 1.5rem;
        margin-bottom: 0.5rem;

        color: #6dd5ed;

        font-size: 1.15rem;
        font-weight: 700;

        text-shadow:
            0 0 8px rgba(109, 213, 237, 0.4);
    }


    /* AI RESPONSE TEXT */
    .stMarkdown {
        color: #f1f7fa;
    }


    /* WARNING */
    .stAlert {
        border-radius: 12px;
    }


    /* HIDE STREAMLIT MENU AND FOOTER */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- UI ----------

st.title("🤖 Friendly AI Bot")

st.markdown(
    '<div class="subtitle">Ask me anything, and let\'s figure it out together ✨</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)


# ---------- USER INPUT ----------

question = st.text_input(
    "Enter your question:",
    placeholder="Type your question here..."
)


# ---------- ASK AI ----------

if st.button("✨ Ask AI"):

    if not question.strip():

        st.warning("Please type a question first 🙂")

    else:

        with st.spinner("🤔 Thinking..."):

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "system",
                        "content": """
                        You are a friendly and funny AI assistant.
                        Explain things in simple language.
                        Be helpful and encouraging.
                        """
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

        answer = response["message"]["content"]


        # ---------- AI RESPONSE ----------

        st.markdown(
            '<div class="response-title">💬 AI Response</div>',
            unsafe_allow_html=True
        )

        st.write(answer)


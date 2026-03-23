"""
Main Streamlit Application for Quantum AI Assistant.

This script sets up the UI, manages the chat history, and orchestrates 
the interaction between speech-to-text, the AI engine, and text-to-speech.
"""
import streamlit as st
import time
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Import our custom modules
from speech_to_text import listen_and_transcribe
from text_to_speech import speak_text
from ai_engine import get_ai_response

st.set_page_config(page_title="Quantum AI Assistant", layout="centered")

# Custom CSS for dark theme and neon blue accents
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #050510;
        color: #e0e0e0;
    }
    
    /* Neon Blue Title */
    h1 {
        color: #00ffff !important;
        text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Neon button */
    .stButton > button {
        background-color: transparent !important;
        color: #00ffff !important;
        border: 2px solid #00ffff !important;
        box-shadow: 0 0 10px #00ffff inset, 0 0 10px #00ffff;
        border-radius: 8px;
        transition: 0.3s;
        width: 100%;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
        letter-spacing: 2px;
    }
    
    .stButton > button:hover {
        background-color: #00ffff !important;
        color: #000 !important;
        box-shadow: 0 0 20px #00ffff inset, 0 0 20px #00ffff;
    }
    
    /* Chat messages containers */
    .user-msg {
        background-color: #1a1a2e;
        border-left: 4px solid #0055ff;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    
    .ai-msg {
        background-color: #0f172a;
        border-left: 4px solid #00ffff;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
        box-shadow: 0 0 5px rgba(0, 255, 255, 0.2);
    }
    
    .status-text {
        color: #00ffff;
        font-style: italic;
        text-align: center;
        margin: 10px 0;
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 0.5; }
        50% { opacity: 1; }
        100% { opacity: 0.5; }
    }
    
    /* Hide top header and footer of streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("Quantum AI Assistant")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">👤 <b>User:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="ai-msg">🤖 <b>Quantum Core:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)

# Status placeholder
status_placeholder = st.empty()

if st.button("Start Listening"):
    # Step 1: Listen
    status_placeholder.markdown('<div class="status-text">🎙️ Listening...</div>', unsafe_allow_html=True)
    user_text = listen_and_transcribe()
    
    if user_text:
        # Display user message immediately in session state (needs rerun to show in loop, but we can append and show manually for smooth UX)
        st.session_state.messages.append({"role": "user", "content": user_text})
        st.markdown(f'<div class="user-msg">👤 <b>User:</b><br>{user_text}</div>', unsafe_allow_html=True)
        
        # Step 2 & 3: Processing & Generating Response
        status_placeholder.markdown('<div class="status-text">⚙️ Processing...</div>', unsafe_allow_html=True)
        time.sleep(0.5) # Slight pause for effect
        status_placeholder.markdown('<div class="status-text">✨ Generating Response...</div>', unsafe_allow_html=True)
        
        ai_response = get_ai_response(user_text)
        
        # Typing effect
        status_placeholder.empty()
        response_placeholder = st.empty()
        typed_text = ""
        for char in ai_response:
            typed_text += char
            response_placeholder.markdown(f'<div class="ai-msg">🤖 <b>Quantum Core:</b><br>{typed_text}▌</div>', unsafe_allow_html=True)
            time.sleep(0.01) # fast typing effect
            
        # Final display without cursor
        response_placeholder.markdown(f'<div class="ai-msg">🤖 <b>Quantum Core:</b><br>{ai_response}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        
        # Clear status
        status_placeholder.empty()
        
        # Step 4: Text to Speech
        speak_text(ai_response)
        
        # Rerun to cleanly draw everything from state
        st.rerun()
        
    else:
        status_placeholder.error("Could not hear anything or an error occurred. Please try again.")


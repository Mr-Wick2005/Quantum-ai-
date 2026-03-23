# 🧠 Quantum AI Assistant

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32.2-FF4B4B.svg)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-Pro-orange.svg)](https://deepmind.google/technologies/gemini/)

## 🚀 Description

Quantum AI Assistant is a futuristic, voice-enabled AI chatbot built specifically for conference environments. Originally designed for live conference demos, this project serves as a "Jarvis-like" assistant that can handle general inquiries comprehensively via Google's **Gemini Pro** API, while also having a robust rule-based command layer for instant, guaranteed responses to specific conference-related queries.

It features a custom dark and neon-blue futuristic Streamlit UI, voice recognition for hands-free interactions, and text-to-speech capabilities to read out the AI's intelligent responses.

## 🎯 Features

*   **Voice Input (Speech-to-Text)**: Automatically captures and transcribes microphone input using Google's free Web Speech API.
*   **AI Intelligence (Gemini Pro)**: Powered by Google's state-of-the-art `gemini-1.5-pro` model for general-purpose chatbot capabilities.
*   **Command Control (Jarvis Brain)**: Instantly answers command-oriented questions (like time, date, specific conference rooms) via a hardcoded fallback layer.
*   **Voice Output (Text-to-Speech)**: Uses `pyttsx3` to read responses aloud to users.
*   **Futuristic UI**: Streamlit interface enhanced with custom CSS for a "Quantum Core" aesthetic.

## 📁 Project Structure

```text
quantum-ai-assistant/
│
├── app/
│   ├── main.py                # Streamlit UI / main entry point
│   ├── ai_engine.py           # AI logic (Gemini integration & fallback routing)
│   ├── speech_to_text.py      # Microphone input & transcription
│   ├── text_to_speech.py      # Voice output handling
│   ├── logic.py               # Rule-based commands and fast responses
│   └── data.py                # Local conference data store
│
├── .env.example               # Template for environment variables
├── .gitignore                 # Standard Python gitignore
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## 🛠️ Setup Instructions

### 1. Prerequisites
Ensure you have **Python 3.10+** installed. On Windows, `PyAudio` is required which might require Microsoft C++ Build Tools depending on your environment.

### 2. Clone and Create Virtual Environment
```bash
git clone https://github.com/Mr-Wick2005/Quantum-ai-.git
cd Quantum-ai-
python -m venv venv

# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Copy the example environment file and add your actual API key:
```bash
cp .env.example .env
```
Open `.env` and configure your keys:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the Application
Start the Streamlit development server:
```bash
streamlit run app/main.py
```

## 🤝 Contributing
Feel free to open issues or submit pull requests for any improvements!

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).

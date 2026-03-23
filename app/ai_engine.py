"""
AI Engine Module.

Handles integration with Google's Gemini API, managing prompt structure,
conversation history, and routing queries through rule-based commands.
"""
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Import the new modules
from data import conference_data
from logic import get_rule_based_response, handle_commands

load_dotenv()

# Maintain short conversation memory (last 2 interactions = 4 messages)
conversation_history = []

SYSTEM_PROMPT = f"""
You are JARVIS, a highly advanced and comprehensive AI Assistant.

RULES:
1. For conference-specific questions, refer to the provided CONFERENCE DATA.
2. For any other general knowledge questions, act as a full-fledged intelligent chatbot. Provide detailed, helpful, and accurate answers.
3. Do not refuse to answer general questions. Answer comprehensively.
4. Be confident, conversational, and slightly futuristic.

CONFERENCE DATA:
{conference_data}
"""

def get_ai_response(user_input: str) -> str:
    global conversation_history
    
    try:
        # Step 0: Command handling (Jarvis brain)
        command_response = handle_commands(user_input)
        if command_response:
            return command_response

        # Step 1: Rule-based Fallback (fast + reliable)
        rule_response = get_rule_based_response(user_input)
        if rule_response:
            return rule_response
            
        # Step 2: Gemini Integration
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key or "your_" in api_key:
            api_key = os.getenv("OPENAI_API_KEY")
            
        if not api_key or "your_" in api_key:
            return "Error: API Key not configured. Please add GEMINI_API_KEY to your .env file."
            
        genai.configure(api_key=api_key)
        
        # Use correct model
        model = genai.GenerativeModel(
            model_name='gemini-1.5-pro',
            system_instruction=SYSTEM_PROMPT
        )
        
        # Map our history to Gemini format
        gemini_history = []
        for msg in conversation_history:
            role = "user" if msg["role"] == "user" else "model"
            gemini_history.append({"role": role, "parts": [msg["content"]]})
            
        # Call Gemini
        chat = model.start_chat(history=gemini_history)
        response = chat.send_message(user_input)
        
        # Step 3: Update History (Memory of last 2 interactions)
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": response.text})
        
        if len(conversation_history) > 4:
            conversation_history = conversation_history[-4:]
            
        return response.text
        
    except Exception as e:
        # Step 4: Print actual error in terminal and return meaningful error message
        print(f"ERROR: {e}")
        return "I'm experiencing a temporary issue. Please try again."

import speech_recognition as sr
import os

def listen_and_transcribe() -> str:
    """
    Captures audio from the microphone and uses Google's Web Speech API to transcribe.
    Returns the transcribed text, or an empty string if failed.
    """
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
        except sr.WaitTimeoutError:
            return ""
            
    try:
        # Use Google's free Web Speech API
        transcript = recognizer.recognize_google(audio)
        return transcript
    except Exception as e:
        print(f"Error during transcription: {e}")
        return ""

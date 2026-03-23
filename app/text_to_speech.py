import pyttsx3

def speak_text(text: str):
    """
    Converts text to speech using pyttsx3 and plays it through the speakers.
    """
    try:
        engine = pyttsx3.init()
        # You can adjust properties like rate and volume here if needed
        # engine.setProperty('rate', 175)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in text-to-speech: {e}")

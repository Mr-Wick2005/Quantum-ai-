import datetime

def handle_commands(user_input: str):
    text = user_input.lower()

    # TIME
    if "time" in text:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M')}"

    # DATE
    if "date" in text:
        return datetime.datetime.now().strftime("%A, %d %B %Y")

    # GREETING
    if "can you hear me" in text:
        return "Yes, I can hear you clearly."

    # IDENTITY
    if "who are you" in text:
        return "I am your Quantum Conference Assistant."

    return None

def get_rule_based_response(user_input: str) -> str:
    user_input = user_input.lower()
    
    if "vedant" in user_input:
        return "Team Vedant is assigned to Room A-301."
    
    if "alpha" in user_input:
        return "Team Alpha is assigned to Room B-204."
        
    if "registration" in user_input:
        return "Registration is on the Ground Floor."
        
    if "keynote" in user_input:
        return "The Keynote is in Auditorium 1."
        
    return None

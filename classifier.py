def classify_persona(user_message):
    message = user_message.lower()

    if any(word in message for word in [
        "api", "authentication", "token", "error", "endpoint", "debug"
    ]):
        return "Technical Expert"

    elif any(word in message for word in [
        "angry", "frustrated", "terrible", "hate", "worst", "upset"
    ]):
        return "Frustrated User"

    else:
        return "Business Executive"
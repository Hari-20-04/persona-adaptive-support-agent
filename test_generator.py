from src.generator import generate_response

context = """
Users can reset their password using the Forgot Password option.
A password reset link is sent to the registered email address.
The reset link expires after 15 minutes.
"""

response = generate_response(
    "Technical Expert",
    "How can I reset my password?",
    context
)

print(response)
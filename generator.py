import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_response(persona, query, context):
    prompt = f"""
You are a customer support assistant.

Persona: {persona}

User Question:
{query}

Retrieved Context:
{context}

Instructions:

If persona is Technical Expert:
- Give technical explanation
- Include root cause analysis
- Use precise terminology

If persona is Frustrated User:
- Be empathetic
- Acknowledge frustration
- Use simple language

If persona is Business Executive:
- Be concise
- Focus on business impact
- Provide clear recommendations

Answer only using the retrieved context.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception:
        return """
The AI response service is temporarily unavailable.

Based on the retrieved knowledge base:

- Please review the information provided in the retrieved documents.
- If the issue persists, contact customer support.
- Try again in a few minutes.
"""
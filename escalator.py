def should_escalate(query):
    query = query.lower()

    escalation_keywords = [
        "refund",
        "billing dispute",
        "legal",
        "lawsuit",
        "account hacked",
        "unauthorized charge",
        "fraud"
    ]

    return any(keyword in query for keyword in escalation_keywords)


def create_handoff(persona, query, docs):
    return {
        "persona": persona,
        "issue": query,
        "documents_used": list(set(docs)),
        "recommendation": "Escalate to human support"
    }
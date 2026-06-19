import streamlit as st

from classifier import classify_persona
from rag_pipeline import create_vector_store, retrieve
from generator import generate_response
from escalator import should_escalate, create_handoff

st.set_page_config(page_title="Persona Support Agent")

st.title("🤖 Persona Adaptive Support Agent")

# Create vector DB once
if "db_initialized" not in st.session_state:
    create_vector_store()
    st.session_state.db_initialized = True

query = st.text_input("Ask your question")

if st.button("Submit") and query:

    persona = classify_persona(query)

    docs = retrieve(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    if should_escalate(query):

        handoff = create_handoff(
            persona,
            query,
            list(set(doc.metadata["source"] for doc in docs))
        )

        st.error("⚠ Escalation Required")

        st.json(handoff)

    else:

        response = generate_response(
            persona,
            query,
            context
        )

        st.subheader("Detected Persona")
        st.write(persona)

        st.subheader("Response")
        st.write(response)

        st.subheader("Sources")

        sources = set()

        sources = list(set(doc.metadata["source"] for doc in docs))

        for source in sources:
            st.write(source)

from src.rag_pipeline import create_vector_store, retrieve

print("Creating vector database...")
create_vector_store()

print("Testing retrieval...")
results = retrieve("How can I reset my password?")

for doc in results:
    print("\n---")
    print("Source:", doc.metadata)
    print(doc.page_content)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

def load_documents(data_folder="."):
    docs = []

    for file in os.listdir(data_folder):
        if file.endswith(".txt"):
            with open(
                os.path.join(data_folder, file),
                "r",
                encoding="utf-8"
            ) as f:

                docs.append(
                    Document(
                        page_content=f.read(),
                        metadata={"source": file}
                    )
                )

    return docs


def create_vector_store():
    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=40
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
   )

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="chroma_db"
    )

    return db


def retrieve(query):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    return db.similarity_search(query, k=3)

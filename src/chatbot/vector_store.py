"""
Builds or rebuilds the FAQ vector database for the TechShop chatbot project.

This script loads all FAQs from a JSON file, generates embeddings using OpenAI, and stores them in a Chroma vector database compatible with LangChain.
It should be run manually after adding, removing or updating FAQs in 'data/faqs.json', or if you wish to reset the database.

Typical usage:
    $ python src/chatbot/vector_store.py

Requirements:
    - Environment variable OPENAI_API_KEY must be set (usually via .env file).
    - data/faqs.json must exist and contain the FAQs to ingest.
    - The output (vector database) is stored in data/vector_db/, matching the config in agent.py.

This script is safe to run multiple times. It will clear and rebuild the collection to ensure a fresh and consistent state.
"""

import os
from dotenv import load_dotenv
from chatbot.faq_loader import load_faqs
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Load environment variables from .env file
load_dotenv()

# Set the path for the vector store (must match agent.py)
data_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "data", "vector_db")
)

# Load FAQs from the JSON file
faqs = load_faqs("data/faqs.json")

# Initialise OpenAI embeddings via LangChain
embeddings = OpenAIEmbeddings()

# Create a Chroma vector store compatible with LangChain
vector_store = Chroma(
    collection_name="faqs",
    embedding_function=embeddings,
    persist_directory=data_dir
)

# Optional: Clear previous collection for a fresh build (useful for debugging)
try:
    vector_store.delete_collection()
    # Re-create the vector store object after deletion
    vector_store = Chroma(
        collection_name="faqs",
        embedding_function=embeddings,
        persist_directory=data_dir
    )
except Exception as e:
    print("Warning (delete_collection):", e)

# Prepare data for ingestion
questions = [faq.question for faq in faqs]
metadatas = [{"answer": faq.answer} for faq in faqs]
ids = [str(faq.id) for faq in faqs]

# Add FAQs to the vector store (embeddings, metadata, and IDs)
vector_store.add_texts(
    texts=questions,
    metadatas=metadatas,
    ids=ids,
)

print(f"Vector store created with {len(faqs)} FAQs ✅")
print("Example FAQ:", questions[0], "→", metadatas[0]["answer"])

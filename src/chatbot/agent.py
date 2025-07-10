"""
agent.py

Core logic for the TechShop FAQ chatbot:
- Connects to the vector database of FAQs
- Uses semantic similarity search to find the most relevant answer for each user question
- Reformulates answers using a Large Language Model (LLM), ensuring responses are accurate, friendly and always grounded in the FAQ database
- Falls back to a default message if no relevant FAQ is found

Designed for easy reuse and adaptation in retrieval-augmented chatbot projects.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

# Ensure OPENAI_API_KEY is set
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Please set the OPENAI_API_KEY environment variable in your .env file or system environment.")

# Import core components
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.schema import HumanMessage
from langchain.memory import ConversationBufferMemory

# Configure embeddings
embeddings = OpenAIEmbeddings()

# Initialize Chroma vector store for FAQs
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "data", "vector_db"))
vector_store = Chroma(
    collection_name="faqs",
    embedding_function=embeddings,
    persist_directory=data_dir
)

# Initialize the ChatOpenAI language model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.0
)

# Set up conversational memory buffer
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

def ask_bot(question: str) -> str:
    """
    Retrieve the most relevant FAQ answer for the user's question using semantic similarity.
    Only responds if similarity score is above the defined threshold.
    If no FAQ is relevant, a fallback message is returned.
    """
    # Use similarity search with score to access match score
    results = vector_store.similarity_search_with_score(question, k=1)
    if results:
        doc, score = results[0]
        # Set your similarity threshold (experiment with 0.7 - 0.8)
        threshold = 0.3
        if score <= threshold:
            raw_answer = doc.metadata.get("answer", "")
            prompt = (
                "You are a customer support assistant for TechShop.\n\n"
                "Here is an answer from our FAQ knowledge base:\n"
                f"{raw_answer}\n\n"
                "A user asked:\n"
                f"{question}\n\n"
                "Using only the information from the FAQ answer above, reply in a friendly and concise manner. "
                "Do not make up or change any details, numbers, or names."
            )
            response = llm([HumanMessage(content=prompt)])
            if hasattr(response, "content"):
                return str(response.content).strip()
            elif isinstance(response, list) and hasattr(response[0], "content"):
                return str(response[0].content).strip()
            else:
                return str(response).strip()
    # Fallback if no relevant FAQ found
    return (
        "I'm sorry, I couldn't find an answer to your question in our FAQs. "
        "Please contact our support team at support@techshop.com for further assistance."
    )

import os
import pytest
from chatbot.agent import ask_bot

def test_known_question():
    """Should return the expected FAQ answer (delivery to Lisbon)."""
    question = "What is the delivery time for Lisbon?"
    answer = ask_bot(question).lower()
    # Accepts both hyphen and en-dash in "2–4"
    assert "2–4" in answer or "2-4" in answer

def test_unknown_question():
    """Should return the fallback/support answer for an unknown query."""
    question = "How do I fly to the moon?"
    answer = ask_bot(question).lower()
    # Only check for key phrase in the fallback message
    assert "sorry" in answer or "contact our support" in answer

def test_vector_store_build():
    """
    Runs the vector_store.py script to check that the vector DB builds without exceptions.
    """
    # Uses absolut path to make sure it finds the script.
    result = os.system("python src/chatbot/vector_store.py")
    assert result == 0, "Vector DB build script failed!"

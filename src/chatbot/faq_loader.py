"""
faq_loader.py

FAQ data model and loader utility for the TechShop FAQ chatbot.

- Defines the FAQ schema using Pydantic for type safety
- Provides a function to load FAQs from a JSON file and parse them into FAQ objects

Usage:
    faqs = load_faqs("data/faqs.json")
"""

from typing import List
from pydantic import BaseModel
import json
import os

class FAQ(BaseModel):
    id: int
    question: str
    answer: str


def load_faqs(json_path: str) -> List[FAQ]:
    """
    Load FAQs from a JSON file and return a list of FAQ objects.
    Args:
        json_path (str): Path to the JSON file containing FAQs.
    Returns:
        List[FAQ]: A list of FAQ objects loaded from the file.
    Raises:
        FileNotFoundError: If the JSON file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"File not found: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    faqs = [FAQ(**item) for item in raw_data]
    return faqs


if __name__ == "__main__":
    faqs = load_faqs("data/faqs.json")
    print(f"Loaded {len(faqs)} FAQs:")
    for faq in faqs[:3]:
        print(f"Q: {faq.question}\nA: {faq.answer}\n")

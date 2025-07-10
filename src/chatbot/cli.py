"""
cli.py

Command-line interface for the TechShop FAQ chatbot.
- Provides an interactive prompt for users to type questions
- Sends questions to the core chatbot logic (ask_bot)
- Prints responses in a conversational style

To run: python -m chatbot.cli
"""

import os
from chatbot.agent import ask_bot

def main():
    print("🤖 TechShop FAQ Chatbot (type 'exit' to quit)")
    while True:
        q = input("\nYou: ")
        if q.lower() in ("exit", "quit"):
            print("Goodbye. See you soon!")
            break
        a = ask_bot(q)
        print(f"Bot: {a}")

if __name__ == "__main__":
    main()

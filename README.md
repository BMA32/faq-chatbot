# TechShop FAQ Chatbot

A retrieval-augmented chatbot for a fictional e-commerce platform called **TechShop**. This chatbot answers customer support questions by combining semantic search over a FAQ database with a large language model (LLM), built for modern e-commerce use cases. This project serves as a portfolio example for practical data science, LLMs and RAG systems.

## Demo

```bash
$ python -m chatbot.cli

🤖 TechShop FAQ Chatbot (type 'exit' to quit)

You: How long does delivery to Lisbon usually take?
Bot: Delivery to Lisbon takes 2–4 working days, depending on stock availability.

You: How can I become a TechShop ambassador?
Bot: I'm sorry, I couldn't find an answer to your question in our FAQs. Please contact our support team at support@techshop.com for further assistance.

```

## Motivation

Companies increasingly want reliable, AI-powered support bots — but real-world systems must avoid “hallucinations” and keep answers grounded in actual business knowledge. This project demonstrates a robust solution: combining semantic search over trusted FAQs with a state-of-the-art LLM, ensuring the chatbot never invents answers and always stays on brand.

Built as a practical exercise for my data science portfolio, it showcases:
- Good prompt engineering and RAG practices,
- Effective use of vector databases,
- Clear, maintainable code ready for adaptation or extension.

## How it works

1. **Vectorisation**: Every FAQ is embedded using OpenAI embeddings and stored in a Chroma vector database.
2. **Retrieval**: When a user asks a question, the bot finds the most semantically similar FAQ (using embedding search).
3. **Threshold**: Only if the FAQ is genuinely relevant (below a certain similarity threshold) does the bot answer; otherwise, it politely says it cannot help.
4. **LLM Paraphrase**: The LLM reformulates the FAQ answer in a customer-friendly tone, but never invents details.

This structure ensures both accuracy and a smooth customer experience.

## Features & Good Practices

- Retrieval-augmented generation: answers always grounded in trusted FAQs.
- Score threshold to prevent unrelated answers (avoiding hallucination).
- LLM only paraphrases, never invents facts.
- Configurable: easy to swap embeddings or vector store.
- Written in English, with clear structure and docstrings for readability and reuse.
- Portable: designed for both local demo and easy cloud deployment.

## Requirements

- Python 3.10.6 (recommended)
- [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) for environment management

If using pyenv (recommended):

```bash
pyenv install 3.10.6
pyenv virtualenv 3.10.6 chatbot-faq
pyenv local chatbot-faq
```

## Quickstart

1. **Clone the repo**
    ```bash
    git clone https://github.com/seu-utilizador/Chatbot-FAQ.git
    cd Chatbot-FAQ
    ```

2. **Create and activate your Python virtual environment**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key**
    - Create a `.env` file in the root folder with:
        ```
        OPENAI_API_KEY=sk-...
        ```

5. **Build the vector database**
    ```bash
    python src/chatbot/vector_store.py
    ```

6. **Run the chatbot**
    ```bash
    python -m chatbot.cli
    ```

## Embeddings and Thresholds

- By default, this project uses OpenAI embeddings for best performance.
- The similarity threshold is set to `0.3` — only questions closely matching a FAQ will be answered directly.
- You can tune the threshold in `agent.py` to make the bot stricter or more permissive.
- If you want a local-only version (no OpenAI cost), you can swap for `sentence-transformers` embeddings (see code comments).

## Customising FAQs

- All FAQs live in `data/faqs.json` — you can add, remove, or change questions and answers easily.
- The system is designed for e-commerce, but can be adapted for any sector.

## Dependencies

- Python 3.10+
- openai
- langchain-openai
- langchain-chroma
- chromadb
- python-dotenv

(See `requirements.txt` for the full list.)

## Development & Automation

For developer convenience, you can use the included `Makefile` to automate common tasks:

| Command            | Description                            |
|--------------------|----------------------------------------|
| `make install`     | Install project dependencies           |
| `make vectors`   | Build/rebuild the FAQ vector database  |
| `make test`        | Run all tests with pytest              |
| `make run`         | Start the chatbot CLI                  |
| `make lint`        | Lint code with flake8 (optional)       |

Feel free to adapt or extend these targets for your workflow.

## Extensions & Future Work

- **Database Integration**:
  This project uses a JSON file for demo purposes, but it can easily be adapted to fetch FAQs from a SQL or NoSQL database for production use.

- **Web/App Frontend**:
  The CLI can be extended with a web-based frontend (e.g. Streamlit or Gradio) for user-friendly interaction and live demos.

- **Cloud Deployment**:
  Ready to be containerised with Docker for deployment on cloud platforms (AWS, GCP, Azure, etc.).

- **Multi-language Support**:
  The chatbot can be extended to handle multiple languages or locales by changing the embedding model and FAQ sources.

- **Analytics/Logging**:
  Add user interaction logging and analytics for insight into customer queries and FAQ coverage.

## How to Adapt

- To use other LLMs or embeddings, just swap the relevant lines in `agent.py`.
- To increase the FAQ base, edit `data/faqs.json` — no code change needed.
- All code is modular and can be reused for other support/chatbot projects.

## Author

Bruno Malheiro
[LinkedIn](https://www.linkedin.com/in/bruno-malheiro/)
[Your portfolio site](https://troopl.com/bruno-malheiro)

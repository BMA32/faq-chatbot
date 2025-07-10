from setuptools import setup, find_packages

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(
    name="chatbot-faq",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "langchain",
        "chromadb",
        "openai",
        "python-dotenv",
        "pydantic",
        "numpy"
    ],
)

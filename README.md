# LangChain Q&A Demo with Streamlit

This repository demonstrates how to create a Question and Answer system using LangChain, OpenAI's Language Model (LLM), and Streamlit for a web-based interface.

## Prerequisites

Ensure you have the following installed:
- [Anaconda](https://www.anaconda.com/products/distribution)
- Python 3.8 or later

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/anachary/langchain-question-answer-demo.git
    cd langchain-question-answer-demo
    ```

2. **Create a Conda Environment**:
    ```bash
    conda create -n langchain-qa-demo python=3.9 -y
    conda activate langchain-qa-demo
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` File**:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```
5. **Run the Streamlit App**:
    ```bash
    streamlit run main.py
    ```

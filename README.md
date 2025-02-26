# Chat-with-Your-Documents

An AI-powered chatbot that lets you chat with your own PDF documents using Retrieval-Augmented Generation (RAG).


[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit App](https://img.shields.io/badge/Streamlit-App-blueviolet)](https://www.streamlit.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-blue)](https://fastapi.tiangolo.com/)

## Overview

This project implements a local question-answering system for PDF documents. Simply upload a PDF file, and the AI assistant will answer your questions based on the document's content. It leverages Retrieval-Augmented Generation (RAG) to provide accurate and context-aware responses.

## Key Features

*   **Local Document Q&A:**  Ask questions about the content of your PDF documents.
*   **Retrieval-Augmented Generation (RAG):**  Provides accurate and context-aware answers.
*   **Streamlit Frontend:**  User-friendly web interface.
*   **FastAPI Backend:**  Handles document processing and question answering.
*   **Persistent Vector Store:** Uses FAISS to efficiently store and retrieve document embeddings.
*   **Private and Secure:** Runs locally on your machine, keeping your documents private.

## Technology Stack

*   **Frontend:** [Streamlit](https://streamlit.io/)
*   **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
*   **Language Model:** [Together AI API](https://www.together.ai/) (Llama 3)
*   **Embeddings:** [Hugging Face Sentence Transformers](https://huggingface.co/sentence-transformers)
*   **Vector Store:** [FAISS](https://github.com/facebookresearch/faiss) (via Langchain)
*   **Document Loading & Splitting:** [Langchain](https://www.langchain.com/)
*   **Python:** 3.10+

## Prerequisites

*   Python 3.10 or higher
*   A [Together AI API key](https://www.together.ai/)

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/Chat-with-Your-Documents.git
    cd Chat-with-Your-Documents
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set your Together AI API key:**

    There are two options:
    *   **Option 1 (Recommended):** Set the `TOGETHER_API_KEY` environment variable.
        *   Linux/macOS: `export TOGETHER_API_KEY="YOUR_API_KEY"`
        *   Windows: `set TOGETHER_API_KEY=YOUR_API_KEY`
    *   **Option 2 (Not Recommended):**  You can hardcode the API key directly into `rag_backend.py`, but this is *not* recommended for security reasons.

## Running the Application

1.  **Start the FastAPI backend:**

    ```bash
    uvicorn backend_chatdoc:app --reload --host 0.0.0.0 --port 8000
    ```

    (The `--reload` flag will automatically restart the server when you make changes).

2.  **Start the Streamlit frontend (in a separate terminal):**

    ```bash
    streamlit run frontend_chatdoc.py
    ```

3.  **Access the application:** Open your web browser and go to the address shown by Streamlit (usually `http://localhost:8501`).

## Usage

1.  **Upload a PDF:** In the sidebar, use the file uploader to select a PDF document from your computer.
2.  **Ask Questions:** In the main chat interface, type your question and press "Send".
3.  **View Answers:** The AI assistant will generate an answer based on the content of the uploaded PDF and display it in the chat.

## Customization

*   **Modify the Prompt:**  You can customize the prompt used for the language model in the `query` function of `backend_chatdoc.py`.  Experiment with different prompts to improve the quality of the answers.
*   **Change the Embedding Model:** You can experiment with different sentence transformer models by changing the `model_name` in the `HuggingFaceEmbeddings` initialization.
*   **Adjust Chunk Size:**  The `chunk_size` parameter in the `CharacterTextSplitter` controls how the document is spli into chunks.  Adjust this value to optimize performance and accuracy.
*   **Switch LLM Provider:**  With some code modifications, you could use a different language model provider instead of Together AI.

## Contributing

Contributions are welcome! If you find a bug, have a feature request, or want to contribute code, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgments

*   This project is inspired by the growing field of Retrieval-Augmented Generation.
*   Thanks to the developers of Streamlit, FastAPI, Langchain, Hugging Face, Together AI, and FAISS for creating these amazing tools.t

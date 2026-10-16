# GenAI Document Assistant 📄

A Python-based GenAI Document Assistant that allows users to upload PDF documents, ask questions in natural language, and receive context-based answers using semantic search and a locally running Large Language Model (LLM).

## Features

- Upload PDF documents through a Streamlit interface.
- Extract text from PDF files using PyPDF.
- Split document text into overlapping chunks for retrieval.
- Generate text embeddings using Sentence Transformers (`all-MiniLM-L6-v2`).
- Retrieve relevant document chunks using cosine similarity.
- Generate answers using Llama 3.2 through Ollama.
- Display chat history and provide a Clear Chat option.
- Run the AI model locally without paid LLM API keys.

## Technologies Used

- Python
- Streamlit
- PyPDF
- Sentence Transformers
- Scikit-learn
- Embeddings
- Cosine Similarity
- Ollama
- Llama 3.2
- Retrieval-Augmented Generation (RAG)

## How It Works

1. Upload a PDF document.
2. Extract the text from the PDF.
3. Split the extracted text into smaller overlapping chunks.
4. Convert the chunks into numerical embeddings using `all-MiniLM-L6-v2`.
5. Convert the user's question into an embedding.
6. Calculate cosine similarity to retrieve relevant chunks.
7. Pass the retrieved context and question to Llama 3.2 through Ollama.
8. Display the generated answer in the Streamlit chatbot.

## Prerequisites

- Python 3.10 or a compatible Python version.
- Ollama installed on your computer.
- Llama 3.2 downloaded through Ollama.


## 📁 Project Structure

```text
genai-document-assistant/
├── app.py
├── requirements.txt
└── README.md
```

## 🎯 Learning Outcomes

- PDF text extraction and preprocessing.
- Text chunking and overlap handling.
- Semantic search using embeddings.
- Similarity-based document retrieval.
- Integration of a local LLM with Python.
- Building interactive AI applications using Streamlit.
- Understanding the fundamentals of Retrieval-Augmented Generation (RAG).

## 🔮 Future Enhancements

- Retrieve multiple relevant chunks for more complete answers.
- Improve duplicate-overlap handling.
- Add source page references and citations.
- Support multiple PDF documents.
- Improve retrieval using hybrid search.
- Deploy the application with a remotely hosted LLM.

## 👨‍💻 Project Type

Personal Learning Project

Built to explore semantic search, local LLMs, and Retrieval-Augmented Generation using free and open-source tools.

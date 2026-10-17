# 🤖 GenAI Document Assistant

An AI-powered PDF ChatBot application built with Python, Streamlit, Sentence Transformers, and the Google Gemini API. Upload a PDF document and ask questions to get AI-generated answers based on its content.

## 📌 Project Overview

The GenAI Document Assistant simplifies the process of understanding lengthy PDF documents. It extracts text, identifies relevant information using semantic similarity, and generates answers using a Large Language Model (LLM).

This project demonstrates a basic **Retrieval-Augmented Generation (RAG)** workflow by combining semantic search with generative AI.

## ✨ Features

- 📄 Upload PDF documents.
- 📝 Extract text from PDF pages.
- ✂️ Split text into overlapping chunks.
- 🧠 Generate text embeddings using Sentence Transformers.
- 🔍 Retrieve relevant content using cosine similarity.
- 🤖 Generate context-aware answers using the Google Gemini API.
- 💬 Interact with documents through a chat interface.
- 🧹 Clear chat history with one click.
- ☁️ Deploy and access the application online.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **PDF Processing:** PyPDF
- **Embedding Model:** all-MiniLM-L6-v2
- **Similarity Search:** Scikit-learn — Cosine Similarity
- **LLM:** Google Gemini API
- **Deployment:** Streamlit Community Cloud

## ⚙️ How It Works

1. **Upload PDF:** The user uploads a PDF through the sidebar.
2. **Extract Text:** PyPDF extracts text from each page.
3. **Chunking:** The extracted text is split into 500-character chunks with a 100-character overlap.
4. **Embedding Generation:** Sentence Transformers converts each chunk into a numerical vector.
5. **Semantic Search:** The user's question is converted into an embedding and compared with document chunks using cosine similarity.
6. **Context Retrieval:** The most relevant chunk is selected.
7. **Answer Generation:** The selected context and question are passed to the Gemini API.
8. **Display Answer:** The generated response is displayed in the chat interface.

## 🔄 Application Workflow

```text
PDF Upload
    |
    v
Text Extraction
    |
    v
Text Chunking
    |
    v
Generate Embeddings
    |
    v
User Asks a Question
    |
    v
Question Embedding
    |
    v
Cosine Similarity Search
    |
    v
Retrieve Relevant Chunk
    |
    v
Google Gemini API
    |
    v
Generate Answer
    |
    v
Display Response
```

## 🎯 Key Learnings

- Implementing a RAG pipeline.
- Extracting and preprocessing PDF text.
- Understanding text chunking and overlap.
- Generating semantic embeddings.
- Applying cosine similarity for information retrieval.
- Integrating an LLM through the Gemini API.
- Building interactive applications using Streamlit.
- Deploying an AI application to the cloud.

## 🔮 Future Enhancements

- Retrieve multiple relevant chunks for improved answers.
- Add support for multiple PDF documents.
- Display source page numbers and relevant excerpts.
- Improve follow-up question handling with conversation memory.
- Add OCR support for scanned PDFs.
- Optimize document processing for larger files.

## 👨‍💻 Author

**Nazeer Ahmad Gaddam**

Python Developer | SQL | Data Analytics | Data Science | Exploring Generative AI & Machine LearningPython Developer.

🔗 **Live Demo:** [GenAI Document Assistant](https://genai-document-assistant-jgthrfuevdzcoafj5atkap.streamlit.app/)

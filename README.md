# 🤖 GenAI Document Assistant

An AI-powered PDF ChatBot application built with **Python, Streamlit, Retrieval-Augmented Generation (RAG), Sentence Transformers, and the Groq API**.

Upload a PDF document and ask questions about its content. The application retrieves relevant text from the document and uses a large language model to generate contextual answers.

🔗 **Live Demo:** https://genai-document-assistant-jgthrfuevdzcoafj5atkap.streamlit.app/

## ✨ Features

- 📄 **PDF Upload:** Upload PDF documents directly through the interface.
- 💬 **Interactive Q&A:** Ask questions about the uploaded document.
- 🔍 **Semantic Retrieval:** Uses Sentence Transformers to identify relevant text chunks.
- 🧠 **RAG Architecture:** Grounds responses in retrieved PDF content.
- ⚡ **Groq API Integration:** Generates answers using the `openai/gpt-oss-20b` model.
- 🗂️ **Conversation History:** Displays previous questions and answers during the session.
- 🔄 **Clear Chat:** Reset the conversation using the Clear Chat button.
- 🚀 **Model Caching:** Uses Streamlit resource caching to reuse the embedding model.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Web application interface |
| PyPDF | Extracting text from PDF files |
| Sentence Transformers | Generating text embeddings |
| all-MiniLM-L6-v2 | Embedding model |
| Scikit-learn | Cosine similarity for retrieval |
| Groq API | Large language model inference |
| Git & GitHub | Version control and project hosting |

## ⚙️ How It Works

The application follows a Retrieval-Augmented Generation (RAG) workflow.

1. **Upload PDF:** The user uploads a PDF document.
2. **Text Extraction:** PyPDF extracts text from the document.
3. **Text Chunking:** The extracted text is divided into smaller overlapping chunks.
4. **Embedding Generation:** Sentence Transformers converts the chunks into numerical vectors.
5. **Question Processing:** The user's question is converted into an embedding.
6. **Similarity Search:** Cosine similarity identifies the most relevant chunks.
7. **Answer Generation:** The retrieved context and question are sent to the Groq API.
8. **Response Display:** The generated answer is displayed in the Streamlit chat interface.

## 📂 Project Structure

```text
genai-document-assistant/
│
├── app.py
├── requirements.txt
├── README.md
```

## 📦 Dependencies

Your `requirements.txt` should contain:

```text
streamlit
pypdf
sentence-transformers
scikit-learn
groq
```

## ⚠️ Limitations

- The application currently supports PDF files.
- Answer quality depends on the text extracted from the PDF and the relevance of retrieved chunks.
- Scanned PDFs may require OCR if they do not contain extractable text.
- Large documents may take longer to process.
- Generated answers may not always be accurate; verify important information against the original document.
- API usage is subject to Groq's current rate limits and availability.

## 🔮 Future Improvements

- Streaming responses for faster perceived answer time.
- Improved chunking and retrieval strategies.
- Support for multiple PDF documents.
- Persistent chat history.
- OCR support for scanned documents.
- Improved retrieval evaluation and response quality.

## 👨‍💻 Author

**Nazeer Ahmad Gaddam**

Python Developer | SQL | Data Analytics | Data Science | Exploring Generative AI & Machine Learning

---

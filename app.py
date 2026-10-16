import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import ollama


#------------------------model------------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

#--------------------------Main Screen-----------------------

col1, col2 = st.columns([5, 1])

with col1:
    st.title("GenAI Document Assistant")
    st.write("Ask me a question!!")

with col2:
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------------- Side Bar-----------------------------
st.sidebar.title("File Uploder")
uploaded_file = st.sidebar.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    st.sidebar.success("PDF uploaded successfully!")
    chunks = []

#---------------------Pdf Extractor-------------------

    pdf_reader = PdfReader(uploaded_file)

    pdf_text = ""

    for page in pdf_reader.pages:
        text = page.extract_text()
        pdf_text = pdf_text + text + "\n"


    st.sidebar.write("PDF text extracted successfully!")

#-----------------------chunking-------------------------------
    start = 0
    chunk_size = 500 
    overlap = 100

    # chunks = []

    while start < len(pdf_text):
        end = start + chunk_size
        chunk = pdf_text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        start = end - overlap

    st.sidebar.write("Chunking successfully!")

#----------------------TF-IDF Vectorization------------------

    doc_chunk_vectors = model.encode(chunks)

#-----------------------Display all--------------------------

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

#-------------------------User---------------------------------

    prompt = st.chat_input("Ask a question about your PDF...")

    if prompt:
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):                  # Display User Message 
            st.write(prompt)


#-----------------cosine similarity b/w ques & ans-----------

        def relavant_chunks(prompt,chunks,doc_chunk_vectors):
            prompt_vector = model.encode([prompt])

            similarities = cosine_similarity(prompt_vector,doc_chunk_vectors)[0]
            best_index = similarities.argmax()
            best_score = similarities[best_index]

            # st.write("Similarity scores:", similarities)
            # st.write("Best score:", best_score)

            return chunks[best_index]

#-------------------------Bot---------------------------------

        if chunks:
            relevant_chunk = relavant_chunks(prompt,chunks,doc_chunk_vectors)
            with st.spinner("Generating answer... Please wait"):
                result = ollama.chat(
                            model="llama3.2",
                            messages=[
                                        {
                                            "role": "system",
                                            "content": (
                                                        "Answer the question using only the supplied "
                                                        "PDF context. If the answer is not in the "
                                                        "context, say you could not find it in the PDF."
                                                        )
                                        },
                                        {
                                            "role": "user",
                                            "content": (
                                                        f"PDF context:\n{relevant_chunk}\n\n"
                                                        f"Question: {prompt}"
                                                        )
                                        }
                                    ]
                                    )
                response = result["message"]["content"]

        else:
            response = "Please upload a PDF first."

        st.session_state.messages.append({
            "role": "assistant",                        # Display and store assistant response
            "content": response
        })

        with st.chat_message("assistant"):
            st.write(response)

else:
    st.write("Please upload a PDF first.")



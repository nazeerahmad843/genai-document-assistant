#   Deployed Url
#   https://genai-document-assistant-jgthrfuevdzcoafj5atkap.streamlit.app/


import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
# import ollama
# from google import genai
import io
from groq import Groq


st.set_page_config(
    page_title="GenAI Document ChatBot",
    page_icon="🤖",
    layout="wide"
)

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")      #embeding

# with st.spinner("⏳ Initializing AI model... First load may take a little longer."):
    # model = load_model()

#--------------------------Main Screen-----------------------

col1, col2 = st.columns([5, 1])

with col1:
    st.title("GenAI Document Assistant")

with col2:
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------------- Side Bar-----------------------------
st.sidebar.title("File Uploder")

# Sidebar footer
st.sidebar.markdown(
    """
    <div style="
        position: fixed;
        bottom: 20px;
        width: 250px;
        text-align: center;
        color: gray;
        font-size: 13px;
        margin: 0;
        padding: 0;
    ">
        <hr>
        <p style="margin: 0;">Designed & Developed<br>
        <b>Nazeer</b></p>
        <small>Python · Streamlit · LLM · RAG</small>
    </div>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.sidebar.file_uploader(
                                            "Upload your PDF",
                                            type=["pdf"]
                                        )

@st.cache_data(show_spinner="Processing PDF...")
def process_pdf(pdf_bytes):
    model = load_model()
    pdf_reader = PdfReader(io.BytesIO(pdf_bytes))
    pdf_text = ""

    for page in pdf_reader.pages:
        text = page.extract_text() or ""
        pdf_text += text + "\n"
    
    start = 0
    chunk_size = 1000
    overlap = 150

    while start < len(pdf_text):
        end = start + chunk_size
        chunk = pdf_text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        start = end - overlap

    if not chunks:
        return [], None


    doc_chunk_vectors = model.encode(chunks)

    return chunks, doc_chunk_vectors

if uploaded_file is not None:
    st.sidebar.success("PDF uploaded successfully!")
    st.write("Ask me a questions!!!")
    chunks = []
    chunks, doc_chunk_vectors = process_pdf(uploaded_file.getvalue())
    
else:
    st.info("👈 Please upload a PDF first using the sidebar to start chatting.")
    st.stop()


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

    def relavant_chunks(prompt,chunks,doc_chunk_vectors,top_k=5):
        model = load_model()
        prompt_vector = model.encode([prompt],normalize_embeddings=True)

        similarities = cosine_similarity(prompt_vector,doc_chunk_vectors)[0]
        best_index = similarities.argsort()[-top_k:][::-1]
        best_score = similarities[best_index]

        # st.write("Similarity scores:", similarities)
        # st.write("Best score:", best_score)

        return "\n\n".join(chunks[i] for i in best_index)

#-------------------------Bot with LLM---------------------------------

    relevant_context = relavant_chunks(
                        prompt,
                        chunks,
                        doc_chunk_vectors
                        )

    if chunks:
        relevant_chunk = relavant_chunks(prompt,chunks,doc_chunk_vectors)
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        recent_messages = st.session_state.messages[-7:-1]

        messages = [
                      {
                        "role": "system",
                        "content": (
                                    "Answer questions using the supplied PDF context. "
                                    "Carefully check all relevant details in the context, "
                                    "including lists near the beginning or end of the document. "
                                    "If the information is present, answer directly. "
                                    "If it is absent, say you could not find it in the PDF. "
                                    "Do not invent information."
                                    )
                        }
                    ] + recent_messages + [
                        {
                            "role": "user",
                            "content": (
                                f"PDF context:\n{relevant_context}\n\n"
                                f"Question: {prompt}"
                            )
                        }
                    ]


        with st.spinner("Generating answer..."):
            result = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=messages,
                temperature=0.2,
                max_completion_tokens=800
            )


        response = result.choices[0].message.content


    st.session_state.messages.append({
        "role": "assistant",                        # Display and store assistant response
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)




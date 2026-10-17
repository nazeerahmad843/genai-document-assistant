#   Deployed Url
#   https://genai-document-assistant-jgthrfuevdzcoafj5atkap.streamlit.app/


import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
# import ollama
from google import genai


#------------------------model------------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")                              #embeding

model = load_model()

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
        <small>Python · Streamlit · Gemini API · RAG</small>
    </div>
    """,
    unsafe_allow_html=True
)



uploaded_file = st.sidebar.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    st.sidebar.success("PDF uploaded successfully!")
    st.write("Ask me a questions!!!")
    prompt = st.chat_input("Ask a question about your PDF...")
    chunks = []


#---------------------Pdf Extractor-------------------

    pdf_reader = PdfReader(uploaded_file)

    pdf_text = ""

    for page in pdf_reader.pages:
        text = page.extract_text()
        pdf_text = pdf_text + text + "\n"


    # st.sidebar.write("PDF text extracted successfully!")

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

    # st.sidebar.write("Chunking successfully!")

#----------------------Embeding------------------

    doc_chunk_vectors = model.encode(chunks)

#-----------------------Display all--------------------------

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

#-------------------------User---------------------------------

    # prompt = st.chat_input("Ask a question about your PDF...")

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

#-------------------------Bot with LLM---------------------------------

        if chunks:
            relevant_chunk = relavant_chunks(prompt,chunks,doc_chunk_vectors)
            client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
            with st.spinner("Generating answer... Please wait"):
                result = client.models.generate_content(
                                                            model="gemini-3.8-flash",
                                                            contents=(
                                                                "Answer the question using only the supplied "
                                                                "PDF context. If the answer is not present, "
                                                                "say you could not find it in the PDF.\n\n"
                                                                f"PDF context:\n{relevant_chunk}\n\n"
                                                                f"Question: {prompt}"
                                                            ),
                                                            config={
                                                                "temperature": 0.2,
                                                                "max_output_tokens": 1024
                                                            }
                                                        )

            response = result.text

                # result = ollama.chat(   
                #             model="llama3.2",
                #             messages=[
                #                         {
                #                             "role": "system",
                #                             "content": (
                #                                         "Answer the question using only the supplied "
                #                                         "PDF context. If the answer is not in the "
                #                                         "context, say you could not find it in the PDF."
                #                                         )
                #                         },
                #                         {
                #                             "role": "user",
                #                             "content": (
                #                                         f"PDF context:\n{relevant_chunk}\n\n"
                #                                         f"Question: {prompt}"
                #                                         )
                #                         }
                #                     ]
                #                     )
                # response = result["message"]["content"]


        # else:
        #     response = "Please upload a PDF first."

        st.session_state.messages.append({
            "role": "assistant",                        # Display and store assistant response
            "content": response
        })

        with st.chat_message("assistant"):
            st.write(response)

else:
    st.info("👈 Please upload a PDF first using the sidebar to start chatting.")
    st.stop()



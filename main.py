import os
import time
import streamlit as st

# LangChain & Groq Imports
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv

# Load environment variables (GROQ_API_KEY)
load_dotenv()

# --- 1. CONFIGURATION & UI SETUP ---
st.set_page_config(
    page_title="InsightStream: AI News Analyst",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        width: 100%;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .header-style {
        font-size: 24px;
        font-weight: bold;
        color: #333;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2965/2965358.png", width=50) # Placeholder icon
    st.title("InsightStream")
    st.markdown("---")
    st.subheader("🔗 News Sources")
    
    urls = []
    for i in range(3):
        url = st.text_input(f"Article URL {i+1}", placeholder="Paste URL here...")
        urls.append(url)

    st.markdown("---")
    process_url_clicked = st.button("🔄 Analyze & Process")
    
    st.markdown("### Status Log")
    status_container = st.empty()

# --- 3. MAIN LOGIC ---

# File path for FAISS index (saved locally)
folder_path = "faiss_index"

# Initialize Main Area
st.title("🧠 InsightStream: AI News Analyst")
st.markdown("Input news article URLs in the sidebar to generate insights using **Groq (Llama3)** and **LangChain**.")

# Logic for Processing URLs
if process_url_clicked:
    # Filter out empty strings
    valid_urls = [url for url in urls if url.strip()]
    
    if not valid_urls:
        st.error("Please enter at least one valid URL.")
    else:
        try:
            status_container.info("⏳ Loading data from URLs...")
            loader = UnstructuredURLLoader(urls=valid_urls)
            data = loader.load()

            status_container.info("⏳ Splitting text into chunks...")
            text_splitter = RecursiveCharacterTextSplitter(
                separators=['\n\n', '\n', '.', ','],
                chunk_size=1000
            )
            docs = text_splitter.split_documents(data)

            status_container.info("⏳ Generating Embeddings (HuggingFace)...")
            # Using HuggingFace embeddings (Free/Local) instead of OpenAI
            embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
            
            status_container.info("⏳ Building Vector Store...")
            vectorstore = FAISS.from_documents(docs, embeddings)

            # Save the FAISS index locally
            vectorstore.save_local(folder_path)

            status_container.success("✅ Analysis Complete! Ask a question.")
            time.sleep(2)
        except Exception as e:
            status_container.error(f"An error occurred: {e}")

# Logic for Querying
query = st.text_input("💬 Ask a question about the articles:", placeholder="e.g., What are the key takeaways from the news?")

if query:
    if os.path.exists(folder_path):
        with st.spinner("Generating answer..."):
            try:
                # 1. Load Embeddings
                embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
                
                # 2. Load Vector Store
                # Allow dangerous deserialization is required for pickle, but we use save_local which is safer.
                # However, LangChain updated FAISS loading recently.
                vectorstore = FAISS.load_local(folder_path, embeddings, allow_dangerous_deserialization=True)

                # 3. Initialize Groq LLM
                # Ensure GROQ_API_KEY is in your .env file
                llm = ChatGroq(
                    temperature=0, 
                    model_name="llama3-70b-8192"  # Or "mixtral-8x7b-32768"
                )

                # 4. Create Chain
                chain = RetrievalQAWithSourcesChain.from_llm(
                    llm=llm, 
                    retriever=vectorstore.as_retriever()
                )

                # 5. Get Result
                result = chain.invoke({"question": query})

                # --- RESULT DISPLAY UI ---
                st.markdown("### 💡 Answer")
                st.markdown(f">{result['answer']}")

                # Display sources elegantly
                sources = result.get("sources", "")
                if sources:
                    with st.expander("📚 View Sources"):
                        st.write(sources)
            
            except Exception as e:
                st.error(f"Error generating response: {e}")
    else:
        st.warning("⚠️ No data found. Please process URLs in the sidebar first.")
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS
from transformers import AutoTokenizer

def build_vectorstore(urls, embeddings, save_path):
    """
    Load articles from URLs, split into token-safe chunks, and build a FAISS vectorstore.
    """
    # Load documents from URLs
    loader = UnstructuredURLLoader(urls=urls)
    documents = loader.load()

    # Initialize tokenizer (use same model as embeddings)
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

    # Token-aware splitter
    splitter = RecursiveCharacterTextSplitter.from_hf_tokenizer(
        tokenizer=tokenizer,
        chunk_size=512,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", ","]
    )

    # Split documents into chunks
    docs = splitter.split_documents(documents)

    # Build FAISS vectorstore and save it locally
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(save_path)

    return True

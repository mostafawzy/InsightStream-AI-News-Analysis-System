# InsightStream – AI News Analyst

InsightStream is a lightweight **AI-powered news analysis application** that allows users to ingest online news articles and ask natural language questions over their content.
It uses **LangChain**, **Groq LLMs**, **Hugging Face embeddings**, and **FAISS** for retrieval-augmented generation (RAG), with a **Streamlit** UI.

---

## Features

* Load and analyze news articles directly from URLs
* Token-aware document chunking
* Semantic search using FAISS vector store
* Question answering with cited sources
* Clean and minimal Streamlit interface
* Fast inference powered by Groq (LLaMA 3.3)

---

## Tech Stack

* **Python 3.12**
* **Streamlit** – UI
* **LangChain** – RAG pipeline
* **Groq** – LLM inference
* **Hugging Face Transformers**
* **FAISS** – Vector database
* **Unstructured** – URL content loading

---

## Project Structure

```
3-InsightStream/
│
├── services/
│   ├── embeddings.py      # Hugging Face embedding model
│   ├── ingestion.py       # URL loading & FAISS indexing
│   └── qa.py              # Question answering pipeline
│
├── ui/
│   ├── layout.py          # Page setup
│   └── components.py     # Sidebar inputs
│
├── faiss_index/           # Stored vector index
├── main.py                # Streamlit entry point
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

---

## How It Works

1. **Input URLs**
   Users provide one or more news article URLs.

2. **Document Processing**
   Articles are loaded and split into token-safe chunks using the same tokenizer as the embedding model.

3. **Vector Store Creation**
   Chunks are embedded using `sentence-transformers/all-MiniLM-L6-v2` and stored in FAISS.

4. **Question Answering**
   User queries are answered using a retrieval-augmented pipeline with **LLaMA-3.3-70B (Groq)**, including source references.

---

## Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/mostafawzy/InsightStream-NewsAI.git
cd InsightStream-NewsAI
```

### 2. Install dependencies (using uv)

```bash
uv sync
```

### 3. Environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

> `.env` is ignored by Git for security reasons.

### 4. Run the app

```bash
streamlit run main.py
```

---

## Example Use Cases

* Analyze breaking news articles
* Compare perspectives across multiple sources
* Extract factual answers from long-form journalism
* Research support for analysts and students

---

## Notes

* FAISS index is stored locally in `faiss_index/`
* Re-running ingestion overwrites the existing index
* Designed for clarity, speed, and extensibility

---

## Author

**Mostafa Mohamed Fawzy**
AI Engineer – Generative AI & NLP

GitHub: [https://github.com/mostafawzy](https://github.com/mostafawzy)

LinkedIn: https://linkedin.com/in/mostafamfawzy

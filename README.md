# InsightStream — AI News Analyst

InsightStream is a lightweight Streamlit app that ingests news article URLs, builds a FAISS vectorstore of embeddings, and answers user questions over the ingested content using retrieval-augmented LLM workflows.

## Key features
- Ingest articles from provided URLs
- Token-aware text splitting for reliable chunking
- Build and persist a FAISS vectorstore of embeddings
- Ask questions and get answers with source references
- Modular structure: `ui/` for presentation, `services/` for data and model logic

## Requirements
- Python 3.9+
- Recommended packages (install via pip):
  pip install -r requirements.txt
  or
  pip install streamlit langchain openai transformers sentence-transformers faiss-cpu python-dotenv langchain-community

Note: FAISS installation may vary by platform. Use `faiss-cpu` on many Linux/Windows systems, or consult FAISS docs for alternatives.

## Setup
1. Clone or copy the project folder to your machine.
2. Create a `.env` file in the project root with at least:
   OPENAI_API_KEY=your_openai_api_key
3. Install dependencies (see Requirements).

## Run
From the project folder that contains `main.py`:
- Open a terminal and run:
  streamlit run main.py

If you have multiple `main.py` copies in subfolders, run the one for the app you want (for example `3-InsightStream/main.py`).

## Configuration
- INDEX_PATH: path for the saved FAISS index (default in code: `faiss_index`).
- UI styles and layout are in `ui/layout.py` and `ui/components.py`.
- Ingestion logic is in `services/ingestion.py`.
- QA and embedding helpers are in `services/qa.py` and `services/embeddings.py`.

## Development
- Keep UI concerns inside `ui/` and model/data logic inside `services/`.
- Add or update unit tests as files change.
- When updating dependencies, test FAISS and transformer behavior locally.

## Troubleshooting
- If index loading fails, rebuild by re-processing URLs in the sidebar.
- If OpenAI calls fail, verify `OPENAI_API_KEY` and network access.

## License
Add your preferred license or keep proprietary as desired.

# InsightStream — AI News Analyst

InsightStream is a compact Streamlit app that ingests news article URLs, builds a FAISS vectorstore of embeddings, and answers questions over the ingested content using retrieval-augmented LLM workflows.

## Quick start

1. Add credentials in a local `.env` (do not commit this file). Typical keys:
   - GROQ_API_KEY or OPENAI_API_KEY (depending on which provider you configure).

2. Install dependencies using your project tool (pyproject.toml is provided). If you use `uv` for dependency management and execution, run the app with:
   uv run streamlit run main.py

   Alternatively, use your preferred environment manager and run:
   streamlit run main.py

## Project layout
- ui/ — Streamlit UI, layout and components
- services/ — ingestion, embeddings, QA logic
- pyproject.toml & uv.lock — dependency metadata for your environment tool

## Configuration
- INDEX_PATH in code is `faiss_index` by default — change if required.
- Keep API keys in `.env` and ensure they are available to the process (dotenv is used).

## Notes
- FAISS may require platform-specific wheels (faiss-cpu is recommended for CPU setups).
- If the saved index becomes invalid, re-run ingestion via the sidebar to rebuild.

## Troubleshooting
- If embeddings or OpenAI/Groq calls fail, verify keys and network access.
- If Streamlit shows layout issues after CSS changes, restart the app and clear browser cache.

## License
Choose and add a license file if you intend to

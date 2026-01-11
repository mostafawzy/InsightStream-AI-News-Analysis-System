import os
import streamlit as st
from dotenv import load_dotenv

from ui.layout import setup_page
from ui.components import sidebar_inputs
from services.ingestion import build_vectorstore
from services.qa import answer_question
from services.embeddings import get_embeddings

load_dotenv()

INDEX_PATH = "faiss_index"

setup_page()

urls, process_clicked, status = sidebar_inputs()

# replace the simple title + markdown with a styled header
st.markdown(
    """
    <div style="display:flex;align-items:center;gap:16px;padding:18px;border-radius:12px;margin-bottom:18px;
                background:linear-gradient(90deg, rgba(14,165,233,0.06), rgba(124,58,237,0.04));
                box-shadow: 0 6px 18px rgba(12,74,110,0.06);">
            <div>
        <div style="font-size:20px;font-weight:700;color:#0f172a;">InsightStream: <span style="color:#7c3aed;">AI News Analyst</span></div>
        <div style="margin-top:4px;color:#64748b;">Analyze news articles using <strong>Groq + LangChain</strong>.</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if process_clicked:
    valid_urls = [u for u in urls if u.strip()]
    if not valid_urls:
        st.error("Please enter at least one URL.")
    else:
        status.info("Processing articles...")
        embeddings = get_embeddings()
        build_vectorstore(valid_urls, embeddings, INDEX_PATH)
        status.success("Analysis complete.")

query = st.text_input("Ask a question:")

if query and os.path.exists(INDEX_PATH):
    with st.spinner("Generating answer..."):
        embeddings = get_embeddings()
        result = answer_question(query, embeddings, INDEX_PATH)

        st.markdown("### Answer")
        st.markdown(f"> {result['answer']}")

        if result.get("sources"):
            with st.expander("Sources"):
                st.write(result["sources"])

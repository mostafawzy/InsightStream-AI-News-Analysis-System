import os
import streamlit as st
from dotenv import load_dotenv

from ui.layout import setup_page
from ui.components import (
    render_header,
    sidebar_inputs,
    render_answer,
    question_input,
)
from services.ingestion import build_vectorstore
from services.qa import answer_question
from services.embeddings import get_embeddings

load_dotenv()

INDEX_PATH = "faiss_index"


def main():
    setup_page()
    render_header()   

    urls, process_clicked, status = sidebar_inputs()

    if process_clicked:
        valid_urls = [u for u in urls if u.strip()]
        if not valid_urls:
            st.error("Please enter at least one valid URL.")
        else:
            status.info("Processing articles...")
            embeddings = get_embeddings()
            build_vectorstore(valid_urls, embeddings, INDEX_PATH)
            status.success("Analysis complete.")

    query, params = question_input()

    if query and os.path.exists(INDEX_PATH):
        with st.spinner("Generating answer..."):
            embeddings = get_embeddings()
            result = answer_question(query, embeddings, INDEX_PATH, **params)
            render_answer(result)


if __name__ == "__main__":
    main()

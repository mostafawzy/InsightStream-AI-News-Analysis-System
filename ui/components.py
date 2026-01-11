import streamlit as st

def render_header():
    st.markdown(
        """
        <style>
        /* ===============================
           Neutral example buttons
           =============================== */
        button[kind="secondary"] {
            background: #f8fafc !important;
            color: #0f172a !important;
            border: 1px solid #e2e8f0 !important;
        }

        button[kind="secondary"]:hover {
            background: #f1f5f9 !important;
        }

        /* ===============================
           Global header layout
           =============================== */
        .global-header {
            position: fixed;
            top: 10px;
            left: 0;
            right: 0;
            z-index: 1000;
            display: flex;
            justify-content: center;
            padding: 0 12px;
            pointer-events: none;
        }

        .global-bar {
            pointer-events: auto;
            width: calc(100% - 32px);
            max-width: none;
            border-radius: 18px;
            display: flex;
            align-items: center;
            gap: 18px;
            padding: 14px 22px;
            background: linear-gradient(
                90deg,
                rgba(14,165,233,0.10),
                rgba(124,58,237,0.06)
            );
            backdrop-filter: blur(8px);
            box-shadow: 0 10px 30px rgba(16,24,40,0.08);
            border: 1px solid rgba(230,238,246,0.9);
        }

        .global-logo {
            width: 56px;
            height: 56px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            background: linear-gradient(135deg,#0ea5e9,#7c3aed);
            color: white;
            box-shadow: 0 6px 20px rgba(12,74,110,0.12);
            flex-shrink: 0;
        }

        .global-title {
            font-size: 18px;
            font-weight: 700;
            color: #0f172a;
            margin: 0;
        }

        .global-subtitle {
            font-size: 13px;
            color: #64748b;
            margin-top: 2px;
        }

        /* ===============================
           Layout spacing
           =============================== */
        section[data-testid="stSidebar"] {
            margin-top: 96px;
            border-radius: 20px;       /* rounded corners */
            padding: 16px;             /* optional padding */
            background-color: #f9fafb; /* optional background */
            box-shadow: 0 4px 20px rgba(0,0,0,0.1); /* optional shadow */
        }

        [data-testid="stAppViewContainer"] .block-container {
            padding-top: 116px;
        }
        </style>

        <div class="global-header">
            <div class="global-bar">
                <div class="global-logo">📰</div>
                <div>
                    <div class="global-title">
                        InsightStream <span style="color:#7c3aed;">AI News Analyst</span>
                    </div>
                    <div class="global-subtitle">
                        Groq · LangChain · Retrieval-Augmented Generation
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def sidebar_inputs():
    with st.sidebar:
       
        st.markdown("<p style='font-weight:600;'>News Sources</p>", unsafe_allow_html=True)

        urls = [
            st.text_input(
                label=f"Article URL {i+1}",
                placeholder="https://news-site.com/article",
                label_visibility="collapsed",
            )
            for i in range(3)
        ]

        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        st.markdown(
            "<p class='muted'>Paste full article URLs (max 3).</p>",
            unsafe_allow_html=True,
        )

        process_clicked = st.button("Analyze Articles")
        status = st.empty()

    return urls, process_clicked, status


def render_answer(result: dict):
    st.markdown("### Answer")
    st.markdown(
        f"""
        <div class="result-answer">
            <p>{result['answer']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if result.get("sources"):
        with st.expander("Sources"):
            st.write(result["sources"])


def question_input():
    st.markdown("### Ask about the articles")

    examples = [
        "Summarize the article in 3 bullets.",
        "What are the key facts and claims?",
        "Is there any noticeable bias?",
    ]

    cols = st.columns(len(examples))
    for i, ex in enumerate(examples):
        if cols[i].button(
            ex,
            key=f"example_{i}",
            type="secondary"   # ← important
        ):
            st.session_state["query"] = ex

    query = st.text_area(
        label="Your question",
        value=st.session_state.get("query", ""),
        placeholder="e.g. What are the main arguments and who supports them?",
        height=100,
    )

    with st.expander("Advanced (optional)"):
        top_k = st.slider(
            "Number of retrieved chunks",
            1,
            10,
            4,
            help="Higher values may improve coverage but increase noise.",
        )

    ask_clicked = st.button("Get Answer", type="primary")

    if ask_clicked and query.strip():
        return query.strip(), {"top_k": top_k}

    return None, {}

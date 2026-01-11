import streamlit as st

def render_header():
    st.markdown(
        """
        <div style="display:flex;align-items:center;gap:16px;padding:18px;border-radius:12px;margin-bottom:18px;
                    background:linear-gradient(90deg, rgba(14,165,233,0.06), rgba(124,58,237,0.04));
                    box-shadow: 0 6px 18px rgba(12,74,110,0.06);">
          <div style="width:56px;height:56px;border-radius:10px;display:flex;align-items:center;justify-content:center;
                      font-size:26px;background:linear-gradient(135deg,#0ea5e9,#7c3aed);color:#fff;">📰</div>
          <div>
            <div style="font-size:20px;font-weight:700;color:#0f172a;">InsightStream: <span style="color:#7c3aed;">AI News Analyst</span></div>
            <div style="margin-top:4px;color:#64748b;">Analyze news articles using <strong>Groq + LangChain</strong>.</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def sidebar_inputs():
    with st.sidebar:
        st.markdown(
            """
            <div class="app-topbar">
                <div class="app-logo">📰</div>
                <div>
                    <div class="app-title">InsightStream</div>
                    <div class="app-subtitle">AI News Intelligence</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown("<p style='margin:0;font-weight:600;'>News Sources</p>", unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

        urls = [
            st.text_input(
                label=f"Article URL {i+1}",
                placeholder="https://news-site.com/article",
                label_visibility="collapsed"
            )
            for i in range(3)
        ]

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

        st.markdown("<p class='muted' style='margin-top:8px;'>Tip: paste full article URLs; you can add up to 3 at once.</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

        process_clicked = st.button("Analyze Articles")

        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
        st.markdown("<p class='muted'>Processing status</p>", unsafe_allow_html=True)
        status = st.empty()

    return urls, process_clicked, status
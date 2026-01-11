import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="InsightStream · AI News Analyst",
        page_icon="📰",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown("""
        <style>
        :root{
            /* Palette */
            --bg: #f5f7fb;
            --surface: #ffffff;
            --primary: #0ea5e9;      /* sky */
            --primary-600: #0284c7;
            --accent: #7c3aed;       /* violet */
            --muted: #64748b;
            --text: #0f172a;
            --border: #e6eef6;
            --card-shadow: rgba(16,24,40,0.06);

            /* Main area subtle color */
            --main-bg: linear-gradient(180deg, rgba(14,165,233,0.03), rgba(124,58,237,0.02));
        }

        /* Global / base */
        html, body, [class*="css"] {
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
            color: var(--text);
            background: var(--bg);
        }

        /* App main container */
        [data-testid="stAppViewContainer"] {
            padding: 20px 28px;
            background: var(--main-bg);
        }
        .block-container {
            padding: 18px 24px 24px 24px;
        }

        /* Header / titles */
        .stMarkdown h1, .stMarkdown h2 {
            color: var(--primary);
            font-weight: 700;
            margin: 0 0 8px 0;
        }
        .stMarkdown h3 { color: var(--text); }

        /* Top bar */
        .app-topbar {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 14px 20px;
            border-radius: 12px;
            margin-bottom: 18px;
            background: linear-gradient(90deg, rgba(14,165,233,0.08), rgba(124,58,237,0.04));
            box-shadow: 0 6px 18px var(--card-shadow);
        }
        .app-logo {
            width:48px;
            height:48px;
            border-radius:10px;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:22px;
            background: linear-gradient(135deg,var(--primary),var(--accent));
            color: #fff;
            box-shadow: 0 6px 18px rgba(12,74,110,0.12);
        }
        .app-title { font-size:18px; font-weight:700; margin:0; }
        .app-subtitle { margin:0; color:var(--muted); font-size:13px; }

        /* Keep Streamlit's top toolbar/header without a colored background */
        header,
        header > div[role="banner"],
        div[data-testid="stToolbar"],
        div[data-testid="stHeader"],
        #MainMenu {
            background: transparent !important;
            box-shadow: none !important;
            color: inherit !important;
        }
        header svg, header button, header div, header span {
            color: inherit !important;
            fill: currentColor !important;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: var(--surface);
            border-right: 1px solid var(--border);
            padding: 18px;
            width: 320px;
        }

        /* Cards */
        .card {
            background: var(--surface);
            border-radius: 12px;
            padding: 16px;
            border: 1px solid var(--border);
            box-shadow: 0 6px 18px var(--card-shadow);
            margin-bottom:16px;
        }

        /* Inputs */
        .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>select {
            border-radius: 8px;
            border: 1px solid var(--border) !important;
            padding: 10px 12px;
            background: linear-gradient(180deg, #ffffff, #fbfdff);
        }
        .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
            outline: none;
            box-shadow: 0 0 0 4px rgba(14,165,233,0.08);
            border-color: var(--primary) !important;
        }

        /* Buttons - match app-logo / app-topbar accent */
        .stButton>button {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: #fff;
            border-radius: 10px;
            padding: 10px 16px;
            height:44px;
            font-weight:600;
            border: none;
            box-shadow: 0 8px 20px rgba(12,74,110,0.14);
        }
        .stButton>button:hover {
            opacity:0.98;
            transform: translateY(-1px);
            transition: all 0.12s ease;
            filter: brightness(1.03);
        }

        /* Divider & muted */
        .divider { height:1px; background:var(--border); margin:12px 0; border-radius:1px; }
        .muted { color:var(--muted); font-size:13px; }

        /* Result styling */
        .result-answer {
            background: linear-gradient(180deg, rgba(255,255,255,0.6), rgba(255,255,255,0.95));
            border-radius: 12px;
            padding: 16px;
            border: 1px solid var(--border);
        }

        /* Expander header tweak */
        .stExpanderHeader { font-weight:600; }

        /* small responsive touch */
        @media (max-width: 880px) {
            section[data-testid="stSidebar"] { width: 100% !important; }
        }
        </style>
    """, unsafe_allow_html=True)
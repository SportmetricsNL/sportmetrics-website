from __future__ import annotations

import streamlit as st


NAV_ITEMS = [
    ("Home", "app.py"),
    ("VO2max", "pages/1_VO2max.py"),
    ("VT1", "pages/2_VT1.py"),
    ("VT2", "pages/3_VT2.py"),
    ("Energiesystemen", "pages/4_Energiesystemen.py"),
    ("Zonemodellen", "pages/5_Zonemodellen.py"),
    ("Critical Power", "pages/6_Critical_Power.py"),
    ("Mijn SportTesting AI", "pages/7_Mijn_SportTesting_AI.py"),
]


def inject_global_css() -> None:
    st.markdown(
        """
        <style>
          @import url("https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap");

          :root {
            --sm-bg: #f4f7f8;
            --sm-surface: #ffffff;
            --sm-ink: #1f363d;
            --sm-muted: #5b747d;
            --sm-accent: #2f7c85;
            --sm-accent-soft: #e3eff1;
            --sm-border: #d6e1e4;
            --sm-shadow: 0 12px 30px rgba(23, 67, 82, 0.1);
          }

          html, body, [class*="st-"] {
            font-family: "Manrope", sans-serif;
            color: var(--sm-ink);
          }

          [data-testid="stSidebar"],
          [data-testid="stSidebarNav"],
          [data-testid="stSidebarCollapsedControl"],
          [data-testid="stToolbar"],
          [data-testid="stDecoration"],
          [data-testid="stStatusWidget"],
          #MainMenu,
          header,
          footer {
            display: none !important;
          }

          [data-testid="stAppViewContainer"] {
            background:
              radial-gradient(circle at 10% 10%, #ffffff 0%, transparent 36%),
              radial-gradient(circle at 85% -5%, #e8f1f3 0%, transparent 44%),
              var(--sm-bg);
          }

          [data-testid="stAppViewContainer"] > .main {
            padding-top: 0;
          }

          .block-container {
            max-width: 1180px;
            padding-top: 1.2rem;
            padding-bottom: 3rem;
            padding-left: 1.25rem;
            padding-right: 1.25rem;
          }

          div[data-testid="stPageLink"] {
            width: 100%;
          }

          div[data-testid="stPageLink"] a {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 2.65rem;
            width: 100%;
            border-radius: 999px;
            border: 1px solid var(--sm-border);
            background: var(--sm-surface);
            color: var(--sm-muted);
            text-decoration: none;
            font-weight: 600;
            letter-spacing: 0.01em;
            box-shadow: 0 4px 14px rgba(24, 56, 70, 0.06);
            transition: all 0.2s ease;
          }

          div[data-testid="stPageLink"] a:hover {
            border-color: var(--sm-accent);
            color: var(--sm-accent);
            transform: translateY(-1px);
          }

          div[data-testid="stPageLink"] a[aria-current="page"],
          div[data-testid="stPageLink"] a[aria-disabled="true"] {
            border-color: var(--sm-accent);
            background: linear-gradient(135deg, var(--sm-accent) 0%, #3f97a2 100%);
            color: #ffffff;
            box-shadow: var(--sm-shadow);
            opacity: 1;
            pointer-events: none;
          }

          .sm-nav-space {
            height: 0.6rem;
          }

          @media (max-width: 1180px) {
            .block-container {
              max-width: 100%;
            }

            div[data-testid="stPageLink"] a {
              min-height: 2.45rem;
              font-size: 0.9rem;
            }
          }

          @media (max-width: 900px) {
            div[data-testid="stPageLink"] a {
              min-height: 2.3rem;
              font-size: 0.8rem;
              padding: 0 0.45rem;
            }
          }
        </style>
        """,
        unsafe_allow_html=True,
    )


def top_nav(active: str) -> None:
    columns = st.columns(len(NAV_ITEMS), gap="small")
    for col, (label, page) in zip(columns, NAV_ITEMS):
        with col:
            st.page_link(page=page, label=label, disabled=(label == active))
    st.markdown('<div class="sm-nav-space"></div>', unsafe_allow_html=True)

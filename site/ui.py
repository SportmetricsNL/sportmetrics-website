from __future__ import annotations

import base64
import mimetypes
from pathlib import Path

import streamlit as st


@st.cache_data(show_spinner=False)
def file_b64(path: str) -> str:
    return base64.b64encode(Path(path).read_bytes()).decode("utf-8")

NAV_ITEMS = [
    ("Home", "app.py"),
    ("Aanbod", "pages/8_Aanbod.py"),
    ("Methode", "pages/9_Methode.py"),
    ("VO2max", "pages/1_VO2max.py"),
    ("VT1", "pages/2_VT1.py"),
    ("VT2", "pages/3_VT2.py"),
    ("Energiesystemen", "pages/4_Energiesystemen.py"),
    ("Zonemodellen", "pages/5_Zonemodellen.py"),
    ("Critical Power", "pages/6_Critical_Power.py"),
    ("Mijn SportTesting AI", "pages/7_Mijn_SportTesting_AI.py"),
]


def _is_mobile_client() -> bool:
    try:
        ua = st.context.headers.get("User-Agent", "")
    except Exception:
        return False
    ua_lower = ua.lower()
    return any(token in ua_lower for token in ("mobile", "android", "iphone", "ipad"))


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
            min-height: 2.3rem;
            width: 100%;
            border-radius: 999px;
            border: 1px solid var(--sm-border);
            background: rgba(255, 255, 255, 0.9);
            color: var(--sm-muted);
            text-decoration: none;
            font-weight: 600;
            letter-spacing: 0.01em;
            font-size: 0.76rem;
            white-space: normal;
            overflow: visible;
            text-overflow: clip;
            text-align: center;
            line-height: 1.18;
            padding: 0.18rem 0.48rem;
            box-shadow: 0 3px 9px rgba(24, 56, 70, 0.05);
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
            height: 0.32rem;
          }

          .sm-nav-row-space {
            height: 0.3rem;
          }

          .sm-logo-wrap {
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            padding-top: 0.1rem;
          }

          .sm-mobile-menu {
            margin-top: 0.2rem;
          }

          @media (max-width: 1180px) {
            .block-container {
              max-width: 100%;
            }

            div[data-testid="stPageLink"] a {
              min-height: 2.2rem;
              font-size: 0.73rem;
            }
          }

          @media (max-width: 900px) {
            div[data-testid="stPageLink"] a {
              min-height: 2.1rem;
              font-size: 0.68rem;
              padding: 0.16rem 0.34rem;
            }

            .sm-nav-row-space {
              height: 0.22rem;
            }
          }

          @media (max-width: 600px) {
            .block-container {
              padding-left: 0.72rem;
              padding-right: 0.72rem;
              padding-bottom: 2rem;
            }

            div[data-testid="stPageLink"] a {
              min-height: 2.18rem;
              font-size: 0.7rem;
              padding: 0.18rem 0.36rem;
            }
          }
        </style>
        """,
        unsafe_allow_html=True,
    )


def top_nav(active: str) -> None:
    logo_path = Path(__file__).resolve().parents[1] / "assets" / "logo.png"
    logo_uri = ""
    if logo_path.exists():
        mime_type, _ = mimetypes.guess_type(logo_path.name)
        if mime_type is None:
            mime_type = "image/png"
        payload = base64.b64encode(logo_path.read_bytes()).decode("utf-8")
        logo_uri = f"data:{mime_type};base64,{payload}"
    logo_col, nav_col = st.columns([0.14, 0.86], gap="small")

    with logo_col:
        st.markdown('<div class="sm-logo-wrap">', unsafe_allow_html=True)
        if logo_uri:
            st.markdown(
                f'<img src="{logo_uri}" alt="SportMetrics logo" style="width: 112px; height: auto; image-rendering: -webkit-optimize-contrast; image-rendering: crisp-edges;" />',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    with nav_col:
        if _is_mobile_client():
            labels = [label for label, _ in NAV_ITEMS]
            current_index = labels.index(active) if active in labels else 0
            st.markdown('<div class="sm-mobile-menu">', unsafe_allow_html=True)
            selected = st.selectbox("Menu", labels, index=current_index, label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
            if selected != active:
                page_map = {label: page for label, page in NAV_ITEMS}
                st.switch_page(page_map[selected])
        else:
            row_size = 5
            for row_start in range(0, len(NAV_ITEMS), row_size):
                row_items = NAV_ITEMS[row_start : row_start + row_size]
                weights = [1.15 if label == "Mijn SportTesting AI" else 1.0 for label, _ in row_items]
                columns = st.columns(weights, gap="small")
                for col, (label, page) in zip(columns, row_items):
                    with col:
                        st.page_link(page=page, label=label, disabled=(label == active), width="stretch")
                if row_start + row_size < len(NAV_ITEMS):
                    st.markdown('<div class="sm-nav-row-space"></div>', unsafe_allow_html=True)

    st.markdown('<div class="sm-nav-space"></div>', unsafe_allow_html=True)

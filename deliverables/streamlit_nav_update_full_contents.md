## site/ui.py
```python
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
```

## app.py
```python
import importlib.util
import sys
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="SportMetrics",
    layout="wide",
)

if "site.ui" not in sys.modules:
    ui_path = Path(__file__).resolve().parent / "site" / "ui.py"
    spec = importlib.util.spec_from_file_location("site.ui", ui_path)
    if spec is None or spec.loader is None:
        raise ImportError("Kon site.ui niet laden")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules["site.ui"] = module

from site.ui import inject_global_css, top_nav

inject_global_css()
top_nav(active="Home")

st.markdown(
    """
    <style>
      .home-hero {
        margin-top: 0.3rem;
      }

      .home-title {
        margin: 0.2rem 0 0.2rem 0;
        font-size: clamp(2.1rem, 4.6vw, 3.3rem);
        line-height: 1.04;
        letter-spacing: -0.02em;
        color: #173f49;
      }

      .home-subtitle {
        margin: 0;
        font-size: 1.26rem;
        color: #2f7c85;
        font-weight: 700;
      }

      .home-line {
        margin-top: 0.9rem;
        margin-bottom: 0.9rem;
        color: #2f5963;
        font-weight: 600;
      }

      .home-text {
        margin: 0.4rem 0;
        color: #315761;
        max-width: 720px;
        line-height: 1.65;
      }

      .home-image-wrap {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.9), rgba(223, 237, 239, 0.9));
        border: 1px solid #d5e2e5;
        border-radius: 1.35rem;
        padding: 0.7rem;
        box-shadow: 0 18px 34px rgba(25, 67, 81, 0.14);
      }

      .home-section-title {
        margin-top: 2.4rem;
        margin-bottom: 0.85rem;
        font-size: 1.5rem;
        color: #173f49;
      }

      .home-card {
        background: #ffffff;
        border: 1px solid #d4e0e4;
        border-radius: 1.15rem;
        padding: 1.2rem 1.25rem;
        box-shadow: 0 10px 24px rgba(23, 67, 82, 0.08);
        height: 100%;
      }

      .home-card h3 {
        margin-top: 0;
        margin-bottom: 0.45rem;
        color: #1f4f5a;
      }

      .home-card p {
        margin-bottom: 0;
        color: #355e68;
        line-height: 1.6;
      }

      .home-profile {
        list-style: none;
        margin: 0;
        padding: 0;
      }

      .home-profile li {
        padding: 0.58rem 0;
        border-bottom: 1px solid #e5edef;
        color: #315761;
      }

      .home-profile li:last-child {
        border-bottom: none;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="home-hero">', unsafe_allow_html=True)
hero_left, hero_right = st.columns([1.1, 1.0], gap="large")

with hero_left:
    st.image("assets/logo.png", width=170)
    st.markdown('<h1 class="home-title">Meten is weten</h1>', unsafe_allow_html=True)
    st.markdown('<p class="home-subtitle">Train slim met jouw data</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="home-line">VO2Max, drempelwaardes, zones, energieverdeling, efficientie en meer</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="home-text">Ontdek de inspanningstesten van SportMetrics. Opgezet voor alle sporters die meer willen weten over hun eigen kunnen en waar hun grenzen liggen.</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="home-text">Wetenschappelijk onderbouwd, persoonlijk en professioneel uitgevoerd.</p>',
        unsafe_allow_html=True,
    )
    st.link_button("Plan je bezoek vandaag nog", "mailto:info@sportmetrics.nl", type="primary")

with hero_right:
    st.markdown('<div class="home-image-wrap">', unsafe_allow_html=True)
    st.image("assets/hero.jpg", width="stretch")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<h2 class="home-section-title">Locatie</h2>', unsafe_allow_html=True)
locatie_col_1, locatie_col_2 = st.columns(2, gap="large")

with locatie_col_1:
    st.markdown(
        """
        <div class="home-card">
          <h3>Ed Marnix (Amsterdam)</h3>
          <p>Persoonlijke testafname op een vaste rustige locatie met directe interpretatie.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with locatie_col_2:
    st.markdown(
        """
        <div class="home-card">
          <h3>Aan huis</h3>
          <p>Beschikbaar mits bezit fietstrainer met bluetooth en wattage meter.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<h2 class="home-section-title">Diensten</h2>', unsafe_allow_html=True)
diensten_left, diensten_right = st.columns([1.35, 0.65], gap="large")

with diensten_left:
    st.markdown(
        """
        <div class="home-card">
          <h3>Inspanningstesten</h3>
          <p>Meten is weten. Ontdek jouw VO₂max, je metabole profiel en energieverdeling via wetenschappelijk onderbouwde inspanningstesten.
          Voor sporters die gericht willen trainen en progressie inzichtelijk willen maken.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with diensten_right:
    st.markdown(
        """
        <div class="home-card">
          <h3>Direct verder</h3>
          <p>Bekijk de pagina met uitleg over de VO2max-test en toepassing in jouw trainingsplan.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link("pages/1_VO2max.py", label="Naar VO2max")

st.markdown('<h2 class="home-section-title">Wie ben ik</h2>', unsafe_allow_html=True)
profiel_col, achtergrond_col = st.columns([1.0, 1.0], gap="large")

with profiel_col:
    st.markdown(
        """
        <div class="home-card">
          <h3>Folkert Vinke</h3>
          <ul class="home-profile">
            <li>Fysiotherapeut</li>
            <li>BIG: 49936591804</li>
            <li>Gespecialiseerd & geaccrediteerd in inspanningsfysiologie</li>
            <li>MSc Student Gezondheidswetenschappen</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with achtergrond_col:
    st.markdown(
        """
        <div class="home-card">
          <h3>Werkwijze</h3>
          <p>Elke test wordt vertaald naar heldere trainingszones, concrete adviezen en een praktische aanpak die past bij je sportdoel.
          Je krijgt inzicht in belasting, herstel en progressie op basis van objectieve data.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
```

## pages/1_VO2max.py
```python
import importlib.util
import sys
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="VO2max - SportMetrics",
    layout="wide",
)

if "site.ui" not in sys.modules:
    ui_path = Path(__file__).resolve().parents[1] / "site" / "ui.py"
    spec = importlib.util.spec_from_file_location("site.ui", ui_path)
    if spec is None or spec.loader is None:
        raise ImportError("Kon site.ui niet laden")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules["site.ui"] = module

from site.ui import inject_global_css, top_nav

inject_global_css()
top_nav(active="VO2max")

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "logo.png"
if not LOGO_PATH.exists():
    LOGO_PATH = BASE_DIR / "1.png"

logo_data_uri = ""
if LOGO_PATH.exists():
    logo_b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    logo_data_uri = f"data:image/png;base64,{logo_b64}"

HARD_IMAGE_PATH = BASE_DIR / "hoe-hard-je-bent.png"
if not HARD_IMAGE_PATH.exists():
    HARD_IMAGE_PATH = BASE_DIR / "hoe-hard-je-bent.jpg"

hard_image_uri = ""
if HARD_IMAGE_PATH.exists():
    hard_b64 = base64.b64encode(HARD_IMAGE_PATH.read_bytes()).decode("utf-8")
    mime = "image/png"
    if HARD_IMAGE_PATH.suffix.lower() in {".jpg", ".jpeg"}:
        mime = "image/jpeg"
    hard_image_uri = f"data:{mime};base64,{hard_b64}"

HTML_PAGE = r"""
<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>VO2max - SportMetrics</title>
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Spectral:wght@400;600&display=swap");

    :root {
      --sand: #f6f1ea;
      --clay: #e9ddd2;
      --ink: #1e2a2f;
      --muted: #5c6b73;
      --sea: #2f7c85;
      --deep: #0f4c5c;
      --sun: #f4b66a;
      --peach: #f1c9a9;
      --card: #fffdf6;
      --card-strong: #ffffff;
      --border: rgba(30, 42, 47, 0.12);
      --shadow: 0 18px 50px rgba(15, 76, 92, 0.18);
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: "Spectral", "Times New Roman", serif;
      color: var(--ink);
      background: radial-gradient(1200px 800px at 10% -10%, #ffffff 0%, var(--sand) 60%, var(--clay) 100%);
    }

    .logo-pattern {
      position: fixed;
      inset: 0;
      background-image: url('{{LOGO_DATA_URI}}');
      background-repeat: repeat;
      background-position: center;
      background-size: 140px;
      opacity: 0.07;
      mix-blend-mode: multiply;
      pointer-events: none;
      z-index: 1;
    }

    .bg-shape {
      position: fixed;
      inset: auto;
      width: 480px;
      height: 480px;
      border-radius: 50%;
      background: radial-gradient(circle at 30% 30%, rgba(47, 124, 133, 0.28), rgba(47, 124, 133, 0.02));
      z-index: -1;
    }
    .bg-shape.one { top: -120px; right: -120px; }
    .bg-shape.two { bottom: -200px; left: -140px; background: radial-gradient(circle, rgba(244, 182, 106, 0.35), rgba(244, 182, 106, 0.02)); }

    nav {
      position: fixed;
      top: 28px;
      right: 26px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 14px 14px;
      box-shadow: var(--shadow);
      z-index: 4;
      max-width: 190px;
    }
    nav h4 {
      margin: 0 0 6px;
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
    }
    .nav-link {
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-decoration: none;
      color: var(--muted);
      display: flex;
      gap: 6px;
      align-items: center;
      transition: color 0.2s ease;
    }
    .nav-link span {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--clay);
      border: 1px solid var(--border);
    }
    .nav-link.active { color: var(--deep); font-weight: 600; }
    .nav-link.active span { background: var(--sea); border-color: var(--sea); }

    .progress {
      height: 6px;
      background: rgba(47, 124, 133, 0.12);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 6px;
    }
    .progress span { display: block; height: 100%; width: 0%; background: var(--sea); transition: width 0.2s ease; }

    main {
      position: relative;
      z-index: 3;
      max-width: 1100px;
      margin: 0 auto;
      padding: 64px 24px 120px;
    }

    section {
      margin: 0 0 72px;
      padding: 36px;
      border-radius: 26px;
      background: var(--card);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      transition: all 0.7s ease;
    }
    body.enable-animations section { opacity: 0; transform: translateY(20px); }
    body.enable-animations section.in-view { opacity: 1; transform: translateY(0); }

    .hero {
      padding: 54px 44px;
      background: linear-gradient(140deg, #ffffff, #f6e7d6);
    }
    .hero h1 {
      font-family: "Space Grotesk", sans-serif;
      font-size: clamp(2.2rem, 3.4vw, 3.4rem);
      margin: 0 0 12px;
      color: var(--deep);
    }
    .hero p {
      font-size: 1.05rem;
      color: var(--muted);
      margin: 0;
      max-width: 720px;
    }
    .hero .hero-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
      margin-top: 28px;
    }
    .hero .stat {
      padding: 16px 18px;
      background: var(--card-strong);
      border-radius: 16px;
      border: 1px solid var(--border);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.95rem;
      color: var(--muted);
    }
    .hero .stat strong { display: block; color: var(--deep); font-size: 1.1rem; }

    h2 {
      font-family: "Space Grotesk", sans-serif;
      margin: 0 0 12px;
      color: var(--deep);
      font-size: 1.8rem;
    }
    h3 {
      font-family: "Space Grotesk", sans-serif;
      margin: 0 0 8px;
      color: var(--deep);
    }
    p { margin: 0 0 14px; color: var(--ink); line-height: 1.55; }
    .muted { color: var(--muted); }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
    }
    .card {
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 16px 18px;
    }
    .pill {
      display: inline-block;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.72rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: 999px;
      margin-bottom: 10px;
    }

    .slider-box {
      margin-top: 18px;
      padding: 18px;
      border-radius: 18px;
      border: 1px dashed rgba(47, 124, 133, 0.4);
      background: #eef5f4;
    }
    .slider-box label {
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
    }
    .slider-box input[type="range"] { width: 100%; margin: 10px 0 6px; }
    .mix-row {
      display: grid;
      grid-template-columns: 130px 1fr 54px;
      gap: 12px;
      align-items: center;
      margin: 10px 0;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.85rem;
    }
    .mix-bar {
      background: #eef5f4;
      border-radius: 999px;
      overflow: hidden;
      height: 10px;
      border: 1px solid rgba(15, 76, 92, 0.2);
    }
    .mix-bar span {
      display: block;
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--sea), var(--deep));
      border-radius: 999px;
      transition: width 0.3s ease;
    }
    .mix-value { text-align: right; color: var(--muted); }

    .callout {
      background: #f3e4d2;
      border: 1px solid #e8cfae;
      padding: 16px 18px;
      border-radius: 18px;
      font-family: "Space Grotesk", sans-serif;
    }

    .tab-list {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin: 12px 0 18px;
    }
    .tab-btn {
      border: 1px solid var(--border);
      background: var(--card-strong);
      font-family: "Space Grotesk", sans-serif;
      padding: 8px 14px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .tab-btn.active { background: var(--deep); color: #fff; border-color: var(--deep); }
    .tab-panel { display: none; }
    .tab-panel.active { display: block; }

    .fatigue-controls {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin: 14px 0 18px;
    }
    .fatigue-btn {
      border: 1px solid var(--border);
      background: var(--card-strong);
      font-family: "Space Grotesk", sans-serif;
      padding: 8px 14px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .fatigue-btn.active { background: var(--deep); color: #fff; border-color: var(--deep); }

    .chain-track {
      display: grid;
      grid-template-columns: minmax(90px, 1fr) 28px minmax(110px, 1fr) 28px minmax(90px, 1fr);
      align-items: center;
      gap: 10px;
      margin: 12px 0 8px;
    }
    .chain-node {
      padding: 12px 10px;
      border-radius: 14px;
      border: 1px solid var(--border);
      background: var(--card-strong);
      font-family: "Space Grotesk", sans-serif;
      text-align: center;
      font-size: 0.9rem;
    }
    .chain-node.active {
      background: #eef5f4;
      border-color: rgba(47, 124, 133, 0.35);
      color: var(--deep);
      box-shadow: 0 10px 24px rgba(47, 124, 133, 0.12);
    }
    .chain-arrow {
      font-family: "Space Grotesk", sans-serif;
      font-size: 1.1rem;
      color: var(--muted);
      text-align: center;
    }
    .genetics-pill {
      display: inline-block;
      margin-top: 8px;
      padding: 6px 12px;
      border-radius: 999px;
      border: 1px dashed rgba(47, 124, 133, 0.35);
      background: #eef5f4;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.8rem;
      color: var(--deep);
    }
    .genetics-pill.active {
      border-color: rgba(47, 124, 133, 0.6);
      background: #dfeeee;
    }

    .interval-strip {
      display: grid;
      grid-template-columns: repeat(7, minmax(70px, 1fr));
      gap: 10px;
      margin-top: 16px;
    }
    .interval-block {
      border-radius: 14px;
      padding: 12px 10px;
      text-align: center;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.8rem;
      border: 1px solid var(--border);
    }
    .interval-work {
      background: var(--deep);
      color: #fff;
      border-color: var(--deep);
    }
    .interval-rest {
      background: #f3e4d2;
      color: var(--ink);
      border-color: #e8cfae;
    }

    .quote-image {
      width: 100%;
      height: auto;
      display: block;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: #ffffff;
    }
    .image-fallback {
      margin-top: 8px;
      color: var(--muted);
      font-size: 0.9rem;
    }

    .summary-list {
      margin: 0;
      padding-left: 18px;
    }
    .summary-list li {
      margin: 0 0 10px;
    }

    .footer {
      text-align: center;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
      color: var(--muted);
    }

    @media (max-width: 980px) {
      nav { display: none; }
      section { padding: 28px; }
      .mix-row { grid-template-columns: 110px 1fr 48px; }
    }

    @media (max-width: 720px) {
      main { padding: 40px 16px 90px; }
      section { padding: 18px; margin: 0 0 36px; }
      .hero { padding: 24px 18px; }
      .hero h1 { font-size: clamp(1.8rem, 6vw, 2.4rem); }
      .hero .hero-grid { grid-template-columns: 1fr; }
      .grid-3 { grid-template-columns: 1fr; }
      .mix-row { grid-template-columns: 1fr; gap: 6px; }
      .mix-value { text-align: left; }
      .tab-btn { width: 100%; text-align: center; }
      .fatigue-btn { width: 100%; text-align: center; }
      .chain-track { grid-template-columns: 1fr; }
      .chain-arrow { display: none; }
      .interval-strip { grid-template-columns: repeat(2, minmax(110px, 1fr)); }
      .card { padding: 14px; }
    }

    @media (prefers-reduced-motion: reduce) {
      * { scroll-behavior: auto; }
      section { transition: none; }
      body.enable-animations section { opacity: 1; transform: none; }
    }
  </style>
</head>
<body>
  <div class="logo-pattern" aria-hidden="true"></div>
  <div class="bg-shape one"></div>
  <div class="bg-shape two"></div>

  <nav aria-label="Navigatie">
    <h4>Route</h4>
    <a class="nav-link" href="#intro" data-section="intro"><span></span>Intro</a>
    <a class="nav-link" href="#definitie" data-section="definitie"><span></span>Definitie</a>
    <a class="nav-link" href="#keten" data-section="keten"><span></span>Keten</a>
    <a class="nav-link" href="#trainen" data-section="trainen"><span></span>Trainen</a>
    <a class="nav-link" href="#zone2" data-section="zone2"><span></span>Zone 2</a>
    <a class="nav-link" href="#meten" data-section="meten"><span></span>Meten</a>
    <a class="nav-link" href="#sportmetrics" data-section="sportmetrics"><span></span>SportMetrics</a>
    <a class="nav-link" href="#samenvatting" data-section="samenvatting"><span></span>Samenvatting</a>
    <div class="progress"><span id="progress-bar"></span></div>
  </nav>

  <main>
    <section id="intro" class="hero" data-title="Intro">
      <span class="pill">VO2max</span>
      <h1>VO2max: de gouden standaard, maar meer dan hard gaan</h1>
      <p>VO2max is je maximale zuurstofopname: hoeveel O2 je per minuut kunt opnemen, transporteren en gebruiken om ATP te maken. Het is je aerobe plafond. Niet de enige voorspeller van prestatie, maar wel een kernanker in je fysiologisch profiel.</p>
      <div class="hero-grid">
        <div class="stat"><strong>Aerobe plafond</strong>Maximale O2-opname bepaalt hoe hoog je aerobe motor kan.</div>
        <div class="stat"><strong>Niet alles</strong>Zelfde VO2max kan anders presteren door drempels, efficiency en pacing.</div>
        <div class="stat"><strong>Trainbaar</strong>Je kunt het plafond verhogen door slim te doseren.</div>
      </div>
    </section>

    <section id="definitie" data-title="Definitie">
      <h2>Wat het precies is, en wat het niet is</h2>
      <div class="grid-3">
        <div class="card">
          <h3>Definitie</h3>
          <p>VO2max = maximale O2-opname (ml/min of ml per kg per minuut). Het is de maximale aerobe energie die je kunt leveren.</p>
        </div>
        <div class="card">
          <h3>Wat het niet is</h3>
          <img id="hard-image" class="quote-image" src="{{HARD_IMAGE_URI}}" alt="Hoe hard je bent" />
          <p id="hard-fallback" class="image-fallback">Het is geen directe maat voor hoe hard je bent.</p>
          <p class="muted">Je drempels, efficiency en pacing bepalen hoe je dat plafond benut.</p>
        </div>
        <div class="card">
          <h3>Waarom het telt</h3>
          <p>Het is een anker om training te positioneren en progressie te volgen.</p>
        </div>
      </div>
    </section>

    <section id="keten" data-title="Keten">
      <h2>De keten die VO2max begrenst</h2>
      <p>VO2max wordt bepaald door de hele keten van aanvoer en gebruik. Trainen verschuift waar de bottleneck ligt.</p>
      <div class="tab-list" role="tablist" aria-label="Keten">
        <button class="tab-btn active" data-tab="longen" role="tab">Longen</button>
        <button class="tab-btn" data-tab="hart" role="tab">Hart & bloed</button>
        <button class="tab-btn" data-tab="spieren" role="tab">Spieren</button>
      </div>
      <div class="tab-panel active" id="tab-longen" role="tabpanel">
        <div class="card">
          <h3>Ventilatie en gaswisseling</h3>
          <p>De longen leveren de O2 aan die het systeem in kan. Goede ventilatie en gaswisseling zijn de start van de keten.</p>
        </div>
      </div>
      <div class="tab-panel" id="tab-hart" role="tabpanel">
        <div class="card">
          <h3>Cardiac output</h3>
          <p>Slagvolume maal hartfrequentie bepaalt hoeveel zuurstofrijk bloed per minuut kan worden vervoerd.</p>
        </div>
      </div>
      <div class="tab-panel" id="tab-spieren" role="tabpanel">
        <div class="card">
          <h3>Gebruik in de spieren</h3>
          <p>Capillairen en mitochondrien bepalen hoe goed de spieren O2 omzetten naar ATP.</p>
        </div>
      </div>

      <div class="slider-box" aria-live="polite">
        <label for="bottleneck">Waar ligt de bottleneck vandaag?</label>
        <input id="bottleneck" type="range" min="0" max="100" value="50" />
        <div class="mix-row">
          <div>Aanvoer</div>
          <div class="mix-bar"><span id="mix-delivery"></span></div>
          <div class="mix-value" id="mix-delivery-value">0%</div>
        </div>
        <div class="mix-row">
          <div>Gebruik</div>
          <div class="mix-bar"><span id="mix-use"></span></div>
          <div class="mix-value" id="mix-use-value">0%</div>
        </div>
      </div>

      <h3>Waar treedt vermoeidheid op na maximaal gaan?</h3>
      <p>Na maximaal gaan valt de keten vaak het eerst uit bij longen, hart of spieren. Welke plek limiterend is, verschilt per persoon en is deels genetisch bepaald.</p>
      <div class="fatigue-controls" role="tablist" aria-label="Vermoeidheid">
        <button class="fatigue-btn active" data-fatigue="longen" role="tab">Longen</button>
        <button class="fatigue-btn" data-fatigue="hart" role="tab">Hart</button>
        <button class="fatigue-btn" data-fatigue="spieren" role="tab">Spieren</button>
        <button class="fatigue-btn" data-fatigue="genetisch" role="tab">Genetisch</button>
      </div>
      <div class="chain-track" aria-hidden="true">
        <div class="chain-node active" data-node="longen">Longen</div>
        <div class="chain-arrow">→</div>
        <div class="chain-node" data-node="hart">Hart & bloed</div>
        <div class="chain-arrow">→</div>
        <div class="chain-node" data-node="spieren">Spieren</div>
      </div>
      <div class="genetics-pill" id="genetics-pill">Genetisch profiel bepaalt startpunt en plafond</div>
      <div class="card" id="fatigue-panel">
        <h3 id="fatigue-title">Longen</h3>
        <p id="fatigue-body">Maximale ademarbeid en gaswisseling kunnen limiteren. Dit is deels trainbaar, maar ook genetisch begrensd.</p>
      </div>
    </section>

    <section id="trainen" data-title="Trainen">
      <h2>Hoe verhoog je VO2max?</h2>
      <p>In de praktijk draait het om genoeg tijd dichtbij je maximale aerobe output. Je dwingt een hoge zuurstofvraag af en prikkelt zowel centrale als perifere factoren.</p>
      <div class="grid-3">
        <div class="card">
          <h3>Tijd bij het plafond</h3>
          <p>Niet sprinten, maar lang genoeg hoog blijven zodat je minuten "bij max" opbouwt.</p>
        </div>
        <div class="card">
          <h3>Voorbeeld: Noorse 4x4</h3>
          <p>4 blokken van 4 minuten op een intensiteit die je snel richting zeer hoge ademdruk en VO2 brengt, met herstel ertussen.</p>
        </div>
        <div class="card">
          <h3>Herhaalbaarheid</h3>
          <p>De kwaliteit zit in het kunnen herhalen van hoge minuten, niet in een enkele piek.</p>
        </div>
      </div>
      <div class="callout">Doel: zoveel mogelijk minuten dicht bij je VO2-plafond verzamelen zonder te sprinten.</div>
      <div class="interval-strip" aria-label="Noorse 4x4 schema">
        <div class="interval-block interval-work">4 min hoog</div>
        <div class="interval-block interval-rest">3 min herstel</div>
        <div class="interval-block interval-work">4 min hoog</div>
        <div class="interval-block interval-rest">3 min herstel</div>
        <div class="interval-block interval-work">4 min hoog</div>
        <div class="interval-block interval-rest">3 min herstel</div>
        <div class="interval-block interval-work">4 min hoog</div>
      </div>
      <p class="muted">Richt je op lang genoeg hoog blijven zodat je minuten bij het plafond opbouwt.</p>
    </section>

    <section id="zone2" data-title="Zone 2">
      <h2>Waarom zone 2 essentieel blijft</h2>
      <p>Alleen hoog-intensief werk is zelden de snelste route omhoog. Het fundament is een grote aerobe basis.</p>
      <div class="grid-3">
        <div class="card">
          <h3>Meer capaciteit</h3>
          <p>Meer mitochondrien en doorbloeding vergroten je aerobe motor.</p>
        </div>
        <div class="card">
          <h3>Efficienter systeem</h3>
          <p>Betere vetoxidatie en lagere herstelkosten maken consistent volume mogelijk.</p>
        </div>
        <div class="card">
          <h3>Betere VO2-trainbaarheid</h3>
          <p>Een sterke basis zorgt dat je hoge blokken vaker kunt herhalen en verwerken.</p>
        </div>
      </div>
      <div class="callout">Zone 2 rond VT1 is de motor van volume en adaptatie.</div>
    </section>

    <section id="meten" data-title="Meten">
      <h2>Meten verslaat formules</h2>
      <p>Horloges, standaardformules en percentages geven een model. Met ademgasanalyse krijg je een meting met minder individuele foutmarge.</p>
      <div class="tab-list" role="tablist" aria-label="Meten">
        <button class="tab-btn active" data-tab="schatting" role="tab">Schattingen</button>
        <button class="tab-btn" data-tab="meting" role="tab">Meting</button>
      </div>
      <div class="tab-panel active" id="tab-schatting" role="tabpanel">
        <div class="card">
          <h3>Model</h3>
          <p>Percentages van HRmax, 220-leeftijd, FTP-only en horloge-schattingen zijn generieke aannames.</p>
        </div>
      </div>
      <div class="tab-panel" id="tab-meting" role="tabpanel">
        <div class="card">
          <h3>Ademgasanalyse</h3>
          <p>Je ziet output (watt/tempo), respons (HR) en interne adem- en zuurstofrespons. Daarmee kun je VO2max en VT1/VT2 precies plaatsen.</p>
        </div>
      </div>
    </section>

    <section id="sportmetrics" data-title="SportMetrics">
      <h2>Wat je praktisch krijgt bij SportMetrics</h2>
      <div class="grid-3">
        <div class="card">
          <h3>VO2max plafond</h3>
          <p>Objectieve bepaling van jouw aerobe plafond.</p>
        </div>
        <div class="card">
          <h3>Progressie richting plafond</h3>
          <p>Hoe snel je richting VO2max gaat bij oplopend vermogen.</p>
        </div>
        <div class="card">
          <h3>Vertaling naar zones</h3>
          <p>VT1/VT2 en wattage-zones gekoppeld aan jouw profiel.</p>
        </div>
      </div>
      <p class="muted">Het doel is niet een mooi getal, maar een profiel om zone 2 en VO2max-werk gericht te doseren.</p>
    </section>

    <section id="samenvatting" data-title="Samenvatting">
      <h2>Samenvatting</h2>
      <ul class="summary-list">
        <li>VO2max is je aerobe plafond: hoeveel O2 je maximaal kunt opnemen en gebruiken.</li>
        <li>Het plafond verhoog je met veel minuten dicht bij max, zoals 4x4-blokken.</li>
        <li>Zone 2 rond VT1 bouwt de basis zodat hoge blokken beter te herhalen zijn.</li>
        <li>Met ademgasanalyse plaats je VO2max en VT1/VT2 precies, in plaats van generieke formules.</li>
      </ul>
      <p class="footer">We zien je snel bij SportMetrics.</p>
    </section>
  </main>

  <script>
    document.body.classList.add("enable-animations");

    const sections = Array.from(document.querySelectorAll("section[data-title]"));
    const navLinks = Array.from(document.querySelectorAll(".nav-link"));
    const progressBar = document.getElementById("progress-bar");

    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
        }
      });
    }, { threshold: 0.2 });

    sections.forEach((section) => revealObserver.observe(section));

    const spyObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          navLinks.forEach((link) => link.classList.toggle("active", link.dataset.section === entry.target.id));
        }
      });
    }, { threshold: 0.55 });

    sections.forEach((section) => spyObserver.observe(section));

    window.addEventListener("scroll", () => {
      const doc = document.documentElement;
      const scrollTop = doc.scrollTop || document.body.scrollTop;
      const scrollHeight = doc.scrollHeight - doc.clientHeight;
      const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
      progressBar.style.width = `${progress}%`;
    });

    const chainButtons = Array.from(document.querySelectorAll("#keten .tab-btn"));
    const chainPanels = {
      longen: document.getElementById("tab-longen"),
      hart: document.getElementById("tab-hart"),
      spieren: document.getElementById("tab-spieren")
    };

    chainButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const target = button.dataset.tab;
        chainButtons.forEach((btn) => btn.classList.toggle("active", btn === button));
        Object.entries(chainPanels).forEach(([key, panel]) => {
          panel.classList.toggle("active", key === target);
        });
      });
    });

    const measureButtons = Array.from(document.querySelectorAll("#meten .tab-btn"));
    const measurePanels = {
      schatting: document.getElementById("tab-schatting"),
      meting: document.getElementById("tab-meting")
    };

    measureButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const target = button.dataset.tab;
        measureButtons.forEach((btn) => btn.classList.toggle("active", btn === button));
        Object.entries(measurePanels).forEach(([key, panel]) => {
          panel.classList.toggle("active", key === target);
        });
      });
    });

    const bottleneck = document.getElementById("bottleneck");

    function updateBottleneck() {
      const value = parseInt(bottleneck.value, 10);
      const delivery = value;
      const use = 100 - value;
      document.getElementById("mix-delivery").style.width = `${delivery}%`;
      document.getElementById("mix-use").style.width = `${use}%`;
      document.getElementById("mix-delivery-value").textContent = `${delivery}%`;
      document.getElementById("mix-use-value").textContent = `${use}%`;
    }

    bottleneck.addEventListener("input", updateBottleneck);
    updateBottleneck();

    const fatigueButtons = Array.from(document.querySelectorAll(".fatigue-btn"));
    const fatigueNodes = Array.from(document.querySelectorAll(".chain-node"));
    const geneticsPill = document.getElementById("genetics-pill");
    const fatigueTitle = document.getElementById("fatigue-title");
    const fatigueBody = document.getElementById("fatigue-body");

    const fatigueCopy = {
      longen: {
        title: "Longen",
        text: "Maximale ademarbeid en gaswisseling kunnen limiteren. De aanleg is deels genetisch, training kan efficientie verbeteren."
      },
      hart: {
        title: "Hart",
        text: "Cardiac output begrenst vaak het plafond. Slagvolume en hartgrootte zijn deels genetisch, maar wel trainbaar."
      },
      spieren: {
        title: "Spieren",
        text: "Lokale benutting (mitochondrien, capillairen) en ionenbalans bepalen hoe lang je hoog kunt blijven. Sterk trainbaar."
      },
      genetisch: {
        title: "Genetisch",
        text: "Je startpunt en plafond voor VO2max zijn deels genetisch bepaald. Training bepaalt hoe dicht je bij dat plafond komt."
      }
    };

    function setFatigue(key) {
      const data = fatigueCopy[key];
      if (!data) return;
      fatigueTitle.textContent = data.title;
      fatigueBody.textContent = data.text;
      fatigueButtons.forEach((btn) => btn.classList.toggle("active", btn.dataset.fatigue === key));
      fatigueNodes.forEach((node) => node.classList.toggle("active", node.dataset.node === key));
      if (geneticsPill) {
        geneticsPill.classList.toggle("active", key === "genetisch");
      }
    }

    fatigueButtons.forEach((button) => {
      button.addEventListener("click", () => {
        setFatigue(button.dataset.fatigue);
      });
    });

    setFatigue("longen");

    const hardImage = document.getElementById("hard-image");
    const hardFallback = document.getElementById("hard-fallback");
    if (hardImage && hardFallback) {
      const src = hardImage.getAttribute("src");
      if (src) {
        hardFallback.style.display = "none";
      } else {
        hardImage.style.display = "none";
      }
    }
  </script>
</body>
</html>
"""

HTML_PAGE = HTML_PAGE.replace("{{LOGO_DATA_URI}}", logo_data_uri)
HTML_PAGE = HTML_PAGE.replace("{{HARD_IMAGE_URI}}", hard_image_uri)

components.html(HTML_PAGE, height=4800, scrolling=True)
```

## pages/2_VT1.py
```python

import importlib.util
import sys
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="VT1 - SportMetrics",
    layout="wide",
)

if "site.ui" not in sys.modules:
    ui_path = Path(__file__).resolve().parents[1] / "site" / "ui.py"
    spec = importlib.util.spec_from_file_location("site.ui", ui_path)
    if spec is None or spec.loader is None:
        raise ImportError("Kon site.ui niet laden")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules["site.ui"] = module

from site.ui import inject_global_css, top_nav

inject_global_css()
top_nav(active="VT1")

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "logo.png"
if not LOGO_PATH.exists():
    LOGO_PATH = BASE_DIR / "1.png"

logo_data_uri = ""
if LOGO_PATH.exists():
    logo_b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    logo_data_uri = f"data:image/png;base64,{logo_b64}"

HTML_PAGE = r"""
<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>VT1 - SportMetrics</title>
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Spectral:wght@400;600&display=swap");

    :root {
      --sand: #f6f1ea;
      --clay: #e9ddd2;
      --ink: #1e2a2f;
      --muted: #5c6b73;
      --sea: #2f7c85;
      --deep: #0f4c5c;
      --sun: #f4b66a;
      --peach: #f1c9a9;
      --card: #fffdf6;
      --card-strong: #ffffff;
      --border: rgba(30, 42, 47, 0.12);
      --shadow: 0 18px 50px rgba(15, 76, 92, 0.18);
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: "Spectral", "Times New Roman", serif;
      color: var(--ink);
      background: radial-gradient(1200px 800px at 10% -10%, #ffffff 0%, var(--sand) 60%, var(--clay) 100%);
    }

    .logo-pattern {
      position: fixed;
      inset: 0;
      background-image: url('{{LOGO_DATA_URI}}');
      background-repeat: repeat;
      background-position: center;
      background-size: 140px;
      opacity: 0.07;
      mix-blend-mode: multiply;
      pointer-events: none;
      z-index: 1;
    }

    .bg-shape {
      position: fixed;
      inset: auto;
      width: 480px;
      height: 480px;
      border-radius: 50%;
      background: radial-gradient(circle at 30% 30%, rgba(47, 124, 133, 0.28), rgba(47, 124, 133, 0.02));
      z-index: -1;
    }
    .bg-shape.one { top: -120px; right: -120px; }
    .bg-shape.two { bottom: -200px; left: -140px; background: radial-gradient(circle, rgba(244, 182, 106, 0.35), rgba(244, 182, 106, 0.02)); }

    nav {
      position: fixed;
      top: 28px;
      right: 26px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 14px 14px;
      box-shadow: var(--shadow);
      z-index: 4;
      max-width: 190px;
    }
    nav h4 {
      margin: 0 0 6px;
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
    }
    .nav-link {
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-decoration: none;
      color: var(--muted);
      display: flex;
      gap: 6px;
      align-items: center;
      transition: color 0.2s ease;
    }
    .nav-link span {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--clay);
      border: 1px solid var(--border);
    }
    .nav-link.active { color: var(--deep); font-weight: 600; }
    .nav-link.active span { background: var(--sea); border-color: var(--sea); }

    .progress {
      height: 6px;
      background: rgba(47, 124, 133, 0.12);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 6px;
    }
    .progress span { display: block; height: 100%; width: 0%; background: var(--sea); transition: width 0.2s ease; }

    main {
      position: relative;
      z-index: 3;
      max-width: 1100px;
      margin: 0 auto;
      padding: 64px 24px 120px;
    }

    section {
      margin: 0 0 72px;
      padding: 36px;
      border-radius: 26px;
      background: var(--card);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      transition: all 0.7s ease;
    }
    body.enable-animations section { opacity: 0; transform: translateY(20px); }
    body.enable-animations section.in-view { opacity: 1; transform: translateY(0); }

    .hero {
      padding: 54px 44px;
      background: linear-gradient(140deg, #ffffff, #f6e7d6);
    }
    .hero h1 {
      font-family: "Space Grotesk", sans-serif;
      font-size: clamp(2.2rem, 3.4vw, 3.4rem);
      margin: 0 0 12px;
      color: var(--deep);
    }
    .hero p {
      font-size: 1.05rem;
      color: var(--muted);
      margin: 0;
      max-width: 720px;
    }
    .hero .hero-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
      margin-top: 28px;
    }
    .hero .stat {
      padding: 16px 18px;
      background: var(--card-strong);
      border-radius: 16px;
      border: 1px solid var(--border);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.95rem;
      color: var(--muted);
    }
    .hero .stat strong { display: block; color: var(--deep); font-size: 1.1rem; }

    h2 {
      font-family: "Space Grotesk", sans-serif;
      margin: 0 0 12px;
      color: var(--deep);
      font-size: 1.8rem;
    }
    h3 {
      font-family: "Space Grotesk", sans-serif;
      margin: 0 0 8px;
      color: var(--deep);
    }
    p { margin: 0 0 14px; color: var(--ink); line-height: 1.55; }
    .muted { color: var(--muted); }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
    }
    .card {
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 16px 18px;
    }
    .pill {
      display: inline-block;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.72rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: 999px;
      margin-bottom: 10px;
    }

    .slider-box {
      margin-top: 18px;
      padding: 18px;
      border-radius: 18px;
      border: 1px dashed rgba(47, 124, 133, 0.4);
      background: #eef5f4;
    }
    .slider-box label {
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
    }
    .slider-box input[type="range"] { width: 100%; margin: 10px 0 6px; }
    .mix-row {
      display: grid;
      grid-template-columns: 130px 1fr 54px;
      gap: 12px;
      align-items: center;
      margin: 10px 0;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.85rem;
    }
    .mix-bar {
      background: #eef5f4;
      border-radius: 999px;
      overflow: hidden;
      height: 10px;
      border: 1px solid rgba(15, 76, 92, 0.2);
    }
    .mix-bar span {
      display: block;
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--sea), var(--deep));
      border-radius: 999px;
      transition: width 0.3s ease;
    }
    .mix-value { text-align: right; color: var(--muted); }

    .vt1-bar {
      margin-top: 14px;
      position: relative;
      height: 16px;
      border-radius: 999px;
      background: #eef5f4;
      border: 1px solid rgba(15, 76, 92, 0.2);
      overflow: hidden;
    }
    .vt1-window {
      position: absolute;
      top: 0;
      bottom: 0;
      width: 18%;
      left: 41%;
      border-radius: 999px;
      background: rgba(47, 124, 133, 0.3);
    }
    .vt1-marker {
      position: absolute;
      top: -4px;
      width: 2px;
      height: 24px;
      background: var(--deep);
      left: 50%;
    }

    .stepper {
      display: grid;
      grid-template-columns: repeat(8, minmax(68px, 1fr));
      gap: 10px;
      margin-top: 16px;
    }
    .step {
      padding: 10px 8px;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: var(--card-strong);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.8rem;
      text-align: center;
      color: var(--muted);
    }
    .step.active {
      background: var(--deep);
      color: #fff;
      border-color: var(--deep);
    }

    .callout {
      background: #f3e4d2;
      border: 1px solid #e8cfae;
      padding: 16px 18px;
      border-radius: 18px;
      font-family: "Space Grotesk", sans-serif;
    }

    .summary-list {
      margin: 0;
      padding-left: 18px;
    }
    .summary-list li {
      margin: 0 0 10px;
    }

    .footer {
      text-align: center;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
      color: var(--muted);
    }

    @media (max-width: 980px) {
      nav { display: none; }
      section { padding: 28px; }
      .mix-row { grid-template-columns: 110px 1fr 48px; }
    }

    @media (max-width: 720px) {
      main { padding: 40px 16px 90px; }
      section { padding: 18px; margin: 0 0 36px; }
      .hero { padding: 24px 18px; }
      .hero h1 { font-size: clamp(1.8rem, 6vw, 2.4rem); }
      .hero .hero-grid { grid-template-columns: 1fr; }
      .grid-3 { grid-template-columns: 1fr; }
      .mix-row { grid-template-columns: 1fr; gap: 6px; }
      .mix-value { text-align: left; }
      .stepper { grid-template-columns: repeat(4, minmax(70px, 1fr)); }
      .card { padding: 14px; }
    }

    @media (prefers-reduced-motion: reduce) {
      * { scroll-behavior: auto; }
      section { transition: none; }
      body.enable-animations section { opacity: 1; transform: none; }
    }
  </style>
</head>
<body>
  <div class="logo-pattern" aria-hidden="true"></div>
  <div class="bg-shape one"></div>
  <div class="bg-shape two"></div>

  <nav aria-label="Navigatie">
    <h4>Route</h4>
    <a class="nav-link" href="#intro" data-section="intro"><span></span>Intro</a>
    <a class="nav-link" href="#definitie" data-section="definitie"><span></span>Definitie</a>
    <a class="nav-link" href="#mechanisme" data-section="mechanisme"><span></span>Mechanisme</a>
    <a class="nav-link" href="#gebied" data-section="gebied"><span></span>Gebied</a>
    <a class="nav-link" href="#ramp" data-section="ramp"><span></span>Ramp-test</a>
    <a class="nav-link" href="#training" data-section="training"><span></span>Training</a>
    <a class="nav-link" href="#sportmetrics" data-section="sportmetrics"><span></span>SportMetrics</a>
    <a class="nav-link" href="#samenvatting" data-section="samenvatting"><span></span>Samenvatting</a>
    <div class="progress"><span id="progress-bar"></span></div>
  </nav>

  <main>
    <section id="intro" class="hero" data-title="Intro">
      <span class="pill">VT1</span>
      <h1>VT1: de eerste drempel is een shift in ademregulatie</h1>
      <p>VT1 markeert het moment waarop je ademhaling disproportioneel begint toe te nemen ten opzichte van de belasting. Geen schakelaar, maar een duidelijke overgang in hoe je lichaam de interne balans stabiel houdt.</p>
      <div class="hero-grid">
        <div class="stat"><strong>Eerste overgang</strong>VE stijgt relatief sneller dan VO2 en vermogen.</div>
        <div class="stat"><strong>Duurzaam domein</strong>Je zit nog duurzaam, maar regulatie wordt merkbaar zwaarder.</div>
        <div class="stat"><strong>Praktisch anker</strong>VT1 kalibreert jouw zone 2 in plaats van generieke percentages.</div>
      </div>
    </section>

    <section id="definitie" data-title="Definitie">
      <h2>Wat VT1 precies is</h2>
      <div class="grid-3">
        <div class="card">
          <h3>Ventilatoire overgang</h3>
          <p>VE (ventilatie) gaat relatief sneller stijgen dan VO2 en het vermogen.</p>
        </div>
        <div class="card">
          <h3>Regulatiepunt</h3>
          <p>Ademhaling en circulatie moeten merkbaar harder werken, terwijl je nog duurzaam kunt werken.</p>
        </div>
        <div class="card">
          <h3>Geen vetzone</h3>
          <p>VT1 is geen vetverbrandingsschakelaar, maar een shift in regulatie.</p>
        </div>
      </div>
    </section>

    <section id="mechanisme" data-title="Mechanisme">
      <h2>Waarom ventilatie toeneemt</h2>
      <p>Bij hogere intensiteit stijgt de koolhydraatbijdrage en verandert de zuur-base balans. Je lichaam ventileert meer om CO2 af te voeren en pH te stabiliseren. Dat is het begin van duidelijke drift.</p>
      <div class="slider-box" aria-live="polite">
        <label for="intensity">Sleep: inspanningsintensiteit</label>
        <input id="intensity" type="range" min="0" max="100" value="35" />
        <div class="mix-row">
          <div>Ventilatie (VE)</div>
          <div class="mix-bar"><span id="mix-ve"></span></div>
          <div class="mix-value" id="mix-ve-value">0%</div>
        </div>
        <div class="mix-row">
          <div>CO2 / pH-regulatie</div>
          <div class="mix-bar"><span id="mix-co2"></span></div>
          <div class="mix-value" id="mix-co2-value">0%</div>
        </div>
        <div class="mix-row">
          <div>Drift</div>
          <div class="mix-bar"><span id="mix-drift"></span></div>
          <div class="mix-value" id="mix-drift-value">0%</div>
        </div>
      </div>
    </section>

    <section id="gebied" data-title="Gebied">
      <h2>VT1 is een gebied, geen exact punt</h2>
      <p>VT1 verschuift met dagvorm, protocol, cadans, voeding en warmte. Daarom rapporteren we VT1 als ankergebied in plaats van een exact wattpunt.</p>
      <div class="slider-box" aria-live="polite">
        <label for="vt1-shift">Dagvorm / omstandigheden</label>
        <input id="vt1-shift" type="range" min="-10" max="10" value="0" />
        <div class="vt1-bar">
          <div class="vt1-window" id="vt1-window"></div>
          <div class="vt1-marker" id="vt1-marker"></div>
        </div>
        <p class="muted">Het ankergebied schuift mee, maar blijft hetzelfde fysiologische domein.</p>
      </div>
    </section>

    <section id="ramp" data-title="Ramp-test">
      <h2>VT1 in een ramp-test</h2>
      <p>In de ramp-test zie je rond VT1 een versnelling in de ademrespons. Door vaste stappen en duur kun je het moment scherp koppelen aan wattage.</p>
      <div class="slider-box" aria-live="polite">
        <label for="ramp-step">Kies een stap in de test</label>
        <input id="ramp-step" type="range" min="1" max="8" value="4" />
        <div class="stepper" id="stepper">
          <div class="step">Step 1</div>
          <div class="step">Step 2</div>
          <div class="step">Step 3</div>
          <div class="step">Step 4</div>
          <div class="step">Step 5</div>
          <div class="step">Step 6</div>
          <div class="step">Step 7</div>
          <div class="step">Step 8</div>
        </div>
        <div class="card" id="ramp-detail">
          <h3>Ademrespons versnelt</h3>
          <p>Hier zie je dat VE sneller toeneemt dan VO2. HR kan nog licht achterlopen (HR-lag).</p>
        </div>
      </div>
      <div class="callout">Ademrespons + wattage geeft een scherp anker. HR alleen kan vertraging hebben.</div>
    </section>

    <section id="training" data-title="Training">
      <h2>Waarom VT1 zo belangrijk is</h2>
      <div class="grid-3">
        <div class="card">
          <h3>Duurvolume en consistentie</h3>
          <p>VT1 is vaak de hoogste intensiteit die je lang kunt stapelen met lage herstelkosten.</p>
        </div>
        <div class="card">
          <h3>Efficientie</h3>
          <p>Meer aerobe efficientie: minder ventilatoire druk bij hetzelfde vermogen.</p>
        </div>
        <div class="card">
          <h3>Pacing</h3>
          <p>Boven VT1 starten geeft sneller drift en onnodige kosten.</p>
        </div>
      </div>
      <p class="muted">VT1 valt vaak in wat veel modellen "zone 2" noemen. VT1 is het fysiologische anker om die zone te kalibreren.</p>
    </section>

    <section id="sportmetrics" data-title="SportMetrics">
      <h2>Wat je praktisch krijgt bij SportMetrics</h2>
      <div class="grid-3">
        <div class="card">
          <h3>VT1 als ankergebied</h3>
          <p>Positionering op basis van VO2, VE, ademfrequentie en teugvolume, gekoppeld aan vermogen en HR.</p>
        </div>
        <div class="card">
          <h3>Direct toepasbaar</h3>
          <p>VT1 wordt vertaald naar uitvoerbare trainingszones en advies.</p>
        </div>
        <div class="card">
          <h3>Transparant meten</h3>
          <p>We meten geen VCO2, dus rapporteren geen exacte RER of substraatpercentages.</p>
        </div>
      </div>
      <div class="callout">VT1 gebruiken we als intensiteitsanker dat direct uitvoerbaar is in training.</div>
    </section>

    <section id="samenvatting" data-title="Samenvatting">
      <h2>Samenvatting</h2>
      <ul class="summary-list">
        <li>VT1 is de eerste ventilatoire overgang: VE versnelt relatief ten opzichte van VO2 en watt.</li>
        <li>Het is geen vetverbrandingsschakelaar maar een regulatiepunt met meer drift.</li>
        <li>VT1 is een gebied dat schuift met dagvorm en omstandigheden, daarom rapporteren we een ankergebied.</li>
        <li>In de ramp-test koppelen we VT1 scherp aan vermogen via ademrespons; HR kan vertragen.</li>
      </ul>
      <p class="footer">We zien je graag bij SportMetrics.</p>
    </section>
  </main>

  <script>
    document.body.classList.add("enable-animations");

    const sections = Array.from(document.querySelectorAll("section[data-title]"));
    const navLinks = Array.from(document.querySelectorAll(".nav-link"));
    const progressBar = document.getElementById("progress-bar");

    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
        }
      });
    }, { threshold: 0.2 });

    sections.forEach((section) => revealObserver.observe(section));

    const spyObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          navLinks.forEach((link) => link.classList.toggle("active", link.dataset.section === entry.target.id));
        }
      });
    }, { threshold: 0.55 });

    sections.forEach((section) => spyObserver.observe(section));

    window.addEventListener("scroll", () => {
      const doc = document.documentElement;
      const scrollTop = doc.scrollTop || document.body.scrollTop;
      const scrollHeight = doc.scrollHeight - doc.clientHeight;
      const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
      progressBar.style.width = `${progress}%`;
    });

    const intensity = document.getElementById("intensity");

    function updateIntensity() {
      const value = parseInt(intensity.value, 10);
      const ve = Math.max(0, (value - 25) / 75);
      const co2 = Math.max(0, (value - 35) / 65);
      const drift = Math.max(0, (value - 50) / 50);

      document.getElementById("mix-ve").style.width = `${Math.round(ve * 100)}%`;
      document.getElementById("mix-co2").style.width = `${Math.round(co2 * 100)}%`;
      document.getElementById("mix-drift").style.width = `${Math.round(drift * 100)}%`;

      document.getElementById("mix-ve-value").textContent = `${Math.round(ve * 100)}%`;
      document.getElementById("mix-co2-value").textContent = `${Math.round(co2 * 100)}%`;
      document.getElementById("mix-drift-value").textContent = `${Math.round(drift * 100)}%`;
    }

    intensity.addEventListener("input", updateIntensity);
    updateIntensity();

    const vt1Shift = document.getElementById("vt1-shift");
    const vt1Window = document.getElementById("vt1-window");
    const vt1Marker = document.getElementById("vt1-marker");

    function updateVT1Shift() {
      const shift = parseInt(vt1Shift.value, 10);
      let center = 50 + shift * 2;
      center = Math.max(15, Math.min(85, center));
      const width = 18;
      vt1Window.style.left = `${center - width / 2}%`;
      vt1Marker.style.left = `${center}%`;
    }

    vt1Shift.addEventListener("input", updateVT1Shift);
    updateVT1Shift();

    const rampStep = document.getElementById("ramp-step");
    const rampSteps = Array.from(document.querySelectorAll("#stepper .step"));
    const rampDetail = document.getElementById("ramp-detail");

    const rampCopy = [
      "Rustig begin: ademrespons volgt vermogen vrijwel lineair.",
      "Ademfrequentie stijgt licht, nog weinig drift.",
      "VO2 stijgt stevig, ventilatie blijft beheersbaar.",
      "Hier rond VT1 begint VE sneller te stijgen dan VO2.",
      "Duidelijker regulatie: ademarbeid neemt toe.",
      "HR kan nog achterlopen terwijl VE versnelt (HR-lag).",
      "Drift wordt zichtbaar bij langer aanhouden.",
      "Boven VT1 neemt ventilatoire druk snel toe."
    ];

    function updateRamp() {
      const step = parseInt(rampStep.value, 10);
      rampSteps.forEach((el, idx) => {
        el.classList.toggle("active", idx === step - 1);
      });
      const text = rampCopy[step - 1] || rampCopy[0];
      rampDetail.querySelector("p").textContent = text;
    }

    rampStep.addEventListener("input", updateRamp);
    updateRamp();
  </script>
</body>
</html>
"""

HTML_PAGE = HTML_PAGE.replace("{{LOGO_DATA_URI}}", logo_data_uri)

components.html(HTML_PAGE, height=4800, scrolling=True)
```

## pages/3_VT2.py
```python

import importlib.util
import sys
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="VT2 - SportMetrics",
    layout="wide",
)

if "site.ui" not in sys.modules:
    ui_path = Path(__file__).resolve().parents[1] / "site" / "ui.py"
    spec = importlib.util.spec_from_file_location("site.ui", ui_path)
    if spec is None or spec.loader is None:
        raise ImportError("Kon site.ui niet laden")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules["site.ui"] = module

from site.ui import inject_global_css, top_nav

inject_global_css()
top_nav(active="VT2")

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "logo.png"
if not LOGO_PATH.exists():
    LOGO_PATH = BASE_DIR / "1.png"

logo_data_uri = ""
if LOGO_PATH.exists():
    logo_b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    logo_data_uri = f"data:image/png;base64,{logo_b64}"

HTML_PAGE = r"""
<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>VT2 - SportMetrics</title>
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Spectral:wght@400;600&display=swap");

    :root {
      --sand: #f6f1ea;
      --clay: #e9ddd2;
      --ink: #1e2a2f;
      --muted: #5c6b73;
      --sea: #2f7c85;
      --deep: #0f4c5c;
      --sun: #f4b66a;
      --peach: #f1c9a9;
      --card: #fffdf6;
      --card-strong: #ffffff;
      --border: rgba(30, 42, 47, 0.12);
      --shadow: 0 18px 50px rgba(15, 76, 92, 0.18);
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: "Spectral", "Times New Roman", serif;
      color: var(--ink);
      background: radial-gradient(1200px 800px at 10% -10%, #ffffff 0%, var(--sand) 60%, var(--clay) 100%);
    }

    .logo-pattern {
      position: fixed;
      inset: 0;
      background-image: url('{{LOGO_DATA_URI}}');
      background-repeat: repeat;
      background-position: center;
      background-size: 140px;
      opacity: 0.07;
      mix-blend-mode: multiply;
      pointer-events: none;
      z-index: 1;
    }

    .bg-shape {
      position: fixed;
      inset: auto;
      width: 480px;
      height: 480px;
      border-radius: 50%;
      background: radial-gradient(circle at 30% 30%, rgba(47, 124, 133, 0.28), rgba(47, 124, 133, 0.02));
      z-index: -1;
    }
    .bg-shape.one { top: -120px; right: -120px; }
    .bg-shape.two { bottom: -200px; left: -140px; background: radial-gradient(circle, rgba(244, 182, 106, 0.35), rgba(244, 182, 106, 0.02)); }

    nav {
      position: fixed;
      top: 28px;
      right: 26px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 14px 14px;
      box-shadow: var(--shadow);
      z-index: 4;
      max-width: 190px;
    }
    nav h4 {
      margin: 0 0 6px;
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
    }
    .nav-link {
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-decoration: none;
      color: var(--muted);
      display: flex;
      gap: 6px;
      align-items: center;
      transition: color 0.2s ease;
    }
    .nav-link span {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--clay);
      border: 1px solid var(--border);
    }
    .nav-link.active { color: var(--deep); font-weight: 600; }
    .nav-link.active span { background: var(--sea); border-color: var(--sea); }

    .progress {
      height: 6px;
      background: rgba(47, 124, 133, 0.12);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 6px;
    }
    .progress span { display: block; height: 100%; width: 0%; background: var(--sea); transition: width 0.2s ease; }

    main {
      position: relative;
      z-index: 3;
      max-width: 1100px;
      margin: 0 auto;
      padding: 64px 24px 120px;
    }

    section {
      margin: 0 0 72px;
      padding: 36px;
      border-radius: 26px;
      background: var(--card);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      transition: all 0.7s ease;
    }
    body.enable-animations section { opacity: 0; transform: translateY(20px); }
    body.enable-animations section.in-view { opacity: 1; transform: translateY(0); }

    .hero {
      padding: 54px 44px;
      background: linear-gradient(140deg, #ffffff, #f6e7d6);
    }
    .hero h1 {
      font-family: "Space Grotesk", sans-serif;
      font-size: clamp(2.2rem, 3.4vw, 3.4rem);
      margin: 0 0 12px;
      color: var(--deep);
    }
    .hero p {
      font-size: 1.05rem;
      color: var(--muted);
      margin: 0;
      max-width: 720px;
    }
    .hero .hero-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
      margin-top: 28px;
    }
    .hero .stat {
      padding: 16px 18px;
      background: var(--card-strong);
      border-radius: 16px;
      border: 1px solid var(--border);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.95rem;
      color: var(--muted);
    }
    .hero .stat strong { display: block; color: var(--deep); font-size: 1.1rem; }

    h2 {
      font-family: "Space Grotesk", sans-serif;
      margin: 0 0 12px;
      color: var(--deep);
      font-size: 1.8rem;
    }
    h3 {
      font-family: "Space Grotesk", sans-serif;
      margin: 0 0 8px;
      color: var(--deep);
    }
    p { margin: 0 0 14px; color: var(--ink); line-height: 1.55; }
    .muted { color: var(--muted); }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
    }
    .card {
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 16px 18px;
    }
    .pill {
      display: inline-block;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.72rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: 999px;
      margin-bottom: 10px;
    }

    .slider-box {
      margin-top: 18px;
      padding: 18px;
      border-radius: 18px;
      border: 1px dashed rgba(47, 124, 133, 0.4);
      background: #eef5f4;
    }
    .slider-box label {
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
    }
    .slider-box input[type="range"] { width: 100%; margin: 10px 0 6px; }
    .mix-row {
      display: grid;
      grid-template-columns: 130px 1fr 54px;
      gap: 12px;
      align-items: center;
      margin: 10px 0;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.85rem;
    }
    .mix-bar {
      background: #eef5f4;
      border-radius: 999px;
      overflow: hidden;
      height: 10px;
      border: 1px solid rgba(15, 76, 92, 0.2);
    }
    .mix-bar span {
      display: block;
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--sea), var(--deep));
      border-radius: 999px;
      transition: width 0.3s ease;
    }
    .mix-value { text-align: right; color: var(--muted); }

    .drift-chart {
      margin-top: 16px;
      display: grid;
      grid-template-columns: repeat(10, minmax(32px, 1fr));
      gap: 6px;
      align-items: end;
      height: 120px;
    }
    .drift-bar {
      width: 100%;
      border-radius: 8px 8px 4px 4px;
      background: rgba(47, 124, 133, 0.2);
      border: 1px solid rgba(47, 124, 133, 0.35);
      height: 40%;
      transition: height 0.4s ease, background 0.4s ease;
    }
    .drift-bar.active {
      background: var(--deep);
      border-color: var(--deep);
    }

    .vt2-bar {
      margin-top: 14px;
      position: relative;
      height: 16px;
      border-radius: 999px;
      background: #eef5f4;
      border: 1px solid rgba(15, 76, 92, 0.2);
      overflow: hidden;
    }
    .vt2-window {
      position: absolute;
      top: 0;
      bottom: 0;
      width: 18%;
      left: 62%;
      border-radius: 999px;
      background: rgba(47, 124, 133, 0.32);
    }
    .vt2-marker {
      position: absolute;
      top: -4px;
      width: 2px;
      height: 24px;
      background: var(--deep);
      left: 70%;
    }

    .stepper {
      display: grid;
      grid-template-columns: repeat(8, minmax(68px, 1fr));
      gap: 10px;
      margin-top: 16px;
    }
    .step {
      padding: 10px 8px;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: var(--card-strong);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.8rem;
      text-align: center;
      color: var(--muted);
    }
    .step.active {
      background: var(--deep);
      color: #fff;
      border-color: var(--deep);
    }

    .callout {
      background: #f3e4d2;
      border: 1px solid #e8cfae;
      padding: 16px 18px;
      border-radius: 18px;
      font-family: "Space Grotesk", sans-serif;
    }

    .summary-list {
      margin: 0;
      padding-left: 18px;
    }
    .summary-list li {
      margin: 0 0 10px;
    }

    .footer {
      text-align: center;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
      color: var(--muted);
    }

    @media (max-width: 980px) {
      nav { display: none; }
      section { padding: 28px; }
      .mix-row { grid-template-columns: 110px 1fr 48px; }
    }

    @media (max-width: 720px) {
      main { padding: 40px 16px 90px; }
      section { padding: 18px; margin: 0 0 36px; }
      .hero { padding: 24px 18px; }
      .hero h1 { font-size: clamp(1.8rem, 6vw, 2.4rem); }
      .hero .hero-grid { grid-template-columns: 1fr; }
      .grid-3 { grid-template-columns: 1fr; }
      .mix-row { grid-template-columns: 1fr; gap: 6px; }
      .mix-value { text-align: left; }
      .stepper { grid-template-columns: repeat(4, minmax(70px, 1fr)); }
      .card { padding: 14px; }
      .drift-chart { grid-template-columns: repeat(5, minmax(36px, 1fr)); }
    }

    @media (prefers-reduced-motion: reduce) {
      * { scroll-behavior: auto; }
      section { transition: none; }
      body.enable-animations section { opacity: 1; transform: none; }
    }
  </style>
</head>
<body>
  <div class="logo-pattern" aria-hidden="true"></div>
  <div class="bg-shape one"></div>
  <div class="bg-shape two"></div>

  <nav aria-label="Navigatie">
    <h4>Route</h4>
    <a class="nav-link" href="#intro" data-section="intro"><span></span>Intro</a>
    <a class="nav-link" href="#definitie" data-section="definitie"><span></span>Definitie</a>
    <a class="nav-link" href="#mechanisme" data-section="mechanisme"><span></span>Mechanisme</a>
    <a class="nav-link" href="#gebied" data-section="gebied"><span></span>Gebied</a>
    <a class="nav-link" href="#ramp" data-section="ramp"><span></span>Ramp-test</a>
    <a class="nav-link" href="#training" data-section="training"><span></span>Training</a>
    <a class="nav-link" href="#meten" data-section="meten"><span></span>Meten</a>
    <a class="nav-link" href="#samenvatting" data-section="samenvatting"><span></span>Samenvatting</a>
    <div class="progress"><span id="progress-bar"></span></div>
  </nav>

  <main>
    <section id="intro" class="hero" data-title="Intro">
      <span class="pill">VT2</span>
      <h1>VT2: de tweede drempel is een shift naar non-steady state</h1>
      <p>VT2 markeert het punt waarop inspanning voor de meeste sporters niet meer lang stabiel blijft. Ademdruk en vermoeidheidsopbouw nemen snel toe: de overgang naar echt zwaar werk.</p>
      <div class="hero-grid">
        <div class="stat"><strong>Non-steady state</strong>Je lichaam kan de interne balans niet meer lang stabiel houden.</div>
        <div class="stat"><strong>Hoge ademdruk</strong>Ventilatie stijgt disproportioneel bij gelijke belasting.</div>
        <div class="stat"><strong>Drempelanker</strong>VT2 positioneert threshold en zwaar tempo-werk.</div>
      </div>
    </section>

    <section id="definitie" data-title="Definitie">
      <h2>Wat VT2 precies is</h2>
      <div class="grid-3">
        <div class="card">
          <h3>Tweede overgang</h3>
          <p>VE versnelt opnieuw ten opzichte van VO2 en wattage.</p>
        </div>
        <div class="card">
          <h3>Ademhaling limiteert pacing</h3>
          <p>Niet omdat je “buiten adem” bent, maar omdat de regulatie steeds zwaarder wordt.</p>
        </div>
        <div class="card">
          <h3>Praktisch</h3>
          <p>Je komt in een domein waar steady werken steeds moeilijker wordt.</p>
        </div>
      </div>
    </section>

    <section id="mechanisme" data-title="Mechanisme">
      <h2>Waarom VT2 anders voelt</h2>
      <p>Rond VT2 leunt je lichaam sterker op snelle koolhydraat-ATP, waardoor de metabole stabiliteit afneemt. Drift wordt snel zichtbaar.</p>
      <div class="slider-box" aria-live="polite">
        <label for="drift-level">Drift bij gelijk vermogen</label>
        <input id="drift-level" type="range" min="1" max="10" value="6" />
        <div class="drift-chart" id="drift-chart">
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
        </div>
        <p class="muted">Drift = progressieve toename van interne belasting (HR/VE) bij gelijk vermogen.</p>
      </div>
    </section>

    <section id="gebied" data-title="Gebied">
      <h2>VT2 is een gebied, geen exact punt</h2>
      <p>VT2 schuift met vermoeidheid, warmte, voeding, protocol en meetruis. Daarom behandelen we het als ankergebied.</p>
      <div class="slider-box" aria-live="polite">
        <label for="vt2-shift">Dagvorm / omstandigheden</label>
        <input id="vt2-shift" type="range" min="-10" max="10" value="0" />
        <div class="vt2-bar">
          <div class="vt2-window" id="vt2-window"></div>
          <div class="vt2-marker" id="vt2-marker"></div>
        </div>
        <p class="muted">Het ankergebied schuift mee, maar blijft hetzelfde fysiologische domein.</p>
      </div>
    </section>

    <section id="ramp" data-title="Ramp-test">
      <h2>VT2 in een ramp-test</h2>
      <p>Door vaste stappen zie je precies waar ventilatie versnelt. HR loopt soms later mee (HR-lag), daarom koppelen we VT2 aan ademrespons.</p>
      <div class="slider-box" aria-live="polite">
        <label for="ramp-step">Kies een stap in de test</label>
        <input id="ramp-step" type="range" min="1" max="8" value="6" />
        <div class="stepper" id="stepper">
          <div class="step">Step 1</div>
          <div class="step">Step 2</div>
          <div class="step">Step 3</div>
          <div class="step">Step 4</div>
          <div class="step">Step 5</div>
          <div class="step">Step 6</div>
          <div class="step">Step 7</div>
          <div class="step">Step 8</div>
        </div>
        <div class="card" id="ramp-detail">
          <h3>Ventilatie versnelt</h3>
          <p>Rond VT2 zie je dat VE opnieuw versnelt en HR nog kan achterlopen.</p>
        </div>
      </div>
      <div class="callout">Ademrespons + wattage geeft een scherp anker. HR alleen kan vertraging hebben.</div>
    </section>

    <section id="training" data-title="Training">
      <h2>Waar VT2 voor dient (en waar niet)</h2>
      <div class="grid-3">
        <div class="card">
          <h3>Thresholdblokken</h3>
          <p>Duurzaam hard, maar niet maximaal. Grote prestatiewinst, hoge herstelkosten.</p>
        </div>
        <div class="card">
          <h3>Pacing</h3>
          <p>Net onder/omheen VT2 voor lange inspanningen.</p>
        </div>
        <div class="card">
          <h3>Begrenzen</h3>
          <p>Voorkom onbewust te veel "duur" werk in dit domein.</p>
        </div>
      </div>
      <p class="muted">VT2 is geen tempo dat je dagelijks kunt stapelen alsof het duur is.</p>
    </section>

    <section id="meten" data-title="Meten">
      <h2>VT2 versus FTP en CP</h2>
      <p>FTP is bruikbaar maar vaak protocol-afhankelijk. VT2 is een fysiologisch anker uit ademrespons. CP komt uit de power-duration relatie.</p>
      <div class="grid-3">
        <div class="card">
          <h3>FTP</h3>
          <p>Performance-schatting met foutmarges, afhankelijk van motivatie, pacing en protocol.</p>
        </div>
        <div class="card">
          <h3>VT2</h3>
          <p>Fysiologisch anker: shift naar non-steady state zichtbaar in ademrespons en VO2.</p>
        </div>
        <div class="card">
          <h3>CP</h3>
          <p>Power-duration model; goed voor het grensgebied van beperkte capaciteit.</p>
        </div>
      </div>
    </section>

    <section id="samenvatting" data-title="Samenvatting">
      <h2>Samenvatting</h2>
      <ul class="summary-list">
        <li>VT2 is de tweede ventilatoire overgang: VE versnelt opnieuw bij hogere belasting.</li>
        <li>Het markeert een shift naar non-steady state, waar drift snel toeneemt.</li>
        <li>VT2 is een gebied dat schuift met dagvorm en omstandigheden.</li>
        <li>Ademrespons + wattage plaatsen VT2 scherper dan HR alleen (HR-lag).</li>
        <li>VT2 is een fysiologisch anker; FTP/CP zijn bruikbaar maar andere kaders.</li>
      </ul>
      <p class="footer">We zien je graag bij SportMetrics.</p>
    </section>
  </main>

  <script>
    document.body.classList.add("enable-animations");

    const sections = Array.from(document.querySelectorAll("section[data-title]"));
    const navLinks = Array.from(document.querySelectorAll(".nav-link"));
    const progressBar = document.getElementById("progress-bar");

    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
        }
      });
    }, { threshold: 0.2 });

    sections.forEach((section) => revealObserver.observe(section));

    const spyObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          navLinks.forEach((link) => link.classList.toggle("active", link.dataset.section === entry.target.id));
        }
      });
    }, { threshold: 0.55 });

    sections.forEach((section) => spyObserver.observe(section));

    window.addEventListener("scroll", () => {
      const doc = document.documentElement;
      const scrollTop = doc.scrollTop || document.body.scrollTop;
      const scrollHeight = doc.scrollHeight - doc.clientHeight;
      const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
      progressBar.style.width = `${progress}%`;
    });

    const driftLevel = document.getElementById("drift-level");
    const driftBars = Array.from(document.querySelectorAll("#drift-chart .drift-bar"));

    function updateDrift() {
      const level = parseInt(driftLevel.value, 10);
      driftBars.forEach((bar, idx) => {
        const height = 30 + idx * 5 + level * 2;
        bar.style.height = `${Math.min(height, 110)}px`;
        bar.classList.toggle("active", idx >= driftBars.length - Math.ceil(level / 2));
      });
    }

    driftLevel.addEventListener("input", updateDrift);
    updateDrift();

    const vt2Shift = document.getElementById("vt2-shift");
    const vt2Window = document.getElementById("vt2-window");
    const vt2Marker = document.getElementById("vt2-marker");

    function updateVT2Shift() {
      const shift = parseInt(vt2Shift.value, 10);
      let center = 70 + shift * 2;
      center = Math.max(25, Math.min(90, center));
      const width = 18;
      vt2Window.style.left = `${center - width / 2}%`;
      vt2Marker.style.left = `${center}%`;
    }

    vt2Shift.addEventListener("input", updateVT2Shift);
    updateVT2Shift();

    const rampStep = document.getElementById("ramp-step");
    const rampSteps = Array.from(document.querySelectorAll("#stepper .step"));
    const rampDetail = document.getElementById("ramp-detail");

    const rampCopy = [
      "Rustig begin: ademrespons volgt vermogen vrijwel lineair.",
      "Ventilatie stijgt licht, nog weinig drift.",
      "VO2 stijgt stevig, ventilatie blijft beheersbaar.",
      "Overgangsgebied richting VT2, ademdruk neemt toe.",
      "Rond VT2 begint VE opnieuw duidelijk te versnellen.",
      "HR kan nog achterlopen terwijl VE versnelt (HR-lag).",
      "Drift wordt snel zichtbaar bij langer aanhouden.",
      "Boven VT2 neemt ademdruk en vermoeidheid snel toe."
    ];

    function updateRamp() {
      const step = parseInt(rampStep.value, 10);
      rampSteps.forEach((el, idx) => {
        el.classList.toggle("active", idx === step - 1);
      });
      const text = rampCopy[step - 1] || rampCopy[0];
      rampDetail.querySelector("p").textContent = text;
    }

    rampStep.addEventListener("input", updateRamp);
    updateRamp();
  </script>
</body>
</html>
"""

HTML_PAGE = HTML_PAGE.replace("{{LOGO_DATA_URI}}", logo_data_uri)

components.html(HTML_PAGE, height=4800, scrolling=True)
```

## pages/4_Energiesystemen.py
```python
import importlib.util
import sys
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Energiesystemen en brandstof - SportMetrics",
    layout="wide",
)

if "site.ui" not in sys.modules:
    ui_path = Path(__file__).resolve().parents[1] / "site" / "ui.py"
    spec = importlib.util.spec_from_file_location("site.ui", ui_path)
    if spec is None or spec.loader is None:
        raise ImportError("Kon site.ui niet laden")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules["site.ui"] = module

from site.ui import inject_global_css, top_nav

inject_global_css()
top_nav(active="Energiesystemen")

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "logo.png"
if not LOGO_PATH.exists():
    LOGO_PATH = BASE_DIR / "1.png"

logo_data_uri = ""
if LOGO_PATH.exists():
    logo_b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    logo_data_uri = f"data:image/png;base64,{logo_b64}"

HTML_PAGE = r"""
<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Energiesystemen en brandstof - SportMetrics</title>
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Spectral:wght@400;600&display=swap");

    :root {
      --sand: #f6f1ea;
      --clay: #e9ddd2;
      --ink: #1e2a2f;
      --muted: #5c6b73;
      --sea: #2f7c85;
      --deep: #0f4c5c;
      --sun: #f4b66a;
      --peach: #f1c9a9;
      --card: #fffdf6;
      --card-strong: #ffffff;
      --border: rgba(30, 42, 47, 0.12);
      --shadow: 0 18px 50px rgba(15, 76, 92, 0.18);
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: "Spectral", "Times New Roman", serif;
      color: var(--ink);
      background: radial-gradient(1200px 800px at 10% -10%, #ffffff 0%, var(--sand) 60%, var(--clay) 100%);
    }

    body::before {
      content: "";
      position: fixed;
      inset: 0;
      background-image: url('{{LOGO_DATA_URI}}');
      background-repeat: repeat;
      background-position: center;
      background-size: 140px;
      opacity: 0.07;
      mix-blend-mode: multiply;
      pointer-events: none;
      z-index: 2;
    }

    .bg-shape {
      position: fixed;
      inset: auto;
      width: 480px;
      height: 480px;
      border-radius: 50%;
      background: radial-gradient(circle at 30% 30%, rgba(47, 124, 133, 0.28), rgba(47, 124, 133, 0.02));
      z-index: -1;
    }
    .bg-shape.one { top: -120px; right: -120px; }
    .bg-shape.two { bottom: -200px; left: -140px; background: radial-gradient(circle, rgba(244, 182, 106, 0.35), rgba(244, 182, 106, 0.02)); }

    nav {
      position: fixed;
      top: 28px;
      right: 26px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 14px 14px;
      box-shadow: var(--shadow);
      z-index: 4;
      max-width: 190px;
    }
    nav h4 {
      margin: 0 0 6px;
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
    }
    .nav-link {
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-decoration: none;
      color: var(--muted);
      display: flex;
      gap: 6px;
      align-items: center;
      transition: color 0.2s ease;
    }
    .nav-link span {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--clay);
      border: 1px solid var(--border);
    }
    .nav-link.active { color: var(--deep); font-weight: 600; }
    .nav-link.active span { background: var(--sea); border-color: var(--sea); }

    .progress {
      height: 6px;
      background: rgba(47, 124, 133, 0.12);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 6px;
    }
    .progress span { display: block; height: 100%; width: 0%; background: var(--sea); transition: width 0.2s ease; }

    main {
      position: relative;
      z-index: 3;
      max-width: 1100px;
      margin: 0 auto;
      padding: 64px 24px 120px;
    }

    section {
      margin: 0 0 72px;
      padding: 36px;
      border-radius: 26px;
      background: var(--card);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      transition: all 0.7s ease;
    }
    body.enable-animations section { opacity: 0; transform: translateY(20px); }
    body.enable-animations section.in-view { opacity: 1; transform: translateY(0); }

    .hero {
      padding: 54px 44px;
      background: linear-gradient(140deg, #ffffff, #f6e7d6);
    }
    .hero h1 {
      font-family: "Space Grotesk", sans-serif;
      font-size: clamp(2.2rem, 3.4vw, 3.4rem);
      margin: 0 0 12px;
      color: var(--deep);
    }
    .hero p {
      font-size: 1.05rem;
      color: var(--muted);
      margin: 0;
      max-width: 720px;
    }
    .hero .hero-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
      margin-top: 28px;
    }
    .hero .stat {
      padding: 16px 18px;
      background: var(--card-strong);
      border-radius: 16px;
      border: 1px solid var(--border);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.95rem;
      color: var(--muted);
    }
    .hero .stat strong { display: block; color: var(--deep); font-size: 1.1rem; }

    h2 {
      font-family: "Space Grotesk", sans-serif;
      margin: 0 0 12px;
      color: var(--deep);
      font-size: 1.8rem;
    }
    h3 {
      font-family: "Space Grotesk", sans-serif;
      margin: 0 0 8px;
      color: var(--deep);
    }
    p { margin: 0 0 14px; color: var(--ink); line-height: 1.55; }
    .muted { color: var(--muted); }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
    }
    .card {
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 16px 18px;
    }
    .pill {
      display: inline-block;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.72rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: 999px;
      margin-bottom: 10px;
    }

    .timeline {
      display: grid;
      grid-template-columns: repeat(3, minmax(120px, 1fr));
      gap: 12px;
      margin-top: 12px;
    }
    .timeline .slot {
      padding: 10px;
      border-radius: 14px;
      background: #eef5f4;
      border: 1px solid rgba(47, 124, 133, 0.22);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.85rem;
    }

    .mixer {
      margin-top: 18px;
      padding: 18px;
      border-radius: 18px;
      border: 1px dashed rgba(47, 124, 133, 0.4);
      background: #eef5f4;
    }
    .mixer label {
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
    }
    .mixer input[type="range"] { width: 100%; margin: 10px 0 6px; }
    .mix-row {
      display: grid;
      grid-template-columns: 130px 1fr 54px;
      gap: 12px;
      align-items: center;
      margin: 10px 0;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.85rem;
    }
    .mix-bar {
      background: #eef5f4;
      border-radius: 999px;
      overflow: hidden;
      height: 10px;
      border: 1px solid rgba(15, 76, 92, 0.2);
    }
    .mix-bar span {
      display: block;
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--sea), var(--deep));
      border-radius: 999px;
      transition: width 0.3s ease;
    }
    .mix-value { text-align: right; color: var(--muted); }

    .fuel-row .mix-bar span { background: linear-gradient(90deg, var(--sun), var(--deep)); }

    .callout {
      background: #f3e4d2;
      border: 1px solid #e8cfae;
      padding: 16px 18px;
      border-radius: 18px;
      font-family: "Space Grotesk", sans-serif;
    }

    .zone-picker {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin: 12px 0 18px;
    }
    .zone-btn {
      border: 1px solid var(--border);
      background: var(--card-strong);
      font-family: "Space Grotesk", sans-serif;
      padding: 8px 14px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .zone-btn.active { background: var(--deep); color: #fff; border-color: var(--deep); }
    .zone-panel { display: none; }
    .zone-panel.active { display: block; }

    .summary {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin-top: 18px;
    }

    .footer {
      text-align: center;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
      color: var(--muted);
    }

    @media (max-width: 980px) {
      nav { display: none; }
      section { padding: 28px; }
      .mix-row { grid-template-columns: 110px 1fr 48px; }
    }

    @media (max-width: 720px) {
      main { padding: 40px 16px 90px; }
      section { padding: 22px; margin: 0 0 48px; }
      .hero { padding: 30px 22px; }
      .hero h1 { font-size: clamp(1.8rem, 6vw, 2.4rem); }
      .hero .hero-grid { grid-template-columns: 1fr; }
      .timeline { grid-template-columns: 1fr; }
      .grid-3 { grid-template-columns: 1fr; }
      .summary { grid-template-columns: 1fr; }
      .mix-row { grid-template-columns: 1fr; gap: 6px; }
      .mix-value { text-align: left; }
      .zone-picker { gap: 8px; }
      .zone-btn { width: 100%; text-align: center; }
    }

    @media (prefers-reduced-motion: reduce) {
      * { scroll-behavior: auto; }
      section { transition: none; }
      body.enable-animations section { opacity: 1; transform: none; }
    }
  </style>
</head>
<body>
  <div class="bg-shape one"></div>
  <div class="bg-shape two"></div>

  <nav aria-label="Navigatie">
    <h4>Route</h4>
    <a class="nav-link" href="#intro" data-section="intro"><span></span>Intro</a>
    <a class="nav-link" href="#atp" data-section="atp"><span></span>ATP</a>
    <a class="nav-link" href="#routes" data-section="routes"><span></span>Routes</a>
    <a class="nav-link" href="#pcr" data-section="pcr"><span></span>ATP-PCr</a>
    <a class="nav-link" href="#anaerobe" data-section="anaerobe"><span></span>Anaerobe</a>
    <a class="nav-link" href="#aerobe" data-section="aerobe"><span></span>Aerobe</a>
    <a class="nav-link" href="#zones" data-section="zones"><span></span>Zones</a>
    <a class="nav-link" href="#samenvatting" data-section="samenvatting"><span></span>Samenvatting</a>
    <div class="progress"><span id="progress-bar"></span></div>
  </nav>

  <main>
    <section id="intro" class="hero" data-title="Intro">
      <span class="pill">Energiesystemen en brandstof</span>
      <h1>Energiesystemen en brandstof: hoe je lichaam vermogen maakt</h1>
      <p>Inspanning is geen "een systeem aan". Je lichaam levert ATP via meerdere routes tegelijk. Wat verandert is de verdeling tussen die routes, afhankelijk van intensiteit, duur, trainingstoestand en brandstofvoorraad.</p>
      <div class="hero-grid">
        <div class="stat"><strong>ATP is de valuta</strong>Elke spiercontractie betaal je met ATP. Je voorraad is klein, dus je maakt het continu opnieuw.</div>
        <div class="stat"><strong>Power vs capaciteit</strong>Hoe hoger de intensiteit, hoe sneller je ATP nodig hebt. Dat duwt je naar routes met hoge power.</div>
        <div class="stat"><strong>Continuum</strong>Er zijn geen harde knips. Alle routes draaien altijd mee, maar de dominantie schuift.</div>
      </div>
    </section>

    <section id="atp" data-title="ATP">
      <h2>ATP als energievaluta</h2>
      <p>Omdat je soms direct maximale power nodig hebt (sprint) en soms lang en laag (duur), bestaan er meerdere routes met verschillende power en capaciteit. De power-capacity trade-off verklaart vrijwel alles in training.</p>
      <div class="timeline">
        <div class="slot">Hoge intensiteit = hoge ATP vraag per seconde</div>
        <div class="slot">Dominantie schuift naar snellere ATP levering</div>
        <div class="slot">Langere duur vraagt om duurzame routes</div>
      </div>
      <div class="mixer" aria-live="polite">
        <label for="intensity">Sleep: intensiteit</label>
        <input id="intensity" type="range" min="0" max="100" value="35" />
        <div class="mix-row">
          <div>ATP-PCr</div>
          <div class="mix-bar"><span id="mix-pcr"></span></div>
          <div class="mix-value" id="mix-pcr-value">0%</div>
        </div>
        <div class="mix-row">
          <div>Anaerobe</div>
          <div class="mix-bar"><span id="mix-anaer"></span></div>
          <div class="mix-value" id="mix-anaer-value">0%</div>
        </div>
        <div class="mix-row">
          <div>Aerobe</div>
          <div class="mix-bar"><span id="mix-aero"></span></div>
          <div class="mix-value" id="mix-aero-value">0%</div>
        </div>
      </div>
    </section>

    <section id="routes" data-title="Routes">
      <h2>De drie hoofd routes (parallel + continu)</h2>
      <div class="grid-3">
        <div class="card">
          <span class="pill">ATP-PCr (alactisch)</span>
          <p><strong>Bron:</strong> fosfocreatine (PCr)</p>
          <p><strong>Dominant venster:</strong> 0-10(15) sec bij maximale inspanning</p>
          <p><strong>Begrenzing:</strong> PCr voorraad is klein en snel leeg</p>
        </div>
        <div class="card">
          <span class="pill">Anaerobe glycolyse</span>
          <p><strong>Substraat:</strong> koolhydraat</p>
          <p><strong>Dominant venster:</strong> 15 sec tot 2-3 min</p>
          <p><strong>Begrenzing:</strong> systeemstress (ionen/H+) en tolerantie</p>
        </div>
        <div class="card">
          <span class="pill">Aerobe oxidatie</span>
          <p><strong>Substraat:</strong> koolhydraat + vet</p>
          <p><strong>Dominant venster:</strong> minuten tot uren</p>
          <p><strong>Begrenzing:</strong> VO2 plafond bij hoge intensiteit en glycogeen bij lange duur</p>
        </div>
      </div>
      <p class="muted">Continuum: alle routes dragen altijd iets bij. Met stijgende intensiteit schuift de dominantie richting routes met hogere ATP productie.</p>
    </section>

    <section id="pcr" data-title="ATP-PCr">
      <h2>ATP-PCr: instant power en waarom herhalingen pijn doen</h2>
      <p>ATP-PCr levert acceleratie en sprintvermogen. PCr buffert de eerste seconden tot tientallen seconden. Maar PCr raakt snel beperkt en herstel kost tijd. Daarom zakt het vermogen bij herhaalde sprints, zelfs als motivatie hoog is.</p>
      <div class="callout">
        Praktisch: bij maximale inspanning wordt PCr vaak binnen 10-15 sec limiterend. Bijna volledig herstel duurt meestal enkele minuten, afhankelijk van herstelintensiteit.
      </div>
    </section>

    <section id="anaerobe" data-title="Anaerobe">
      <h2>Anaerobe koolhydraatafbraak en lactaat</h2>
      <p>Deze route levert snel ATP uit koolhydraten en wordt belangrijk zodra de ATP vraag per seconde hoog wordt. De keerzijde is dat systeemstress snel oploopt (o.a. H+ en ionen), waardoor prestatie en duurzaamheid dalen.</p>
      <div class="grid-3">
        <div class="card">
          <h3>Lactaat is geen afval</h3>
          <p>Lactaat is een transportvorm van energie en kan later weer worden geoxideerd. Denk aan lactate shuttle in andere spiervezels en de hartspier.</p>
        </div>
        <div class="card">
          <h3>Waar het mis gaat</h3>
          <p>Probleem ontstaat wanneer productie en stress sneller stijgen dan oxidatieve verwerking. Dan nemen drift en onhoudbaarheid toe.</p>
        </div>
        <div class="card">
          <h3>Praktisch venster</h3>
          <p>Typisch tientallen seconden tot enkele minuten hard werken. Daarna zie je vaak vermogensval en sterke adem- of HR-drift.</p>
        </div>
      </div>
    </section>

    <section id="aerobe" data-title="Aerobe">
      <h2>Aerobe oxidatie en substraten</h2>
      <p>De aerobe motor is je duurzame ATP fabriek. Je verbrandt altijd een mix van koolhydraat en vet. Naarmate intensiteit stijgt wordt koolhydraat relatief dominanter, omdat vetoxidatie de gevraagde ATP snelheid minder goed kan bijbenen.</p>
      <div class="mixer" aria-live="polite">
        <label for="fuel">Sleep: intensiteit en brandstofmix</label>
        <input id="fuel" type="range" min="0" max="100" value="35" />
        <div class="mix-row fuel-row">
          <div>Koolhydraat</div>
          <div class="mix-bar"><span id="mix-carb"></span></div>
          <div class="mix-value" id="mix-carb-value">0%</div>
        </div>
        <div class="mix-row fuel-row">
          <div>Vet</div>
          <div class="mix-bar"><span id="mix-fat"></span></div>
          <div class="mix-value" id="mix-fat-value">0%</div>
        </div>
      </div>
      <div class="summary">
        <div class="card">
          <h3>Glycogeen als limiter</h3>
          <p>Aerobe koolhydraatverbranding kan stevige intensiteit lang ondersteunen, maar bij lange duur wordt vaak glycogeen limiterend. Richtlijn: 60-120 min bij stevige belasting, afhankelijk van voeding, pacing en training.</p>
        </div>
        <div class="card">
          <h3>Vet als voorraad</h3>
          <p>Vetvoorraad raakt zelden op. Het is vooral bruikbaar bij lage tot matige intensiteit waar de ATP vraag lager is.</p>
        </div>
        <div class="card">
          <h3>FatMax context</h3>
          <p>FatMax is een piek in vetoxidatie, geen vet-only zone. De mix verschuift, niet de aanwezigheid van vet.</p>
        </div>
      </div>
    </section>

    <section id="zones" data-title="Zones">
      <h2>Koppeling naar zones en SportMetrics</h2>
      <p>Zone modellen zijn de praktische vertaalslag van het energiesysteem. SportMetrics koppelt vermogen, hartslag, ademrespons en VO2 om jouw drempelgebieden en aerobe plafond te positioneren. We gebruiken de test om intensiteitsdomeinen en zone-ankers te bepalen die direct naar training vertaalbaar zijn.</p>
      <div class="callout">SportMetrics doet geen lactaatmetingen (prikken), alleen ademgasanalyse.</div>
      <div class="zone-picker" role="tablist" aria-label="Zones">
        <button class="zone-btn active" data-zone="vt1" role="tab">Rond VT1</button>
        <button class="zone-btn" data-zone="vt2" role="tab">Richting VT2/CP</button>
        <button class="zone-btn" data-zone="above" role="tab">Boven VT2/CP</button>
      </div>
      <div class="zone-panel active" id="zone-vt1" role="tabpanel">
        <p>Overwegend aerobe dominantie. Stabieler, zuinig en geschikt voor veel volume.</p>
      </div>
      <div class="zone-panel" id="zone-vt2" role="tabpanel">
        <p>Hogere ATP vraag, meer koolhydraat en glycolytische druk. Meer drift en hogere herstelkosten.</p>
      </div>
      <div class="zone-panel" id="zone-above" role="tabpanel">
        <p>Geen echte steady state. Tijd op beperkte capaciteit, hoge systeemstress.</p>
      </div>
    </section>

    <section id="samenvatting" data-title="Samenvatting">
      <h2>Caption B (kort, inhoudelijk strak)</h2>
      <p>Elke beweging betaal je met ATP. Omdat je ATP voorraad klein is, moet je lichaam het continu bijmaken via meerdere routes die parallel draaien. Het is een continuum: er zijn geen harde afkappunten, maar wel een verschuiving in dominantie wanneer de ATP vraag per seconde stijgt. PCr levert instant power (kort), anaerobe koolhydraatafbraak levert snel ATP (beperkt houdbaar, hogere systeemstress) en aerobe oxidatie levert duurzame energie uit koolhydraat en vet (vet: enorme voorraad, maar lagere maximale ATP snelheid). Lactaat is geen afval, maar een transportvorm van energie die later weer kan worden geoxideerd (o.a. spier en hart).</p>
      <p>Zone modellen zijn de praktische kaart: rond VT1 stabiel en zuinig, richting VT2/CP nemen drift en herstelkosten toe, en daarboven kom je in een domein zonder echte steady state.</p>
      <p class="footer">Wil je deze pagina in een specifieke huisstijl of met extra visuals? Zeg het, dan pas ik het aan.</p>
    </section>
  </main>

  <script>
    document.body.classList.add("enable-animations");

    const sections = Array.from(document.querySelectorAll("section[data-title]"));
    const navLinks = Array.from(document.querySelectorAll(".nav-link"));
    const progressBar = document.getElementById("progress-bar");

    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
        }
      });
    }, { threshold: 0.2 });

    sections.forEach((section) => revealObserver.observe(section));

    const spyObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          navLinks.forEach((link) => link.classList.toggle("active", link.dataset.section === entry.target.id));
        }
      });
    }, { threshold: 0.55 });

    sections.forEach((section) => spyObserver.observe(section));

    window.addEventListener("scroll", () => {
      const doc = document.documentElement;
      const scrollTop = doc.scrollTop || document.body.scrollTop;
      const scrollHeight = doc.scrollHeight - doc.clientHeight;
      const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
      progressBar.style.width = `${progress}%`;
    });

    const intensity = document.getElementById("intensity");
    const fuel = document.getElementById("fuel");

    function normalize(values) {
      const sum = values.reduce((acc, val) => acc + val, 0) || 1;
      return values.map((val) => val / sum);
    }

    function systemMix(value) {
      const pcr = Math.max(0, (value - 70) / 30);
      const anaer = Math.max(0, 1 - Math.abs(value - 60) / 30);
      const aero = Math.max(0, (70 - value) / 70);
      const [p, a, e] = normalize([pcr, anaer, aero]);
      return { p, a, e };
    }

    function updateMix() {
      const value = parseInt(intensity.value, 10);
      const { p, a, e } = systemMix(value);
      document.getElementById("mix-pcr").style.width = `${Math.round(p * 100)}%`;
      document.getElementById("mix-anaer").style.width = `${Math.round(a * 100)}%`;
      document.getElementById("mix-aero").style.width = `${Math.round(e * 100)}%`;
      document.getElementById("mix-pcr-value").textContent = `${Math.round(p * 100)}%`;
      document.getElementById("mix-anaer-value").textContent = `${Math.round(a * 100)}%`;
      document.getElementById("mix-aero-value").textContent = `${Math.round(e * 100)}%`;
    }

    function updateFuel() {
      const value = parseInt(fuel.value, 10);
      const carb = Math.min(1, Math.max(0, value / 100));
      const fat = 1 - carb;
      document.getElementById("mix-carb").style.width = `${Math.round(carb * 100)}%`;
      document.getElementById("mix-fat").style.width = `${Math.round(fat * 100)}%`;
      document.getElementById("mix-carb-value").textContent = `${Math.round(carb * 100)}%`;
      document.getElementById("mix-fat-value").textContent = `${Math.round(fat * 100)}%`;
    }

    intensity.addEventListener("input", updateMix);
    fuel.addEventListener("input", updateFuel);
    updateMix();
    updateFuel();

    const zoneButtons = Array.from(document.querySelectorAll(".zone-btn"));
    const zonePanels = {
      vt1: document.getElementById("zone-vt1"),
      vt2: document.getElementById("zone-vt2"),
      above: document.getElementById("zone-above")
    };

    zoneButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const target = button.dataset.zone;
        zoneButtons.forEach((btn) => btn.classList.toggle("active", btn === button));
        Object.entries(zonePanels).forEach(([key, panel]) => {
          panel.classList.toggle("active", key === target);
        });
      });
    });
  </script>
</body>
</html>
"""

HTML_PAGE = HTML_PAGE.replace("{{LOGO_DATA_URI}}", logo_data_uri)

components.html(HTML_PAGE, height=4200, scrolling=True)
```

## pages/5_Zonemodellen.py
```python
import importlib.util
import sys
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Zone-modellen en Z1-5 - SportMetrics",
    layout="wide",
)

if "site.ui" not in sys.modules:
    ui_path = Path(__file__).resolve().parents[1] / "site" / "ui.py"
    spec = importlib.util.spec_from_file_location("site.ui", ui_path)
    if spec is None or spec.loader is None:
        raise ImportError("Kon site.ui niet laden")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules["site.ui"] = module

from site.ui import inject_global_css, top_nav

inject_global_css()
top_nav(active="Zonemodellen")

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "logo.png"
if not LOGO_PATH.exists():
    LOGO_PATH = BASE_DIR / "1.png"

logo_data_uri = ""
if LOGO_PATH.exists():
    logo_b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    logo_data_uri = f"data:image/png;base64,{logo_b64}"

HTML_PAGE = r"""
<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Zone-modellen en Z1-5 - SportMetrics</title>
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Spectral:wght@400;600&display=swap");

    :root {
      --sand: #f6f1ea;
      --clay: #e9ddd2;
      --ink: #1e2a2f;
      --muted: #5c6b73;
      --sea: #2f7c85;
      --deep: #0f4c5c;
      --sun: #f4b66a;
      --peach: #f1c9a9;
      --card: #fffdf6;
      --card-strong: #ffffff;
      --border: rgba(30, 42, 47, 0.12);
      --shadow: 0 18px 50px rgba(15, 76, 92, 0.18);
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: "Spectral", "Times New Roman", serif;
      color: var(--ink);
      background: radial-gradient(1200px 800px at 10% -10%, #ffffff 0%, var(--sand) 60%, var(--clay) 100%);
    }

    body::before {
      content: "";
      position: fixed;
      inset: 0;
      background-image: url('{{LOGO_DATA_URI}}');
      background-repeat: repeat;
      background-position: center;
      background-size: 140px;
      opacity: 0.07;
      mix-blend-mode: multiply;
      pointer-events: none;
      z-index: 2;
    }

    .bg-shape {
      position: fixed;
      inset: auto;
      width: 480px;
      height: 480px;
      border-radius: 50%;
      background: radial-gradient(circle at 30% 30%, rgba(47, 124, 133, 0.28), rgba(47, 124, 133, 0.02));
      z-index: -1;
    }
    .bg-shape.one { top: -120px; right: -120px; }
    .bg-shape.two { bottom: -200px; left: -140px; background: radial-gradient(circle, rgba(244, 182, 106, 0.35), rgba(244, 182, 106, 0.02)); }

    nav {
      position: fixed;
      top: 28px;
      right: 26px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 14px 14px;
      box-shadow: var(--shadow);
      z-index: 4;
      max-width: 190px;
    }
    nav h4 {
      margin: 0 0 6px;
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
    }
    .nav-link {
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-decoration: none;
      color: var(--muted);
      display: flex;
      gap: 6px;
      align-items: center;
      transition: color 0.2s ease;
    }
    .nav-link span {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--clay);
      border: 1px solid var(--border);
    }
    .nav-link.active { color: var(--deep); font-weight: 600; }
    .nav-link.active span { background: var(--sea); border-color: var(--sea); }

    .progress {
      height: 6px;
      background: rgba(47, 124, 133, 0.12);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 6px;
    }
    .progress span { display: block; height: 100%; width: 0%; background: var(--sea); transition: width 0.2s ease; }

    main {
      position: relative;
      z-index: 3;
      max-width: 1100px;
      margin: 0 auto;
      padding: 64px 24px 120px;
    }

    section {
      margin: 0 0 72px;
      padding: 36px;
      border-radius: 26px;
      background: var(--card);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      transition: all 0.7s ease;
    }
    body.enable-animations section { opacity: 0; transform: translateY(20px); }
    body.enable-animations section.in-view { opacity: 1; transform: translateY(0); }

    .hero {
      padding: 54px 44px;
      background: linear-gradient(140deg, #ffffff, #f6e7d6);
    }
    .hero h1 {
      font-family: "Space Grotesk", sans-serif;
      font-size: clamp(2.2rem, 3.4vw, 3.4rem);
      margin: 0 0 12px;
      color: var(--deep);
    }
    .hero p {
      font-size: 1.05rem;
      color: var(--muted);
      margin: 0;
      max-width: 720px;
    }
    .hero .hero-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
      margin-top: 28px;
    }
    .hero .stat {
      padding: 16px 18px;
      background: var(--card-strong);
      border-radius: 16px;
      border: 1px solid var(--border);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.95rem;
      color: var(--muted);
    }
    .hero .stat strong { display: block; color: var(--deep); font-size: 1.1rem; }

    h2 {
      font-family: "Space Grotesk", sans-serif;
      margin: 0 0 12px;
      color: var(--deep);
      font-size: 1.8rem;
    }
    h3 {
      font-family: "Space Grotesk", sans-serif;
      margin: 0 0 8px;
      color: var(--deep);
    }
    p { margin: 0 0 14px; color: var(--ink); line-height: 1.55; }
    .muted { color: var(--muted); }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
    }
    .card {
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 16px 18px;
    }
    .pill {
      display: inline-block;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.72rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: 999px;
      margin-bottom: 10px;
    }

    .domain-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-top: 18px;
    }
    .domain {
      padding: 14px 16px;
      border-radius: 16px;
      border: 1px solid rgba(47, 124, 133, 0.22);
      background: #eef5f4;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
    }

    .callout {
      background: #f3e4d2;
      border: 1px solid #e8cfae;
      padding: 16px 18px;
      border-radius: 18px;
      font-family: "Space Grotesk", sans-serif;
    }

    .zone-picker {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin: 12px 0 18px;
    }
    .zone-btn {
      border: 1px solid var(--border);
      background: var(--card-strong);
      font-family: "Space Grotesk", sans-serif;
      padding: 8px 14px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .zone-btn.active { background: var(--deep); color: #fff; border-color: var(--deep); }
    .zone-panel { display: none; }
    .zone-panel.active { display: block; }

    .zone-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
    }

    .footer {
      text-align: center;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
      color: var(--muted);
    }

    @media (max-width: 980px) {
      nav { display: none; }
      section { padding: 28px; }
    }

    @media (max-width: 720px) {
      main { padding: 40px 16px 90px; }
      section { padding: 22px; margin: 0 0 48px; }
      .hero { padding: 30px 22px; }
      .hero h1 { font-size: clamp(1.8rem, 6vw, 2.4rem); }
      .hero .hero-grid { grid-template-columns: 1fr; }
      .grid-3 { grid-template-columns: 1fr; }
      .domain-strip { grid-template-columns: 1fr; }
      .zone-grid { grid-template-columns: 1fr; }
      .zone-btn { width: 100%; text-align: center; }
    }

    @media (prefers-reduced-motion: reduce) {
      * { scroll-behavior: auto; }
      section { transition: none; }
      body.enable-animations section { opacity: 1; transform: none; }
    }
  </style>
</head>
<body>
  <div class="bg-shape one"></div>
  <div class="bg-shape two"></div>

  <nav aria-label="Navigatie">
    <h4>Route</h4>
    <a class="nav-link" href="#intro" data-section="intro"><span></span>Intro</a>
    <a class="nav-link" href="#waarom" data-section="waarom"><span></span>Waarom</a>
    <a class="nav-link" href="#ankers" data-section="ankers"><span></span>Ankers</a>
    <a class="nav-link" href="#zones" data-section="zones"><span></span>Z1-5</a>
    <a class="nav-link" href="#praktijk" data-section="praktijk"><span></span>Praktijk</a>
    <div class="progress"><span id="progress-bar"></span></div>
  </nav>

  <main>
    <section id="intro" class="hero" data-title="Intro">
      <span class="pill">Zone-modellen</span>
      <h1>Trainingszones zijn modellen, geen hokjes</h1>
      <p>Zone-indelingen zijn vereenvoudigingen van hoe het lichaam reageert op oplopende inspanningsintensiteit. Of je nu 3, 5, 6 of 7 zones gebruikt: de onderliggende fysiologie verandert niet. In de kern draait het om drie domeinen onder en boven twee drempels: VT1 en VT2.</p>
      <div class="hero-grid">
        <div class="stat"><strong>Zelfde fysiologie</strong>Meer zones betekent een fijnere verdeling, niet een ander systeem.</div>
        <div class="stat"><strong>Drie domeinen</strong>Onder VT1, tussen VT1 en VT2, boven VT2.</div>
        <div class="stat"><strong>Hulpmiddel</strong>Zones maken complexiteit hanteerbaar, niet het doel op zich.</div>
      </div>
    </section>

    <section id="waarom" data-title="Waarom">
      <h2>Waarom zones bestaan</h2>
      <p>Zones bestaan om belasting te doseren, niet om inspanning in hokjes te stoppen. Ze helpen voorkomen dat je alles "grijs" rijdt en maken training herhaalbaar en voorspelbaar.</p>
      <div class="grid-3">
        <div class="card">
          <h3>Rust echt rustig</h3>
          <p>Zones helpen rustige dagen echt rustig te houden.</p>
        </div>
        <div class="card">
          <h3>Hard echt hard</h3>
          <p>Ze maken het makkelijker om intensieve blokken scherp genoeg te doseren.</p>
        </div>
        <div class="card">
          <h3>Gerichte adaptatie</h3>
          <p>Je stuurt aanpassingen in energie- en herstel systemen doelgerichter.</p>
        </div>
      </div>
      <div class="callout">Belangrijk: het aantal zones is minder belangrijk dan de fysiologische domeinen eronder.</div>
    </section>

    <section id="ankers" data-title="Ankers">
      <h2>Waar hangen zones aan</h2>
      <p>Vrijwel alle zone-modellen komen voort uit het 3-fasenmodel, gebaseerd op twee ventilatoire drempels:</p>
      <div class="grid-3">
        <div class="card">
          <h3>VT1</h3>
          <p>Eerste duidelijke verandering in ademhaling en interne belasting. Het anker voor "easy" en basis.</p>
        </div>
        <div class="card">
          <h3>VT2</h3>
          <p>Tweede omslagpunt waarbij langdurig steady werken moeilijk wordt. Het anker voor "hard".</p>
        </div>
        <div class="card">
          <h3>Meetbaar</h3>
          <p>Zichtbaar via ventilatie, lactaatgedrag en te vertalen naar watt, hartslag en pace.</p>
        </div>
      </div>
      <p class="muted">VT1 en VT2 zijn in de praktijk exacter dan vaste HRmax-percentages, omdat percentages groepsgemiddelden zijn.</p>
      <div class="domain-strip">
        <div class="domain"><strong>Onder VT1:</strong> laag en duurzaam</div>
        <div class="domain"><strong>Tussen VT1-VT2:</strong> matig, meer drift</div>
        <div class="domain"><strong>Boven VT2:</strong> hoog, beperkt houdbaar</div>
      </div>
    </section>

    <section id="zones" data-title="Z1-5">
      <h2>Zones 1-5 in de praktijk</h2>
      <p>Klik een zone om de herkenning, het trainingsdoel en de praktische inzet te zien.</p>
      <div class="zone-picker" role="tablist" aria-label="Zones">
        <button class="zone-btn active" data-zone="z1" role="tab">Zone 1</button>
        <button class="zone-btn" data-zone="z2" role="tab">Zone 2</button>
        <button class="zone-btn" data-zone="z3" role="tab">Zone 3</button>
        <button class="zone-btn" data-zone="z4" role="tab">Zone 4</button>
        <button class="zone-btn" data-zone="z5" role="tab">Zone 5</button>
      </div>

      <div class="zone-panel active" id="zone-z1" role="tabpanel">
        <div class="zone-grid">
          <div class="card"><strong>Herkenning</strong><br/>Zeer rustig. Praattempo moeiteloos. Ademhaling laag en stabiel.</div>
          <div class="card"><strong>Wat train je</strong><br/>Herstelcapaciteit, doorbloeding, techniek en cadans zonder metabole stress.</div>
          <div class="card"><strong>Helpt bij</strong><br/>Sneller herstellen, extra volume zonder vermoeidheid, week-na-week consistent trainen.</div>
          <div class="card"><strong>Gebruik</strong><br/>Herstelritten, in- en uitfietsen, rustige dagen tussen intensieve blokken.</div>
          <div class="card"><strong>Let op</strong><br/>Alleen Z1 trainen geeft weinig prestatieprikkel. Ondersteunend, niet compleet.</div>
        </div>
      </div>

      <div class="zone-panel" id="zone-z2" role="tabpanel">
        <div class="zone-grid">
          <div class="card"><strong>Herkenning</strong><br/>Rustig tot steady. Praten kan nog, maar je voelt dat je werkt.</div>
          <div class="card"><strong>Wat train je</strong><br/>Aerobe capaciteit, efficiency en vet-koolhydraat mix.</div>
          <div class="card"><strong>Helpt bij</strong><br/>Uithoudingsvermogen, basis voor intensiever werk, betere pacing.</div>
          <div class="card"><strong>Belangrijk</strong><br/>De naam Z2 verschilt per model. VT1 is het anker om deze zone goed te kalibreren.</div>
        </div>
      </div>

      <div class="zone-panel" id="zone-z3" role="tabpanel">
        <div class="zone-grid">
          <div class="card"><strong>Herkenning</strong><br/>Stevig. Korte zinnen praten lukt net. Comfortabel zwaar.</div>
          <div class="card"><strong>Wat train je</strong><br/>Tempo-uithoudingsvermogen, wedstrijdspecifiek tempo, mentale tolerantie.</div>
          <div class="card"><strong>Helpt bij</strong><br/>Gran fondo, lange solo's, langere beklimmingen, dieselvermogen.</div>
          <div class="card"><strong>Valkuil</strong><br/>Z3 wordt snel de standaard. Te veel Z3 beperkt veel Z2 en kwaliteit in Z4-Z5.</div>
        </div>
      </div>

      <div class="zone-panel" id="zone-z4" role="tabpanel">
        <div class="zone-grid">
          <div class="card"><strong>Herkenning</strong><br/>Hard. Praten lukt nauwelijks. Ademdruk hoog. Rond VT2.</div>
          <div class="card"><strong>Wat train je</strong><br/>Drempelvermogen, tolerantie voor hoge ventilatie, pacing rond wedstrijdintensiteit.</div>
          <div class="card"><strong>Helpt bij</strong><br/>Inspanningen van 20-60 min, tijdritten, lange klimmen, breakaways.</div>
          <div class="card"><strong>Praktisch</strong><br/>Bij korte blokken kan HR achterlopen. Watt en ademrespons zijn vaak betrouwbaarder.</div>
        </div>
      </div>

      <div class="zone-panel" id="zone-z5" role="tabpanel">
        <div class="zone-grid">
          <div class="card"><strong>Herkenning</strong><br/>Zeer hard. Praten kan niet. Korte, scherpe blokken. Ventilatie max.</div>
          <div class="card"><strong>Wat train je</strong><br/>VO2max prikkel, hoog vermogen herhalen onder vermoeidheid, top-end.</div>
          <div class="card"><strong>Helpt bij</strong><br/>Klimvermogen op 3-8 min, sneller herstel tussen harde inspanningen, racesituaties.</div>
          <div class="card"><strong>Belangrijk</strong><br/>Z5 vraagt veel herstel en werkt het best ingebed in veel Z1-Z2.</div>
        </div>
      </div>
    </section>

    <section id="praktijk" data-title="Praktijk">
      <h2>Van zone-model naar training in de praktijk</h2>
      <p>Zone-modellen zijn hulpmiddelen. De echte waarde zit in het fysiologische anker (VT1 en VT2) en hoe je dit vertaalt naar bruikbare trainingsintensiteiten.</p>
      <div class="grid-3">
        <div class="card">
          <h3>Zonder meting</h3>
          <p>Zones vervallen snel in standaardpercentages of gevoel. Dat vergroot ruis.</p>
        </div>
        <div class="card">
          <h3>Best practice</h3>
          <p>3-zone denken voor fysiologie, 5-zone gebruiken voor coachingdetail.</p>
        </div>
        <div class="card">
          <h3>Context</h3>
          <p>Koppel zones aan watt. Gebruik HR en RPE als context voor drift en HR-lag.</p>
        </div>
      </div>
      <div class="callout">Eindboodschap: zones werken pas echt als ze gemeten, gekalibreerd en consequent toegepast worden.</div>
      <p class="footer">Carbs!.</p>
      <p class="footer">We zien je graag bij SportMetrics.</p>
    </section>
  </main>

  <script>
    document.body.classList.add("enable-animations");

    const sections = Array.from(document.querySelectorAll("section[data-title]"));
    const navLinks = Array.from(document.querySelectorAll(".nav-link"));
    const progressBar = document.getElementById("progress-bar");

    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
        }
      });
    }, { threshold: 0.2 });

    sections.forEach((section) => revealObserver.observe(section));

    const spyObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          navLinks.forEach((link) => link.classList.toggle("active", link.dataset.section === entry.target.id));
        }
      });
    }, { threshold: 0.55 });

    sections.forEach((section) => spyObserver.observe(section));

    window.addEventListener("scroll", () => {
      const doc = document.documentElement;
      const scrollTop = doc.scrollTop || document.body.scrollTop;
      const scrollHeight = doc.scrollHeight - doc.clientHeight;
      const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
      progressBar.style.width = `${progress}%`;
    });

    const zoneButtons = Array.from(document.querySelectorAll(".zone-btn"));
    const zonePanels = {
      z1: document.getElementById("zone-z1"),
      z2: document.getElementById("zone-z2"),
      z3: document.getElementById("zone-z3"),
      z4: document.getElementById("zone-z4"),
      z5: document.getElementById("zone-z5")
    };

    zoneButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const target = button.dataset.zone;
        zoneButtons.forEach((btn) => btn.classList.toggle("active", btn === button));
        Object.entries(zonePanels).forEach(([key, panel]) => {
          panel.classList.toggle("active", key === target);
        });
      });
    });
  </script>
</body>
</html>
"""

HTML_PAGE = HTML_PAGE.replace("{{LOGO_DATA_URI}}", logo_data_uri)

components.html(HTML_PAGE, height=4200, scrolling=True)
```

## pages/6_Critical_Power.py
```python
import importlib.util
import sys
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Critical Power - SportMetrics",
    layout="wide",
)

if "site.ui" not in sys.modules:
    ui_path = Path(__file__).resolve().parents[1] / "site" / "ui.py"
    spec = importlib.util.spec_from_file_location("site.ui", ui_path)
    if spec is None or spec.loader is None:
        raise ImportError("Kon site.ui niet laden")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules["site.ui"] = module

from site.ui import inject_global_css, top_nav

inject_global_css()
top_nav(active="Critical Power")

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "logo.png"
if not LOGO_PATH.exists():
    LOGO_PATH = BASE_DIR / "1.png"

logo_data_uri = ""
if LOGO_PATH.exists():
    logo_b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    logo_data_uri = f"data:image/png;base64,{logo_b64}"

CP_IMAGE_PATH = BASE_DIR / "cp_image.png"
cp_image_uri = ""
if CP_IMAGE_PATH.exists():
    cp_b64 = base64.b64encode(CP_IMAGE_PATH.read_bytes()).decode("utf-8")
    cp_image_uri = f"data:image/png;base64,{cp_b64}"

HTML_PAGE = r"""
<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Critical Power - SportMetrics</title>
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Spectral:wght@400;600&display=swap");

    :root {
      --sand: #f6f1ea;
      --clay: #e9ddd2;
      --ink: #1e2a2f;
      --muted: #5c6b73;
      --sea: #2f7c85;
      --deep: #0f4c5c;
      --sun: #f4b66a;
      --peach: #f1c9a9;
      --card: #fffdf6;
      --card-strong: #ffffff;
      --border: rgba(30, 42, 47, 0.12);
      --shadow: 0 18px 50px rgba(15, 76, 92, 0.18);
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: "Spectral", "Times New Roman", serif;
      color: var(--ink);
      background: radial-gradient(1200px 800px at 10% -10%, #ffffff 0%, var(--sand) 60%, var(--clay) 100%);
    }

    .logo-pattern {
      position: fixed;
      inset: 0;
      background-image: url('{{LOGO_DATA_URI}}');
      background-repeat: repeat;
      background-position: center;
      background-size: 140px;
      opacity: 0.07;
      mix-blend-mode: multiply;
      pointer-events: none;
      z-index: 1;
    }

    .bg-shape {
      position: fixed;
      inset: auto;
      width: 480px;
      height: 480px;
      border-radius: 50%;
      background: radial-gradient(circle at 30% 30%, rgba(47, 124, 133, 0.28), rgba(47, 124, 133, 0.02));
      z-index: -1;
    }
    .bg-shape.one { top: -120px; right: -120px; }
    .bg-shape.two { bottom: -200px; left: -140px; background: radial-gradient(circle, rgba(244, 182, 106, 0.35), rgba(244, 182, 106, 0.02)); }

    nav {
      position: fixed;
      top: 28px;
      right: 26px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 14px 14px;
      box-shadow: var(--shadow);
      z-index: 4;
      max-width: 190px;
    }
    nav h4 {
      margin: 0 0 6px;
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
    }
    .nav-link {
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-decoration: none;
      color: var(--muted);
      display: flex;
      gap: 6px;
      align-items: center;
      transition: color 0.2s ease;
    }
    .nav-link span {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--clay);
      border: 1px solid var(--border);
    }
    .nav-link.active { color: var(--deep); font-weight: 600; }
    .nav-link.active span { background: var(--sea); border-color: var(--sea); }

    .progress {
      height: 6px;
      background: rgba(47, 124, 133, 0.12);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 6px;
    }
    .progress span { display: block; height: 100%; width: 0%; background: var(--sea); transition: width 0.2s ease; }

    main {
      position: relative;
      z-index: 3;
      max-width: 1100px;
      margin: 0 auto;
      padding: 64px 24px 120px;
    }

    section {
      margin: 0 0 72px;
      padding: 36px;
      border-radius: 26px;
      background: var(--card);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      transition: all 0.7s ease;
    }
    body.enable-animations section { opacity: 0; transform: translateY(20px); }
    body.enable-animations section.in-view { opacity: 1; transform: translateY(0); }

    .hero {
      padding: 54px 44px;
      background: linear-gradient(140deg, #ffffff, #f6e7d6);
    }
    .hero h1 {
      font-family: "Space Grotesk", sans-serif;
      font-size: clamp(2.2rem, 3.4vw, 3.4rem);
      margin: 0 0 12px;
      color: var(--deep);
    }
    .hero p {
      font-size: 1.05rem;
      color: var(--muted);
      margin: 0;
      max-width: 720px;
    }
    .hero .hero-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
      margin-top: 28px;
    }
    .hero .stat {
      padding: 16px 18px;
      background: var(--card-strong);
      border-radius: 16px;
      border: 1px solid var(--border);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.95rem;
      color: var(--muted);
    }
    .hero .stat strong { display: block; color: var(--deep); font-size: 1.1rem; }

    h2 { font-family: "Space Grotesk", sans-serif; margin: 0 0 12px; color: var(--deep); font-size: 1.8rem; }
    h3 { font-family: "Space Grotesk", sans-serif; margin: 0 0 8px; color: var(--deep); }
    p { margin: 0 0 14px; color: var(--ink); line-height: 1.55; }
    .muted { color: var(--muted); }

    .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 18px; }
    .card { background: var(--card-strong); border: 1px solid var(--border); border-radius: 18px; padding: 16px 18px; }
    .pill { display: inline-block; font-family: "Space Grotesk", sans-serif; font-size: 0.72rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); border: 1px solid var(--border); padding: 4px 10px; border-radius: 999px; margin-bottom: 10px; }

    .slider-box { margin-top: 18px; padding: 18px; border-radius: 18px; border: 1px dashed rgba(47, 124, 133, 0.4); background: #eef5f4; }
    .slider-box label { font-family: "Space Grotesk", sans-serif; font-size: 0.9rem; }
    .slider-box input[type="range"] { width: 100%; margin: 10px 0 6px; }
    .value-tag { display: inline-block; margin-left: 8px; padding: 4px 8px; border-radius: 10px; background: #fff; border: 1px solid var(--border); font-family: "Space Grotesk", sans-serif; font-size: 0.85rem; color: var(--deep); }
    .mix-row { display: grid; grid-template-columns: 130px 1fr 54px; gap: 12px; align-items: center; margin: 10px 0; font-family: "Space Grotesk", sans-serif; font-size: 0.85rem; }
    .mix-bar { background: #eef5f4; border-radius: 999px; overflow: hidden; height: 10px; border: 1px solid rgba(15, 76, 92, 0.2); }
    .mix-bar span { display: block; height: 100%; width: 0%; background: linear-gradient(90deg, var(--sea), var(--deep)); border-radius: 999px; transition: width 0.3s ease; }
    .mix-value { text-align: right; color: var(--muted); }

    .cp-curve { margin-top: 16px; display: grid; grid-template-columns: repeat(8, minmax(60px, 1fr)); gap: 8px; align-items: end; height: 140px; position: relative; }
    .cp-bar { position: relative; z-index: 1; width: 100%; border-radius: 10px 10px 6px 6px; background: rgba(47, 124, 133, 0.18); border: 1px solid rgba(47, 124, 133, 0.3); height: 40%; transition: height 0.3s ease; }
    .cp-bar.active { background: var(--deep); border-color: var(--deep); }
    .cp-line { position: absolute; left: 0; right: 0; height: 2px; background: rgba(15, 76, 92, 0.6); z-index: 3; }
    .cp-line span { position: absolute; right: 6px; top: -16px; font-family: "Space Grotesk", sans-serif; font-size: 0.8rem; color: var(--deep); background: #fff; padding: 2px 6px; border-radius: 8px; border: 1px solid var(--border); }
    .zone-band { position: absolute; left: 0; right: 0; pointer-events: none; font-family: "Space Grotesk", sans-serif; font-size: 0.8rem; color: var(--deep); padding-left: 6px; display: flex; align-items: center; z-index: 0; }
    .steady { background: rgba(85, 214, 170, 0.12); color: #0f4c5c; }
    .nonsteady { background: rgba(244, 182, 106, 0.14); color: #5c3a12; }
    .cp-recovery { position: absolute; left: 0; right: 0; height: 1px; border-top: 1px dashed rgba(15, 76, 92, 0.5); z-index: 2; }
    .cp-recovery span { position: absolute; right: 6px; top: -16px; font-family: "Space Grotesk", sans-serif; font-size: 0.8rem; color: var(--deep); background: #fff; padding: 2px 6px; border-radius: 8px; border: 1px solid var(--border); }

    .context-line { font-size: 0.85rem; color: var(--muted); margin-top: 6px; }
    .context-badges { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 6px; }
    .badge { padding: 4px 8px; border-radius: 10px; border: 1px solid var(--border); background: #fff; font-size: 0.82rem; }
    .tooltip { display: inline-block; margin-top: 8px; color: var(--muted); font-size: 0.85rem; }

    .defs-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; margin-top: 12px; }
    .defs-card { border: 1px solid var(--border); border-radius: 14px; padding: 12px 14px; background: var(--card-strong); }
    .defs-card h3 { margin: 0 0 6px; font-size: 1.05rem; }
    .defs-card ul { margin: 0; padding-left: 18px; }
    .defs-card ul li { margin: 0 0 6px; }

    .vt2-bar { margin-top: 14px; position: relative; height: 16px; border-radius: 999px; background: #eef5f4; border: 1px solid rgba(15, 76, 92, 0.2); overflow: hidden; }
    .vt2-window { position: absolute; top: 0; bottom: 0; width: 18%; left: 62%; border-radius: 999px; background: rgba(47, 124, 133, 0.32); }
    .vt2-marker { position: absolute; top: -4px; width: 2px; height: 24px; background: var(--deep); left: 70%; }

    .callout { background: #f3e4d2; border: 1px solid #e8cfae; padding: 16px 18px; border-radius: 18px; font-family: "Space Grotesk", sans-serif; }

    .summary-list { margin: 0; padding-left: 18px; }
    .summary-list li { margin: 0 0 10px; }

    .footer { text-align: center; font-family: "Space Grotesk", sans-serif; font-size: 0.9rem; color: var(--muted); }

    .cp-image { width: 100%; height: auto; border-radius: 14px; border: 1px solid var(--border); background: #fff; margin-top: 12px; }
    .image-fallback { color: var(--muted); font-size: 0.9rem; margin-top: 8px; }

    .context-line { font-size: 0.85rem; color: var(--muted); margin-top: 6px; }
    .context-badges { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 6px; }
    .badge { padding: 4px 8px; border-radius: 10px; border: 1px solid var(--border); background: #fff; font-size: 0.82rem; }
    .tooltip { display: inline-block; margin-left: 6px; color: var(--muted); font-size: 0.85rem; }

    .defs-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-top: 12px; }
    .defs-card { border: 1px solid var(--border); border-radius: 14px; padding: 12px 14px; background: var(--card-strong); }
    .defs-card h3 { margin: 0 0 6px; font-size: 1.05rem; }
    .defs-card ul { margin: 0; padding-left: 18px; }
    .defs-card ul li { margin: 0 0 6px; }

    @media (max-width: 980px) {
      nav { display: none; }
      section { padding: 28px; }
      .mix-row { grid-template-columns: 110px 1fr 48px; }
    }

    @media (max-width: 720px) {
      main { padding: 40px 16px 90px; }
      section { padding: 18px; margin: 0 0 36px; }
      .hero { padding: 24px 18px; }
      .hero h1 { font-size: clamp(1.8rem, 6vw, 2.4rem); }
      .hero .hero-grid { grid-template-columns: 1fr; }
      .grid-3 { grid-template-columns: 1fr; }
      .mix-row { grid-template-columns: 1fr; gap: 6px; }
      .mix-value { text-align: left; }
      .cp-curve { grid-template-columns: repeat(4, minmax(70px, 1fr)); }
      .card { padding: 14px; }
    }

    @media (prefers-reduced-motion: reduce) {
      * { scroll-behavior: auto; }
      section { transition: none; }
      body.enable-animations section { opacity: 1; transform: none; }
    }
  </style>
</head>
<body>
  <div class="logo-pattern" aria-hidden="true"></div>
  <div class="bg-shape one"></div>
  <div class="bg-shape two"></div>

  <nav aria-label="Navigatie">
    <h4>Route</h4>
    <a class="nav-link" href="#intro" data-section="intro"><span></span>Intro</a>
    <a class="nav-link" href="#definitie" data-section="definitie"><span></span>Definitie</a>
    <a class="nav-link" href="#model" data-section="model"><span></span>Model</a>
    <a class="nav-link" href="#meten" data-section="meten"><span></span>Meten</a>
    <a class="nav-link" href="#casus" data-section="casus"><span></span>Casus</a>
    <a class="nav-link" href="#begrippen" data-section="begrippen"><span></span>Begrippen</a>
    <a class="nav-link" href="#samenvatting" data-section="samenvatting"><span></span>Samenvatting</a>
    <div class="progress"><span id="progress-bar"></span></div>
  </nav>

  <main>
    <section id="intro" class="hero" data-title="Intro">
      <span class="pill">Critical Power</span>
      <h1>Critical Power: jouw duurzame grens in watt</h1>
      <p>CP met W′ beschrijft je gedrag in het zware domein: wat je duurzaam kunt leveren en hoeveel boven-CP budget je hebt. Krachtige aanvulling op VT1/VT2 en VO2max.</p>
      <div class="hero-grid">
        <div class="stat"><strong>Duurzame grens</strong>CP is waar je naartoe trekt als de inspanning langer wordt.</div>
        <div class="stat"><strong>Boven-CP budget</strong>W′ verklaart aanvallen, heuvels en surges.</div>
        <div class="stat"><strong>Praktisch</strong>Helpt pacing en intervalontwerp onderbouwen.</div>
      </div>
    </section>

    <section id="definitie" data-title="Definitie">
      <h2>Wat CP en W′ zijn</h2>
      <div class="grid-3">
        <div class="card">
          <h3>CP</h3>
          <p>Duurzame grens in het zware domein. Boven CP geen echte steady state.</p>
        </div>
        <div class="card">
          <h3>W′</h3>
          <p>Eindig boven-CP budget. Elke extra watt boven CP verbruikt W′ sneller.</p>
        </div>
        <div class="card">
          <h3>Waarom relevant</h3>
          <p>Verklaart waarom je kunt aanvallen én waarom je kunt opblazen.</p>
        </div>
      </div>
      <img class="cp-image" id="cp-image" src="{{CP_IMAGE_URI}}" alt="Critical Power visual" />
      <div class="image-fallback">Als de visual niet laadt: CP = grens, W′ = budget boven die grens.</div>
    </section>

    <section id="model" data-title="Model">
      <h2>Critical Power-model (constante belasting)</h2>
      <p>Geldig bij constant vermogen boven CP. Boven CP wordt W′ lineair verbruikt; onder CP kan W′ herstellen.</p>
      <p class="muted">CP is de steady-state grens; alles daarboven is non-steady en tijdelijk.</p>
      <div class="slider-box" aria-live="polite">
        <label for="cp-input">Jouw CP (W) <span id="cp-val" class="value-tag"></span></label>
        <input id="cp-input" type="range" min="150" max="400" value="280" />
        <div class="context-badges">
          <span class="badge">&lt; 200 W: recreatief</span>
          <span class="badge">200–260 W: getraind</span>
          <span class="badge">260–320 W: competitief</span>
          <span class="badge">&gt; 320 W: zeer hoog niveau</span>
        </div>
        <p class="context-line">Indicatief, geen norm. Individuele waarden verschillen sterk.</p>
        <label for="wprime-input">Jouw W′ (kJ) <span id="wprime-val" class="value-tag"></span></label>
        <input id="wprime-input" type="range" min="8" max="30" value="15" />
        <label for="power-input">Vermogen (W) <span id="power-val" class="value-tag"></span></label>
        <input id="power-input" type="range" min="200" max="450" value="320" />
        <div class="mix-row">
          <div>ΔP = P − CP</div>
          <div class="mix-bar"><span id="mix-delta"></span></div>
          <div class="mix-value" id="delta-val">0 W</div>
        </div>
        <div class="mix-row">
          <div>Theoretische volhoudtijd (mm:ss)</div>
          <div class="mix-bar"><span id="mix-time"></span></div>
          <div class="mix-value" id="mix-time-value">0</div>
        </div>
        <div class="mix-row">
          <div>W′ gebruik (kJ)</div>
          <div class="mix-bar"><span id="mix-wprime"></span></div>
          <div class="mix-value" id="mix-wprime-value">0</div>
        </div>
      </div>

      <div class="slider-box" aria-live="polite">
        <label for="duration-input">Doelduur (s) voor een klim / blok <span id="duration-val" class="value-tag"></span></label>
        <input id="duration-input" type="range" min="120" max="900" value="360" />
        <div class="mix-row">
          <div>Maximaal vol te houden vermogen</div>
          <div class="mix-bar"><span id="mix-adv"></span></div>
          <div class="mix-value" id="mix-adv-value">0 W</div>
        </div>
        <p class="muted">Bij constante belasting en volledige inzet.</p>
      </div>

      <p class="tooltip">ⓘ Critical Power is individueel en afhankelijk van trainingstoestand, testprotocol en meetmethode; waarden zijn niet 1-op-1 vergelijkbaar.</p>

      <div class="cp-curve" id="cp-curve" aria-hidden="true">
        <div class="cp-bar"></div><div class="cp-bar"></div><div class="cp-bar"></div><div class="cp-bar"></div>
        <div class="cp-bar"></div><div class="cp-bar"></div><div class="cp-bar"></div><div class="cp-bar"></div>
        <div class="zone-band steady" id="steady-zone"><span>≤ CP: steady-state, W′ kan herstellen</span></div>
        <div class="zone-band nonsteady" id="nonsteady-zone"><span>&gt; CP: non-steady, W′ verbruik</span></div>
        <div class="cp-recovery" id="cp-recovery"><span>W′ herstel mogelijk onder CP</span></div>
        <div class="cp-line" id="cp-line"><span>CP</span></div>
      </div>
    </section>

    <section id="meten" data-title="Meten">
      <h2>Hoe wij CP meten</h2>
      <div class="grid-3">
        <div class="card">
          <h3>Efforts</h3>
          <p>3–4 max efforts in 3–20 min (bijv. 3, 5, 12, 20 min).</p>
        </div>
        <div class="card">
          <h3>Kwaliteit</h3>
          <p>Bij voorkeur op aparte dagen; vermoeidheid vertekent vooral W′.</p>
        </div>
        <div class="card">
          <h3>Model</h3>
          <p>We nemen de beste gemiddelde power per effort → CP + W′.</p>
        </div>
      </div>
      <div class="callout">CP/W′ komt uit je power–duration gedrag en maakt expliciet wat er boven je duurzame grens gebeurt.</div>
    </section>

    <section id="begrippen" data-title="Begrippen">
      <h2>Wat betekenen de variabelen?</h2>
      <div class="defs-grid">
        <div class="defs-card">
          <h3>Vermogen (P, W)</h3>
          <ul>
            <li>Mechanische energie per seconde (1 W = 1 J/s).</li>
            <li>Hoger vermogen = meer energie per tijdseenheid.</li>
            <li>Gemeten met vermogensmeter (crank/pedaal/naaf/trainer); kalibreer/zero-offset voor nauwkeurigheid.</li>
            <li>Onafhankelijk van snelheid of terrein.</li>
          </ul>
        </div>
        <div class="defs-card">
          <h3>Critical Power (CP)</h3>
          <ul>
            <li>Hoogste vermogen dat langdurig vol te houden is zonder voortdurende uitputting.</li>
            <li>Grens tussen steady-state en non-steady-state (verwant aan VT2/MLSS).</li>
            <li>Typisch ±30–60 minuten vol te houden.</li>
          </ul>
        </div>
        <div class="defs-card">
          <h3>W′ (“W-prime”)</h3>
          <ul>
            <li>Beperkte extra energie boven CP (kJ); model van anaerobe capaciteit.</li>
            <li>Verbruikt bij P &gt; CP; kan (gedeeltelijk) herstellen bij P &lt;= CP.</li>
            <li>Geen vaste “tank”, maar een modelmatige tijdelijke capaciteit.</li>
          </ul>
        </div>
        <div class="defs-card">
          <h3>P</h3>
          <ul>
            <li>Gekozen of geleverd vermogen.</li>
            <li>P ≤ CP: steady-state mogelijk; P &gt; CP: W′ wordt aangesproken.</li>
          </ul>
        </div>
        <div class="defs-card">
          <h3>Tijd (t)</h3>
          <ul>
            <li>Duur (s) dat een vermogen wordt geleverd.</li>
            <li>Hoe groter ΔP, hoe sneller W′ opgaat en hoe korter de maximale volhoudtijd.</li>
          </ul>
        </div>
      </div>

      <h3>Formules (constante belasting boven CP)</h3>
      <ul class="summary-list">
        <li>W′-verbruik: W′ = (P − CP) × t</li>
        <li>Volhoudtijd: t = W′ / (P − CP)</li>
      </ul>
      <p class="muted">Alleen geldig bij constant vermogen; vereenvoudigd model.</p>
      <p class="muted">In praktijk wisselt vermogen voortdurend; CP-model helpt plannen/begrijpen, niet exact voorspellen.</p>
      <p class="muted">W′ herstelt alleen bij belasting onder of rond CP; hersteltempo hangt af van hoe ver je onder CP zit.</p>
    </section>

    <section id="casus" data-title="Casus">
      <h2>Casus: klim van ~6 minuten</h2>
      <p>CP = 280 W, W′ = 15 kJ. Bij 330 W is (P−CP)=50 W → tijd = 15.000/50 = 300 s (5:00) → te hoog voor 6 min. Bij 315 W is tijd ≈ 7:09 → realistischer.</p>
      <div class="callout">Gebruik CP/W′ om pacing te plannen en intervalwerk te doseren.</div>
    </section>

    <section id="samenvatting" data-title="Samenvatting">
      <h2>Samenvatting</h2>
      <ul class="summary-list">
        <li>CP = duurzame grens in het zware domein; W′ = boven-CP budget.</li>
        <li>Model: tijd = W′/(P−CP) en W′-gebruik = (P−CP)×tijd → direct toepasbaar.</li>
        <li>Meten met meerdere max efforts (3–20 min) levert reproduceerbare CP/W′.</li>
        <li>Gebruik voor pacing, intervalontwerp en om “opblazen” te voorkomen.</li>
      </ul>
      <p class="footer">We zien je graag bij SportMetrics.</p>
    </section>
  </main>

  <script>
    document.body.classList.add("enable-animations");

    const sections = Array.from(document.querySelectorAll("section[data-title]"));
    const navLinks = Array.from(document.querySelectorAll(".nav-link"));
    const progressBar = document.getElementById("progress-bar");

    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) entry.target.classList.add("in-view");
      });
    }, { threshold: 0.2 });
    sections.forEach((section) => revealObserver.observe(section));

    const spyObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          navLinks.forEach((link) => link.classList.toggle("active", link.dataset.section === entry.target.id));
        }
      });
    }, { threshold: 0.55 });
    sections.forEach((section) => spyObserver.observe(section));

    window.addEventListener("scroll", () => {
      const doc = document.documentElement;
      const scrollTop = doc.scrollTop || document.body.scrollTop;
      const scrollHeight = doc.scrollHeight - doc.clientHeight;
      const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
      progressBar.style.width = `${progress}%`;
    });

    const cpInput = document.getElementById("cp-input");
    const wprimeInput = document.getElementById("wprime-input");
    const powerInput = document.getElementById("power-input");
    const durationInput = document.getElementById("duration-input");

    function formatTime(seconds) {
      const m = Math.floor(seconds / 60);
      const s = Math.max(0, Math.round(seconds % 60));
      return `${m}:${s.toString().padStart(2, "0")}`;
    }

    function updateModel() {
      const cp = parseInt(cpInput.value, 10);
      const wprime = parseInt(wprimeInput.value, 10) * 1000; // to J
      const power = parseInt(powerInput.value, 10);
      const above = power - cp;
      const wprimeKj = wprime / 1000;

      const cpVal = document.getElementById("cp-val");
      const wpVal = document.getElementById("wprime-val");
      const powVal = document.getElementById("power-val");
      if (cpVal) cpVal.textContent = `${cp} W`;
      if (wpVal) wpVal.textContent = `${wprimeKj.toFixed(1)} kJ`;
      if (powVal) powVal.textContent = `${power} W`;

      const deltaVal = document.getElementById("delta-val");
      const deltaBar = document.getElementById("mix-delta");
      const deltaAbs = Math.abs(above);
      const deltaSign = above >= 0 ? "+" : "−";
      if (deltaVal) deltaVal.textContent = `${deltaSign}${deltaAbs} W`;
      if (deltaBar) {
        const width = Math.min(100, (deltaAbs / 200) * 100);
        deltaBar.style.width = `${width}%`;
      }

      if (above <= 0) {
        document.getElementById("mix-time").style.width = "0%";
        document.getElementById("mix-wprime").style.width = "0%";
        document.getElementById("mix-time-value").textContent = "∞";
        document.getElementById("mix-wprime-value").textContent = "0 kJ";
      } else {
        const timeSec = wprime / above;
        document.getElementById("mix-time").style.width = `${Math.min(100, (timeSec / 600) * 100)}%`;
        document.getElementById("mix-wprime").style.width = `${Math.min(100, (wprimeKj / 30) * 100)}%`;
        document.getElementById("mix-time-value").textContent = formatTime(timeSec);
        document.getElementById("mix-wprime-value").textContent = `${wprimeKj.toFixed(1)} kJ`;
      }

      const bars = Array.from(document.querySelectorAll("#cp-curve .cp-bar"));
      bars.forEach((bar, idx) => {
        const t = (idx + 2) * 60;
        const p = cp + wprime / Math.max(1, t);
        const norm = Math.min(1, (p - 150) / 350);
        bar.style.height = `${30 + norm * 70}%`;
        bar.classList.toggle("active", Math.abs(p - power) < 10);
      });

      const cpLine = document.getElementById("cp-line");
      const steadyZone = document.getElementById("steady-zone");
      const nonsteadyZone = document.getElementById("nonsteady-zone");
      const cpRecovery = document.getElementById("cp-recovery");
      if (cpLine) {
        const norm = Math.min(1, (cp - 150) / 350);
        const pct = 30 + norm * 70;
        cpLine.style.bottom = `${pct}%`;
        if (steadyZone) {
          steadyZone.style.height = `${pct}%`;
          steadyZone.style.bottom = "0";
        }
        if (nonsteadyZone) {
          const topPct = 100 - pct;
          nonsteadyZone.style.height = `${topPct}%`;
          nonsteadyZone.style.bottom = `${pct}%`;
        }
        if (cpRecovery) {
          const recPct = Math.max(5, pct - 8);
          cpRecovery.style.bottom = `${recPct}%`;
        }
      }
    }

    function updateAdvice() {
      const cp = parseInt(cpInput.value, 10);
      const wprime = parseInt(wprimeInput.value, 10) * 1000;
      const dur = parseInt(durationInput.value, 10);
      const advPower = cp + wprime / dur;
      const durVal = document.getElementById("duration-val");
      if (durVal) durVal.textContent = `${dur} s`;
      document.getElementById("mix-adv").style.width = `${Math.min(100, (advPower - 150) / 3.5)}%`;
      document.getElementById("mix-adv-value").textContent = `${Math.round(advPower)} W`;
    }

    [cpInput, wprimeInput, powerInput].forEach((el) => el.addEventListener("input", () => { updateModel(); updateAdvice(); }));
    durationInput.addEventListener("input", updateAdvice);

    updateModel();
    updateAdvice();
  </script>
</body>
</html>
"""

HTML_PAGE = HTML_PAGE.replace("{{LOGO_DATA_URI}}", logo_data_uri)
HTML_PAGE = HTML_PAGE.replace("{{CP_IMAGE_URI}}", cp_image_uri)

components.html(HTML_PAGE, height=4800, scrolling=True)
```

## pages/7_Mijn_SportTesting_AI.py
```python
import importlib.util
import sys
from pathlib import Path

import streamlit as st
import google.generativeai as genai
import pypdf
import docx
import os

# Pagina instellingen
st.set_page_config(page_title="Sportfysioloog AI", page_icon="🚴‍♂️")

if "site.ui" not in sys.modules:
    ui_path = Path(__file__).resolve().parents[1] / "site" / "ui.py"
    spec = importlib.util.spec_from_file_location("site.ui", ui_path)
    if spec is None or spec.loader is None:
        raise ImportError("Kon site.ui niet laden")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules["site.ui"] = module

from site.ui import inject_global_css, top_nav

inject_global_css()
top_nav(active="Mijn SportTesting AI")

st.title("🚴‍♂️ Jouw Wieler & Hardloop Expert")

# --- 1. CONFIGURATIE & API ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"].strip()
        genai.configure(api_key=api_key)
    else:
        st.error("Geen API Key gevonden. Voeg deze toe aan secrets.toml")
        st.stop()
except Exception as e:
    st.error(f"Error bij configureren API: {e}")
    st.stop()

# --- 2. KENNIS LADEN (PDF & DOCX) ---
@st.cache_resource
def load_all_knowledge():
    """Zoekt automatisch naar alle PDF en DOCX bestanden en leest ze."""
    combined_text = ""
    # We kijken in de huidige map naar alle bestanden
    for filename in os.listdir("."):
        try:
            # Als het een PDF is
            if filename.lower().endswith(".pdf"):
                reader = pypdf.PdfReader(filename)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        combined_text += text + "\n"
            
            # Als het een Word bestand is
            elif filename.lower().endswith(".docx"):
                doc = docx.Document(filename)
                for para in doc.paragraphs:
                    combined_text += para.text + "\n"
                
        except Exception as e:
            print(f"Kon bestand {filename} niet lezen: {e}")

    return combined_text

# Hier laden we alles in (gebeurt onzichtbaar voor de klant)
knowledge_base = load_all_knowledge()

# --- 3. DE AI INSTRUCTIES ---
SYSTEM_PROMPT = f"""
ROL: Je bent een expert sportfysioloog van SportMetrics.

BRONMATERIAAL:
Je hebt toegang tot specifieke literatuur over trainingsleer (zie hieronder).
Gebruik DEZE INFORMATIE als de absolute waarheid.

=== START LITERATUUR ===
{knowledge_base}
=== EINDE LITERATUUR ===

BELANGRIJKE REGELS:
1. SportMetrics doet GEEN lactaatmetingen (prikken), alleen ademgasanalyse.
2. Gebruik de principes (zoals Seiler zones) zoals beschreven in de geüploade literatuur.
3. Wees praktisch, enthousiast en gebruik bulletpoints.
4. Geen medisch advies.
5. Geef altijd een props aan de persoon voor de test en bedank dat hij of zij dat bij SportMetrics heeft gedaan.
"""

# Model laden
try:
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash", 
        system_instruction=SYSTEM_PROMPT
    )
except Exception as e:
    st.error(f"Model fout: {e}")

# --- 4. CHAT INTERFACE ---

if "messages" not in st.session_state:
    st.session_state.messages = []
    
    # We splitsen de tekst in twee delen om de foutmelding te voorkomen
    deel1 = "Hoi! Ik geef antwoord op basis van mijn AI-kennis en de best beschikbare literatuur over trainingsleer."
    deel2 = "\n\nUpload je testresultaten of stel direct een vraag!"
    intro = deel1 + deel2
    
    st.session_state.messages.append({"role": "assistant", "content": intro})

# -- MOBIELVRIENDELIJKE UPLOAD KNOP VOOR KLANTEN --
with st.expander("📄 Klik hier om een PDF Rapport te uploaden", expanded=False):
    uploaded_file = st.file_uploader("Kies je testresultaten", type="pdf", key="mobile_uploader")
    
    if uploaded_file is not None:
        try:
            reader = pypdf.PdfReader(uploaded_file)
            client_pdf_text = ""
            for page in reader.pages:
                client_pdf_text += page.extract_text() + "\n"
            
            st.session_state['last_uploaded_text'] = client_pdf_text
            st.success("✅ Rapport ontvangen! Typ hieronder je vraag.")
        except Exception as e:
            st.error(f"Fout bij lezen rapport: {e}")

# Toon geschiedenis
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input veld
prompt = st.chat_input("Stel je vraag of zeg 'Maak mijn zones'...")

if prompt:
    extra_context = ""
    # Kijk of er net een bestand is geüpload door de klant
    if 'last_uploaded_text' in st.session_state:
        extra_context = f"\n\nHIER IS HET RAPPORT VAN DE KLANT:\n{st.session_state['last_uploaded_text']}\n\n"
        # We verwijderen het uit de sessie zodat het niet bij elke volgende vraag opnieuw wordt meegestuurd als 'nieuw'
        del st.session_state['last_uploaded_text']

    full_prompt_for_ai = prompt + extra_context

    # Gebruiker bericht toevoegen aan sessie en scherm
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            # 1. ANIMATIE: Fietsjes die van links naar rechts bewegen
            loading_placeholder = st.empty()
            loading_placeholder.markdown("""
            <div style="width: 100%; overflow: hidden; padding: 10px 0;">
                <div style="display: inline-block; white-space: nowrap; animation: moveRight 3s linear infinite;">
                    🚴‍♂️ 💨 🚴‍♂️ 💨 🚴‍♂️
                </div>
            </div>
            <style>
                @keyframes moveRight {
                    0% { transform: translateX(-20%); }
                    100% { transform: translateX(120%); }
                }
            </style>
            """, unsafe_allow_html=True)

            # Antwoord genereren
            response = model.generate_content(full_prompt_for_ai)
            
            # Animatie weghalen (leegmaken)
            loading_placeholder.empty()

            # 2. DISCLAIMER TOEVOEGEN
            final_text = response.text + "\n\n---\n*Disclaimer: Dit is geen medisch advies.*"
            
            # Antwoord tonen
            st.markdown(final_text)
            
            # Opslaan in geschiedenis
            st.session_state.messages.append({"role": "assistant", "content": final_text})
            
    except Exception as e:
        st.error(f"De AI reageert niet of er is een fout opgetreden: {e}")
```


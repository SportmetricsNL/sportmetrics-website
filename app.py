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

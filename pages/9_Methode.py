import importlib.util
import sys
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Methode - SportMetrics",
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
top_nav(active="Methode")

CTA_URL = "mailto:folkertvinke@gmail.com"

st.markdown(
    """
    <style>
      .method-hero {
        margin-top: 0.2rem;
        padding: 1.2rem 1.25rem;
        border-radius: 1.1rem;
        border: 1px solid #d5e2e7;
        background: linear-gradient(140deg, #f5fafb 0%, #e6f1f3 100%);
        box-shadow: 0 14px 26px rgba(18, 62, 74, 0.08);
      }

      .method-hero h1 {
        margin: 0;
        color: #194751;
        font-size: clamp(1.75rem, 3.1vw, 2.5rem);
      }

      .method-hero p {
        margin: 0.55rem 0 0;
        color: #2e5f69;
      }

      .method-section {
        margin-top: 1.2rem;
        padding: 1.15rem;
        border-radius: 1rem;
        border: 1px solid #d5e2e6;
        background: rgba(255, 255, 255, 0.9);
        box-shadow: 0 10px 22px rgba(21, 65, 77, 0.07);
      }

      .method-section h2 {
        margin: 0;
        color: #1f505a;
        font-size: 1.28rem;
      }

      .method-card {
        height: 100%;
        padding: 1rem;
        border-radius: 0.92rem;
        border: 1px solid #d8e4e8;
        background: #ffffff;
      }

      .method-card h3 {
        margin: 0;
        color: #205561;
        font-size: 1.05rem;
      }

      .method-card p {
        margin: 0.55rem 0 0;
        color: #315a65;
        line-height: 1.58;
      }

      .method-note {
        margin-top: 0.95rem;
        padding: 0.95rem 1rem;
        border-radius: 0.9rem;
        border: 1px dashed #acc5cc;
        background: #eef6f7;
        color: #2e5861;
        line-height: 1.6;
      }

      .method-cta {
        margin-top: 0.8rem;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.72rem 1.2rem;
        border-radius: 999px;
        background: linear-gradient(140deg, #2d7c85 0%, #3d9199 100%);
        color: #ffffff !important;
        text-decoration: none !important;
        font-weight: 700;
        letter-spacing: 0.01em;
        box-shadow: 0 10px 22px rgba(22, 74, 87, 0.22);
      }

      .method-footer {
        margin-top: 1.7rem;
        text-align: center;
        color: #4a6c74;
        font-weight: 600;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="method-hero">
      <h1>Methode</h1>
      <p>Van testafname naar praktische trainingssturing. Je werkt met duidelijke kernconcepten en vertaalt data naar concrete keuzes.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<section class="method-section"><h2>Zo werkt de methode</h2></section>', unsafe_allow_html=True)
step_a, step_b, step_c = st.columns(3, gap="large")

with step_a:
    st.markdown(
        """
        <article class="method-card">
          <h3>1. Meten</h3>
          <p>We bepalen jouw VO2max, drempelwaardes, energieverdeling en zones met een wetenschappelijk onderbouwde inspanningstest.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with step_b:
    st.markdown(
        """
        <article class="method-card">
          <h3>2. Begrijpen</h3>
          <p>Je rapport vertaalt je resultaten naar duidelijke inzichten over trainingsintensiteit, opbouw en herstelmomenten.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with step_c:
    st.markdown(
        """
        <article class="method-card">
          <h3>3. Toepassen</h3>
          <p>Met de AI-coach en de kernbegrippen bovenin kun je de uitkomsten direct toepassen op je eigen situatie.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<section class="method-section"><h2>Kernbegrippen interactief</h2></section>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="method-note">
      Start hier jouw leerproces. De kernbegrippen bovenin zijn interactief uitgelegd, zodat je ze kunt toepassen op je eigen situatie.
      Loop alle kernconcepten door voor een volledig beeld van je testresultaten en trainingssturing.
    </div>
    """,
    unsafe_allow_html=True,
)

core_row_1 = st.columns(3, gap="large")
with core_row_1[0]:
    st.page_link("pages/1_VO2max.py", label="VO2max", width="stretch")
with core_row_1[1]:
    st.page_link("pages/2_VT1.py", label="VT1", width="stretch")
with core_row_1[2]:
    st.page_link("pages/3_VT2.py", label="VT2", width="stretch")

core_row_2 = st.columns(3, gap="large")
with core_row_2[0]:
    st.page_link("pages/4_Energiesystemen.py", label="Energiesystemen", width="stretch")
with core_row_2[1]:
    st.page_link("pages/5_Zonemodellen.py", label="Zonemodellen", width="stretch")
with core_row_2[2]:
    st.page_link("pages/6_Critical_Power.py", label="Critical Power", width="stretch")

st.markdown('<section class="method-section"><h2>AI-chatbot ondersteuning</h2></section>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="method-note">
      Wil je alsnog een vraag stellen? Dan kun je altijd terecht bij de AI-chatbot rechtsboven.
      De chatbot is getraind op recente literatuur en helpt je met trainingsinrichting, periodisering en het interpreteren van zones.
      Ook nadat je je eigen rapport hebt geupload, helpt hij je graag verder in jouw fietstraject.
    </div>
    """,
    unsafe_allow_html=True,
)

st.page_link("pages/4_Energiesystemen.py", label="Start met Energiesystemen", width="stretch")
st.markdown(f'<a class="method-cta" href="{CTA_URL}">Klik hier voor je afspraak</a>', unsafe_allow_html=True)
st.markdown('<p class="method-footer">We zien je snel bij SportMetrics.</p>', unsafe_allow_html=True)

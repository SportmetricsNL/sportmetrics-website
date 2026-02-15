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

from site.ui import inject_global_css, plan_test_button, render_plan_dialog_if_open, top_nav

inject_global_css()
top_nav(active="Methode")
render_plan_dialog_if_open(page_id="methode")

st.markdown(
    """
    <style>
      .method-hero {
        margin-top: 0.35rem;
        padding: clamp(2.2rem, 4.2vw, 3.2rem) clamp(1.2rem, 2.8vw, 2rem);
        border-radius: 1.1rem;
        border: 1px solid #d5e2e6;
        background: linear-gradient(140deg, #f7fbfc 0%, #e9f3f5 100%);
        box-shadow: 0 14px 30px rgba(18, 62, 74, 0.08);
      }

      .method-hero h1 {
        margin: 0;
        font-size: clamp(2rem, 4.3vw, 2.95rem);
        color: #153f48;
        line-height: 1.04;
      }

      .method-hero p {
        margin: 0.82rem 0 0;
        max-width: 48ch;
        color: #2b5d66;
        line-height: 1.6;
      }

      .method-section {
        margin-top: 1.5rem;
        padding: 1.2rem;
        border-radius: 1rem;
        border: 1px solid #d5e2e6;
        background: rgba(255, 255, 255, 0.92);
        box-shadow: 0 10px 24px rgba(21, 65, 77, 0.07);
      }

      .method-section h2 {
        margin: 0;
        color: #1f505a;
        font-size: 1.3rem;
      }

      .method-sub {
        margin: 0.44rem 0 0;
        color: #5a747d;
      }

      .method-step {
        height: 100%;
        padding: 1rem;
        border-radius: 0.92rem;
        border: 1px solid #d8e4e8;
        background: #ffffff;
      }

      .method-step h3 {
        margin: 0;
        color: #215763;
        font-size: 1.06rem;
      }

      .method-step p {
        margin: 0.46rem 0 0;
        color: #315a65;
        line-height: 1.55;
      }

      .method-list {
        margin: 0.52rem 0 0;
        padding-left: 1rem;
      }

      .method-list li {
        margin: 0.26rem 0;
        color: #315a65;
      }

      .method-info {
        margin-top: 0.92rem;
        padding: 0.82rem 0.92rem;
        border-radius: 0.85rem;
        border: 1px solid #d8e6ea;
        background: #f3f9fa;
        color: #315a65;
        line-height: 1.54;
      }

      .method-link-note {
        margin-top: 0.56rem;
        color: #678089;
        font-size: 0.88rem;
      }

      .method-mini {
        height: 100%;
        padding: 0.88rem;
        border-radius: 0.86rem;
        border: 1px solid #d8e4e8;
        background: #ffffff;
      }

      .method-mini h3 {
        margin: 0;
        color: #1f505a;
        font-size: 0.97rem;
      }

      .method-mini ul {
        margin: 0.5rem 0 0;
        padding-left: 1rem;
      }

      .method-mini li {
        margin: 0.2rem 0;
        color: #315a65;
        font-size: 0.92rem;
      }

      .method-compact {
        margin-top: 0.9rem;
        padding: 0.86rem 0.96rem;
        border-radius: 0.86rem;
        border: 1px solid #d8e6ea;
        background: #f2f8f9;
        color: #315a65;
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
      <h1>Zo meten we jouw fysiologie.</h1>
      <p>Geen schattingen, maar een gestructureerde inspanningstest die direct vertaald wordt naar bruikbare trainingszones.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

hero_pad_l, hero_left, hero_right, hero_pad_r = st.columns([0.06, 0.44, 0.44, 0.06], gap="small")
with hero_left:
    st.link_button("Bekijk Aanbod", "/Aanbod", use_container_width=True)
with hero_right:
    plan_test_button("Plan je meting", key="method_hero_plan", page_id="methode", use_container_width=True)

st.markdown(
    """
    <section class="method-section">
      <h2>Hoe werkt het?</h2>
      <p class="method-sub">Drie stappen: meten, begrijpen, toepassen.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

step_1, step_2, step_3 = st.columns(3, gap="large")

with step_1:
    st.markdown(
        """
        <article class="method-step">
          <h3>1. Meten</h3>
          <p>We testen op jouw eigen fiets en setup.</p>
          <ul class="method-list">
            <li>Zone &amp; Drempel Test (Step)</li>
            <li>Max &amp; Performance Test (Ramp)</li>
          </ul>
          <p><strong>Wat meten we</strong></p>
          <ul class="method-list">
            <li>VO2peak</li>
            <li>VT1 (duurgrens)</li>
            <li>VT2 (drempelgebied)</li>
            <li>Vermogen (watt) en hartslag</li>
            <li>Ademprofiel (VE = Rf x Tv)</li>
          </ul>
        </article>
        """,
        unsafe_allow_html=True,
    )

with step_2:
    st.markdown(
        """
        <article class="method-step">
          <h3>2. Begrijpen</h3>
          <p>Je krijgt een helder PDF-rapport met:</p>
          <ul class="method-list">
            <li>Trainingszones in watt en hartslag</li>
            <li>VT1 en VT2 als concrete stuurpunten</li>
            <li>Inzicht in waar jouw trainingswinst ligt</li>
          </ul>
          <p class="method-link-note">Wil je extra uitleg over terminologie? <a href="/Energiesystemen">Bekijk Kernbegrippen</a>.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with step_3:
    st.markdown(
        """
        <article class="method-step">
          <h3>3. Toepassen</h3>
          <p>De uitkomsten gebruik je direct voor:</p>
          <ul class="method-list">
            <li>Duurtraining rond VT1</li>
            <li>Drempeltraining rond VT2</li>
            <li>VO2-ontwikkeling</li>
            <li>Pacing bij klimmen en tijdritten</li>
            <li>Na <strong>6-8 weken</strong>: hertest en zones bijstellen</li>
          </ul>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <article class="method-info">
      <strong>Ademprofiel uitgelegd</strong><br/>
      Ventilatie (VE) is de hoeveelheid lucht per minuut. VE bestaat uit ademfrequentie (Rf) en teugvolume (Tv): VE = Rf x Tv.
      Dit laat zien hoe jouw ademhaling opschaalt bij toenemende intensiteit en helpt bij interpretatie en pacing.
    </article>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="method-section">
      <h2>Voorbereiding op de test</h2>
      <p class="method-sub">Een goede voorbereiding zorgt voor betrouwbare drempels en een representatieve VO2peak.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

prep_a, prep_b, prep_c = st.columns(3, gap="large")
with prep_a:
    st.markdown(
        """
        <article class="method-mini">
          <h3>24 uur vooraf</h3>
          <ul>
            <li>Geen zware training</li>
            <li>Geen alcohol</li>
            <li>Normaal eten</li>
            <li>Goed slapen</li>
          </ul>
        </article>
        """,
        unsafe_allow_html=True,
    )
with prep_b:
    st.markdown(
        """
        <article class="method-mini">
          <h3>3-6 uur vooraf</h3>
          <ul>
            <li>Geen cafeine (of consistent houden)</li>
            <li>Grote maaltijd 2-3 uur vooraf</li>
          </ul>
        </article>
        """,
        unsafe_allow_html=True,
    )
with prep_c:
    st.markdown(
        """
        <article class="method-mini">
          <h3>Op de dag zelf</h3>
          <ul>
            <li>Drink normaal</li>
            <li>Meld medische bijzonderheden</li>
            <li>Gebruik medicatie zoals normaal</li>
          </ul>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <section class="method-section">
      <h2>Submaximale mogelijkheid</h2>
      <article class="method-compact">
        Indien nodig kan de Zone &amp; Drempel Test submaximaal worden uitgevoerd, bijvoorbeeld bij hart- of longproblematiek.
        We stemmen de opbouw veilig af op jouw situatie.
      </article>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="method-section">
      <h2>Wat je krijgt na afloop</h2>
      <ul class="method-list">
        <li>Helder PDF-rapport</li>
        <li>Persoonlijke nabespreking</li>
        <li>Advies bij het formuleren van doelen</li>
        <li>Toegang tot de inspanningsfysiologie AI-tool</li>
      </ul>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="method-section">
      <h2>Plan je meting</h2>
    </section>
    """,
    unsafe_allow_html=True,
)
bottom_pad_l, bottom_plan_col, bottom_pad_r = st.columns([0.2, 0.6, 0.2], gap="small")
with bottom_plan_col:
    plan_test_button("Plan je meting", key="method_bottom_plan", page_id="methode", use_container_width=True)

st.markdown('<p class="method-footer">We zien je snel bij SportMetrics.</p>', unsafe_allow_html=True)

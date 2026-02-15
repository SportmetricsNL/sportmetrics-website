import importlib.util
import sys
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Aanbod - SportMetrics",
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
top_nav(active="Aanbod")
render_plan_dialog_if_open()

st.markdown(
    """
    <style>
      .offer-hero {
        margin-top: 0.35rem;
        padding: clamp(2.2rem, 4vw, 3rem) clamp(1.25rem, 2.8vw, 2rem);
        border-radius: 1.1rem;
        border: 1px solid #d5e2e6;
        background: linear-gradient(140deg, #f7fbfc 0%, #ebf4f6 100%);
        box-shadow: 0 14px 30px rgba(18, 62, 74, 0.08);
      }

      .offer-hero h1 {
        margin: 0;
        font-size: clamp(2rem, 4.3vw, 3rem);
        color: #153f48;
        line-height: 1.04;
      }

      .offer-hero p {
        margin: 0.85rem 0 0;
        max-width: 48ch;
        color: #2b5d66;
        line-height: 1.6;
      }

      .offer-panel {
        margin-top: 1.45rem;
        padding: 1.25rem;
        background: rgba(255, 255, 255, 0.82);
        border: 1px solid #d7e3e6;
        border-radius: 1.08rem;
        box-shadow: 0 10px 26px rgba(19, 61, 73, 0.08);
      }

      .offer-panel h2 {
        margin: 0;
        font-size: 1.34rem;
        color: #173f49;
      }

      .offer-sub {
        margin: 0.42rem 0 0;
        color: #5a747d;
      }

      .offer-grid-2 {
        margin-top: 0.95rem;
        display: grid;
        gap: 1rem;
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }

      .offer-grid-4 {
        margin-top: 0.95rem;
        display: grid;
        gap: 0.8rem;
        grid-template-columns: repeat(4, minmax(0, 1fr));
      }

      .offer-card {
        background: #ffffff;
        border: 1px solid #d8e2e5;
        border-radius: 0.95rem;
        padding: 1rem;
        height: 100%;
      }

      .offer-card-step {
        border-color: #c9d8dc;
        background: #f9fcfd;
        box-shadow: 0 8px 18px rgba(20, 66, 78, 0.09);
      }

      .offer-tag {
        display: inline-block;
        margin-bottom: 0.4rem;
        font-size: 0.78rem;
        font-weight: 700;
        color: #48666d;
      }

      .offer-card h3 {
        margin: 0;
        color: #1f4f5a;
        font-size: 1.06rem;
      }

      .offer-card p {
        margin: 0.5rem 0 0;
        color: #355e68;
        line-height: 1.6;
      }

      .offer-card h4 {
        margin: 0.84rem 0 0.35rem;
        color: #244f59;
        font-size: 0.98rem;
      }

      .offer-card ul {
        margin: 0.38rem 0 0;
        padding-left: 1rem;
      }

      .offer-card li {
        margin: 0.24rem 0;
        color: #355e68;
      }

      .offer-divider {
        border: 0;
        border-top: 1px solid #dce7ea;
        margin: 0.9rem 0 0.72rem;
      }

      .offer-note {
        margin-top: 0.65rem;
        color: #5a747d;
        font-size: 0.9rem;
      }

      .offer-soft {
        background: #f3f9fa;
      }

      .offer-mini h3 {
        margin: 0;
        color: #1f4f5a;
        font-size: 0.98rem;
      }

      .offer-mini p {
        margin: 0.4rem 0 0;
        color: #355e68;
        line-height: 1.55;
      }

      .offer-price {
        margin: 0.55rem 0 0;
        color: #1f505a;
        font-size: clamp(1.35rem, 2.4vw, 1.8rem);
        font-weight: 800;
      }

      .offer-bundle-grid {
        margin-top: 0.95rem;
        display: grid;
        gap: 1rem;
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }

      .offer-muted {
        margin: 0.62rem 0 0;
        color: #6a838a;
      }

      @media (max-width: 900px) {
        .offer-panel {
          padding: 1rem;
        }

        .offer-grid-2,
        .offer-grid-4,
        .offer-bundle-grid {
          grid-template-columns: 1fr;
        }
      }
    </style>

    <section class="offer-hero">
      <h1>Train dit seizoen op jouw fysiologie.</h1>
      <p>Start met een basismeting op je eigen fiets. Geen schattingen, maar duidelijke zones en drempels die direct toepasbaar zijn op je training.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div style='height:0.62rem'></div>", unsafe_allow_html=True)
pad_l, plan_col, pad_r = st.columns([0.2, 0.6, 0.2], gap="small")
with plan_col:
    plan_test_button("Plan je meting", key="offer_hero_plan", use_container_width=True)

st.markdown(
    """
    <section class="offer-panel">
      <h2>Kies jouw test</h2>
      <p class="offer-sub">Twee duidelijke opties, afhankelijk van jouw doel.</p>
      <div class="offer-grid-2">
        <article class="offer-card offer-card-step">
          <span class="offer-tag">Aanbevolen voor de meeste duursporters</span>
          <h3>Zone &amp; Drempel Test (Step)</h3>
          <p>Train op jouw fysiologie: duidelijke zones en drempels voor duur, tempo en drempeltraining.</p>
          <h4>Doel</h4>
          <p>Persoonlijke trainingssturing op basis van VT1, VT2 en zones.</p>
          <h4>Wat je krijgt</h4>
          <ul>
            <li>VO2peak</li>
            <li>VT1 (duurgrens) en VT2 (drempelgebied)</li>
            <li>Zones in watt en hartslag</li>
            <li>Ademprofiel (VE = Rf x Tv)</li>
          </ul>
          <h4>Waarom dit protocol</h4>
          <p>Stabiele stappen maken VT1 en VT2 vaak duidelijker. Je rijdt door tot maximaal, dus VO2peak is volwaardig en goed vergelijkbaar over tijd.</p>
          <hr class="offer-divider" />
          <h4>Wanneer kies je deze test?</h4>
          <ul>
            <li>Je je trainingszones exact wilt bepalen</li>
            <li>Je gericht wilt verbeteren in duur of drempel</li>
            <li>Je progressie wilt meten na 6-8 weken</li>
            <li>Je wilt trainen op jouw fysiologie</li>
          </ul>
          <p><strong>Beste keuze voor de meeste sporters.</strong></p>
        </article>

        <article class="offer-card">
          <span class="offer-tag">Max &amp; performance focus</span>
          <h3>Max &amp; Performance Test (Ramp)</h3>
          <p>Continu oplopende belasting met nadruk op maximale prestatie. Geschikt wanneer maximale capaciteit centraal staat.</p>
          <h4>Doel</h4>
          <p>Inzicht in VO2peak, maximale prestatie en pacingrichting.</p>
          <h4>Wat je krijgt</h4>
          <ul>
            <li>VO2peak</li>
            <li>Maximaal vermogen en hartslagrespons</li>
            <li>VT1/VT2-indicatie en zoneadvies</li>
          </ul>
          <h4>Waarom dit protocol</h4>
          <p>Vloeiende opbouw zonder vaste blokken. Past goed bij sporters die dit prettiger rijden of in step-tests stoppen door lokale vermoeidheid.</p>
          <hr class="offer-divider" />
          <h4>Wanneer kies je deze test?</h4>
          <ul>
            <li>Je je maximale vermogen centraal wilt stellen</li>
            <li>Je focust op korte klimmen of top-end prestaties</li>
            <li>Je een continu oplopende test prettiger vindt</li>
          </ul>
          <p class="offer-note">Twijfel je welke test past bij jouw doel? Ik adviseer je vooraf persoonlijk.</p>
        </article>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="offer-panel">
      <h2>Op doel: verdieping</h2>
      <p class="offer-sub">Voor specifieke trainingsvragen.</p>
      <div class="offer-grid-2">
        <article class="offer-card">
          <h3>Duurgrens Test (VT1)</h3>
          <p>Voor langeafstand-duursporters die hun duurzone nauwkeurig willen kalibreren.</p>
          <h4>Doel</h4>
          <p>Maximale zekerheid over je duurgrens.</p>
          <h4>Wat je krijgt</h4>
          <ul>
            <li>VT1 in watt en hartslag</li>
            <li>Zone 1-2 richtlijnen</li>
            <li>Advies voor duurtraining</li>
          </ul>
        </article>
        <article class="offer-card">
          <h3>Critical Power Testpakket (3 momenten)</h3>
          <p>Voor klimmen, tijdritten en pacing.</p>
          <h4>Doel</h4>
          <p>Prestatieprofiel en pacingstrategie per inspanningsduur.</p>
          <h4>Wat je krijgt</h4>
          <ul>
            <li>Critical Power profiel (<a href="/Critical_Power">zie uitleg CP-pagina</a>)</li>
            <li>Pacingrichtlijnen</li>
            <li>Klimstrategie</li>
            <li>Metabolisch profiel en trainingsaccenten</li>
          </ul>
        </article>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="offer-panel offer-soft">
      <h2>Submaximale insteek (indien nodig)</h2>
      <p>De Zone &amp; Drempel Test kan ook submaximaal bij hart- of longproblematiek of klachten bij zware inspanning, met een veilige opbouw op maat.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="offer-panel">
      <h2>Wanneer testen?</h2>
      <p class="offer-sub">Seizoensmomenten en hertesten (6-8 weken)</p>
      <div class="offer-grid-4">
        <article class="offer-card offer-mini">
          <h3>Voorseizoen</h3>
          <p>Basismeting en plan.</p>
        </article>
        <article class="offer-card offer-mini">
          <h3>Midden seizoen</h3>
          <p>Zones bijstellen na 6-8 weken.</p>
        </article>
        <article class="offer-card offer-mini">
          <h3>Na seizoen</h3>
          <p>Evaluatie en nieuwe focus.</p>
        </article>
        <article class="offer-card offer-mini">
          <h3>MesoCycle (6-8 weken)</h3>
          <p>Startmeting, gerichte trainingsfocus en hertest op een specifiek doel.</p>
        </article>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="offer-panel">
      <h2>Seizoensstart - tijdelijke actie</h2>
      <p class="offer-price">Zone &amp; Drempel Test of Max &amp; Performance Test: 100 euro per test</p>
      <div class="offer-bundle-grid">
        <article class="offer-card">
          <h3>Bundel 1</h3>
          <p>Meting + nameting (6-8 weken): 190 euro</p>
        </article>
        <article class="offer-card">
          <h3>Bundel 2</h3>
          <p>Voorseizoen + midden seizoen + na seizoen: 270 euro</p>
        </article>
      </div>
      <h4 style="margin:0.9rem 0 0.35rem; color:#244f59;">Verdiepende testen in overleg:</h4>
      <ul style="margin:0.3rem 0 0; padding-left:1rem;">
        <li>Duurgrens Test (VT1)</li>
        <li>Critical Power (3 momenten)</li>
      </ul>
      <p class="offer-muted">Populair bij sporters die gericht willen verbeteren.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="offer-panel">
      <h2>Wat je altijd krijgt</h2>
      <ul style="margin:0.5rem 0 0; padding-left:1rem;">
        <li>De test in een helder PDF-rapport</li>
        <li>Heldere nabespreking van je rapport</li>
        <li>Advies en hulp bij het formuleren van doelen</li>
        <li>Toegang tot de inspanningsfysiologie AI-tool (upload je rapport en neem zones en periodisering stap voor stap door, ook getraind voor hardlopen en krachttraining)</li>
      </ul>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div style='height:0.72rem'></div>", unsafe_allow_html=True)
with st.container(border=True):
    st.markdown("<h2 class='offer-section-title'>Plan je meting</h2>", unsafe_allow_html=True)
pad_l2, plan_bottom_col, pad_r2 = st.columns([0.2, 0.6, 0.2], gap="small")
with plan_bottom_col:
    plan_test_button("Plan je meting", key="offer_bottom_plan", use_container_width=True)

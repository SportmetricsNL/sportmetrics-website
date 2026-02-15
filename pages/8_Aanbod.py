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

from site.ui import inject_global_css, top_nav

inject_global_css()
top_nav(active="Aanbod")

CTA_URL = "mailto:folkertvinke@gmail.com"

st.markdown(
    """
    <style>
      .offer-hero {
        margin-top: 0.35rem;
        padding: clamp(2.2rem, 4.2vw, 3.3rem) clamp(1.25rem, 2.8vw, 2.1rem);
        border-radius: 1.12rem;
        border: 1px solid #d5e2e6;
        background: linear-gradient(140deg, #f7fbfc 0%, #ebf4f6 100%);
        box-shadow: 0 14px 30px rgba(18, 62, 74, 0.08);
      }

      .offer-hero h1 {
        margin: 0;
        color: #153f48;
        font-size: clamp(2rem, 4.4vw, 3rem);
        line-height: 1.04;
      }

      .offer-hero p {
        margin: 0.9rem 0 0;
        max-width: 48ch;
        color: #2b5d66;
        line-height: 1.6;
      }

      .offer-hero-actions {
        margin-top: 1.25rem;
        display: flex;
        flex-wrap: wrap;
        gap: 0.7rem;
      }

      .offer-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.72rem 1.2rem;
        border-radius: 999px;
        border: 1px solid #c9d9dd;
        text-decoration: none !important;
        font-weight: 700;
        letter-spacing: 0.01em;
      }

      .offer-btn-primary {
        background: linear-gradient(140deg, #2d7c85 0%, #3d9199 100%);
        border-color: #2d7c85;
        color: #ffffff !important;
        box-shadow: 0 10px 22px rgba(22, 74, 87, 0.22);
      }

      .offer-btn-secondary {
        background: #ffffff;
        color: #245e67 !important;
      }

      .offer-section {
        margin-top: 1.52rem;
        padding: 1.2rem;
        border-radius: 1rem;
        border: 1px solid #d5e2e6;
        background: rgba(255, 255, 255, 0.92);
        box-shadow: 0 10px 22px rgba(21, 65, 77, 0.07);
      }

      .offer-section h2 {
        margin: 0;
        color: #1f505a;
        font-size: 1.26rem;
      }

      .offer-subtitle {
        margin: 0.45rem 0 0;
        color: #5a747d;
      }

      .offer-grid-2 {
        display: grid;
        gap: 1rem;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        margin-top: 0.95rem;
      }

      .offer-card {
        height: 100%;
        padding: 1rem;
        border-radius: 0.92rem;
        border: 1px solid #d8e4e8;
        background: #ffffff;
      }

      .offer-card-compact {
        padding: 0.86rem;
      }

      .offer-card-compact p {
        font-size: 0.94rem;
      }

      .offer-card-step {
        border: 1px solid #c9d8dc;
        background: #f9fcfd;
        box-shadow: 0 8px 18px rgba(20, 66, 78, 0.09);
      }

      .offer-label {
        display: inline-block;
        font-size: 0.76rem;
        font-weight: 700;
        color: #48666d;
        letter-spacing: 0.02em;
        margin-bottom: 0.45rem;
      }

      .offer-card h3 {
        margin: 0;
        color: #205561;
        font-size: 1.06rem;
      }

      .offer-card h4 {
        margin: 0.88rem 0 0.3rem;
        color: #275965;
        font-size: 0.95rem;
        font-weight: 700;
      }

      .offer-card p {
        margin: 0.5rem 0 0;
        color: #315a65;
        line-height: 1.58;
      }

      .offer-list {
        margin: 0.5rem 0 0;
        padding-left: 1rem;
      }

      .offer-list li {
        margin: 0.28rem 0;
        color: #315a65;
      }

      .offer-divider {
        margin: 0.86rem 0 0.24rem;
        border: 0;
        border-top: 1px solid #dce7ea;
      }

      .offer-small-note {
        margin-top: 0.72rem;
        color: #5a747d;
        font-size: 0.86rem;
      }

      .offer-soft {
        background: #f3f9fa;
      }

      .offer-grid-4 {
        display: grid;
        gap: 0.8rem;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        margin-top: 0.95rem;
      }

      .offer-mini {
        border: 1px solid #d8e4e8;
        border-radius: 0.9rem;
        background: #ffffff;
        padding: 0.9rem;
      }

      .offer-mini h3 {
        margin: 0;
        font-size: 0.95rem;
        color: #1f505a;
      }

      .offer-mini p {
        margin: 0.38rem 0 0;
        color: #5a747d;
        font-size: 0.9rem;
      }

      .offer-price-main {
        margin-top: 0.55rem;
        color: #1f505a;
        font-size: clamp(1.35rem, 2.4vw, 1.8rem);
        font-weight: 800;
      }

      .offer-price-bundles {
        display: grid;
        gap: 0.8rem;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        margin-top: 0.95rem;
      }

      .offer-muted {
        margin-top: 0.72rem;
        color: #6a838a;
      }

      .offer-plan {
        margin-top: 1.62rem;
        padding: 1.15rem;
        border-radius: 1rem;
        border: 1px solid #d5e2e6;
        background: #ffffff;
      }

      .offer-plan h2 {
        margin: 0;
        color: #1f505a;
        font-size: 1.26rem;
      }

      .offer-plan .offer-btn-primary {
        width: fit-content;
        margin-top: 0.85rem;
      }

      @media (max-width: 900px) {
        .offer-section {
          padding: 0.95rem;
        }

        .offer-grid-2,
        .offer-price-bundles,
        .offer-grid-4 {
          grid-template-columns: 1fr;
        }

        .offer-hero-actions .offer-btn,
        .offer-plan .offer-btn-primary {
          width: 100%;
        }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <section class="offer-hero">
      <h1>Train dit seizoen op jouw fysiologie.</h1>
      <p>Start met een basismeting op je eigen fiets. Geen schattingen, maar duidelijke zones en drempels die direct toepasbaar zijn op je training.</p>
      <div class="offer-hero-actions">
        <a class="offer-btn offer-btn-primary" href="{CTA_URL}">Plan je meting</a>
        <a class="offer-btn offer-btn-secondary" href="/Methode">Bekijk Kernbegrippen</a>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="offer-section">
      <h2>Kies jouw test</h2>
      <p class="offer-subtitle">Twee duidelijke opties, afhankelijk van jouw doel.</p>

      <div class="offer-grid-2">
        <article class="offer-card offer-card-step">
          <span class="offer-label">Aanbevolen voor de meeste duursporters</span>
          <h3>Zone &amp; Drempel Test (Step)</h3>
          <p>Train op jouw fysiologie: duidelijke zones en drempels voor duur, tempo en drempeltraining.</p>

          <p><strong>Doel</strong><br/>Persoonlijke trainingssturing op basis van VT1, VT2 en zones.</p>
          <h4>Wat je krijgt</h4>
          <ul class="offer-list">
            <li>VO2peak</li>
            <li>VT1 (duurgrens) en VT2 (drempelgebied)</li>
            <li>Zones in watt en hartslag</li>
            <li>Ademprofiel (VE = Rf x Tv)</li>
          </ul>

          <h4>Waarom dit protocol</h4>
          <p>Stabiele stappen maken VT1 en VT2 vaak duidelijker. Je rijdt door tot maximaal, dus VO2peak is volwaardig en goed vergelijkbaar over tijd.</p>

          <hr class="offer-divider" />
          <h4>Wanneer kies je deze test?</h4>
          <p>Bijvoorbeeld als:</p>
          <ul class="offer-list">
            <li>Je je trainingszones exact wilt bepalen</li>
            <li>Je gericht wilt verbeteren in duur of drempel</li>
            <li>Je progressie wilt meten na 6-8 weken</li>
            <li>Je wilt trainen op jouw fysiologie</li>
          </ul>
          <p><strong>Beste keuze voor de meeste sporters.</strong></p>
        </article>

        <article class="offer-card">
          <span class="offer-label">Max &amp; performance focus</span>
          <h3>Max &amp; Performance Test (Ramp)</h3>
          <p>Continu oplopende belasting met nadruk op maximale prestatie. Geschikt wanneer maximale capaciteit centraal staat.</p>

          <p><strong>Doel</strong><br/>Inzicht in VO2peak, maximale prestatie en pacingrichting.</p>
          <h4>Wat je krijgt</h4>
          <ul class="offer-list">
            <li>VO2peak</li>
            <li>Maximaal vermogen en hartslagrespons</li>
            <li>VT1/VT2-indicatie en zoneadvies</li>
          </ul>

          <h4>Waarom dit protocol</h4>
          <p>Vloeiende opbouw zonder vaste blokken. Past goed bij sporters die dit prettiger rijden of in step-tests stoppen door lokale vermoeidheid.</p>

          <hr class="offer-divider" />
          <h4>Wanneer kies je deze test?</h4>
          <p>Bijvoorbeeld als:</p>
          <ul class="offer-list">
            <li>Je je maximale vermogen centraal wilt stellen</li>
            <li>Je focust op korte klimmen of top-end prestaties</li>
            <li>Je een continu oplopende test prettiger vindt</li>
          </ul>
          <p class="offer-small-note">Twijfel je welke test past bij jouw doel? Ik adviseer je vooraf persoonlijk.</p>
        </article>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="offer-section">
      <h2>Op doel: verdieping</h2>
      <p class="offer-subtitle">Voor specifieke trainingsvragen.</p>

      <div class="offer-grid-2">
        <article class="offer-card offer-card-compact">
          <h3>Duurgrens Test (VT1)</h3>
          <p>Voor langeafstand-duursporters die hun duurzone nauwkeurig willen kalibreren.</p>
          <p><strong>Doel</strong><br/>Maximale zekerheid over je duurgrens.</p>
          <h4>Wat je krijgt</h4>
          <ul class="offer-list">
            <li>VT1 in watt en hartslag</li>
            <li>Zone 1-2 richtlijnen</li>
            <li>Advies voor duurtraining</li>
          </ul>
        </article>

        <article class="offer-card offer-card-compact">
          <h3>Critical Power Testpakket (3 momenten)</h3>
          <p>Voor klimmen, tijdritten en pacing.</p>
          <p><strong>Doel</strong><br/>Prestatieprofiel en pacingstrategie per inspanningsduur.</p>
          <h4>Wat je krijgt</h4>
          <ul class="offer-list">
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
    <section class="offer-section">
      <h2>Submaximale insteek (indien nodig)</h2>
      <article class="offer-card offer-soft">
        <p>De Zone &amp; Drempel Test kan ook submaximaal bij hart- of longproblematiek of klachten bij zware inspanning, met een veilige opbouw op maat.</p>
      </article>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="offer-section">
      <h2>Wanneer testen?</h2>
      <p class="offer-subtitle">Seizoensmomenten en hertesten (6-8 weken)</p>

      <div class="offer-grid-4">
        <article class="offer-mini">
          <h3>Voorseizoen</h3>
          <p>Basismeting en plan.</p>
        </article>
        <article class="offer-mini">
          <h3>Midden seizoen</h3>
          <p>Zones bijstellen na 6-8 weken.</p>
        </article>
        <article class="offer-mini">
          <h3>Na seizoen</h3>
          <p>Evaluatie en nieuwe focus.</p>
        </article>
        <article class="offer-mini">
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
    <section class="offer-section">
      <h2>Seizoensstart - tijdelijke actie</h2>
      <p class="offer-price-main">Zone &amp; Drempel Test of Max &amp; Performance Test: 100 euro per test</p>

      <div class="offer-price-bundles">
        <article class="offer-card">
          <h3>Bundel</h3>
          <p>Meting + nameting (6-8 weken): 190 euro</p>
        </article>
        <article class="offer-card">
          <h3>Bundel</h3>
          <p>Voorseizoen + midden seizoen + na seizoen: 270 euro</p>
        </article>
      </div>

      <p><strong>Verdiepende testen in overleg:</strong></p>
      <ul class="offer-list">
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
    <section class="offer-section">
      <h2>Wat je altijd krijgt</h2>
      <article class="offer-card">
        <ul class="offer-list">
          <li>De test in een helder PDF-rapport</li>
          <li>Heldere nabespreking van je rapport</li>
          <li>Advies en hulp bij het formuleren van doelen</li>
          <li>Toegang tot de inspanningsfysiologie AI-tool (upload je rapport en neem zones en periodisering stap voor stap door, ook getraind voor hardlopen en krachttraining)</li>
        </ul>
      </article>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <section class="offer-plan">
      <h2>Plan je meting</h2>
      <a class="offer-btn offer-btn-primary" href="{CTA_URL}">Plan je meting</a>
    </section>
    """,
    unsafe_allow_html=True,
)

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
render_plan_dialog_if_open(page_id="aanbod")

st.markdown(
    """
    <style>
      .offer-title { margin: 0; color: #173f49; font-size: clamp(2rem, 4.2vw, 3rem); line-height: 1.05; }
      .offer-sub { margin: 0.82rem 0 0; color: #355e68; max-width: 50ch; line-height: 1.6; }
      .offer-section-title { margin: 0; color: #173f49; font-size: 1.34rem; }
      .offer-section-sub { margin: 0.38rem 0 0; color: #5a747d; }
      .offer-note { margin: 0.6rem 0 0; color: #6a838a; font-size: 0.9rem; }
      .offer-price-big { margin: 0.2rem 0 0; color: #1f505a; font-size: clamp(1.35rem, 2.4vw, 1.9rem); font-weight: 800; }
      .offer-card-title { margin: 0; color: #1f4f5a; font-size: 1.06rem; }

      .offer-card {
        height: 100%;
        border: 1px solid #d8e2e5;
        border-radius: 0.95rem;
        background: #ffffff;
        padding: 1rem 1.1rem;
      }

      .offer-card-gold {
        border: 1px solid #d7b45e;
      }

      .offer-pill {
        margin: 0;
        color: #2f6b75;
        font-size: 0.8rem;
        font-weight: 800;
        letter-spacing: 0.05em;
        text-transform: uppercase;
      }

      .offer-card h3 {
        margin: 0.35rem 0 0.65rem;
        color: #1f4f5a;
        font-size: 2rem;
      }

      .offer-card p {
        margin: 0.5rem 0;
        color: #315a65;
        line-height: 1.6;
      }

      .offer-card ul {
        margin: 0.35rem 0 0.35rem 1.05rem;
      }

      .offer-card li {
        margin: 0.18rem 0;
        color: #315a65;
      }

      .offer-divider {
        height: 1px;
        margin: 0.85rem 0 0.75rem;
        background: #dfe7ea;
      }

      .offer-price-card {
        height: 100%;
        border: 1px solid #d8e2e5;
        border-radius: 0.95rem;
        background: #ffffff;
        padding: 1rem 1.1rem;
      }

      .offer-price-card h3 {
        margin: 0;
        color: #1f4f5a;
        font-size: 1.35rem;
      }

      .offer-price-card p {
        margin: 0.48rem 0 0;
        color: #315a65;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.markdown('<h1 class="offer-title">Train dit seizoen op jouw fysiologie.</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="offer-sub">Start met een basismeting op je eigen fiets. Geen schattingen, maar duidelijke zones en drempels die direct toepasbaar zijn op je training.</p>',
        unsafe_allow_html=True,
    )

st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
pad_l, plan_top_col, pad_r = st.columns([0.2, 0.6, 0.2], gap="small")
with plan_top_col:
    plan_test_button("Plan je meting", key="offer_hero_plan", page_id="aanbod", use_container_width=True)

with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Kies jouw test</h2>', unsafe_allow_html=True)
    st.markdown('<p class="offer-section-sub">Twee duidelijke opties, afhankelijk van jouw doel.</p>', unsafe_allow_html=True)
    left, right = st.columns(2, gap="large")
    with left:
        st.markdown(
            """
            <article class="offer-card offer-card-gold">
              <p class="offer-pill">aanbevolen voor de meeste fietsers</p>
              <h3>Zone &amp; Drempel Test (Step)</h3>
              <p>Train op jouw fysiologie: duidelijke zones en drempels voor duur, tempo en drempeltraining.</p>
              <p><strong>Doel</strong></p>
              <p>Persoonlijke trainingssturing op basis van VT1, VT2 en zones.</p>
              <p><strong>Wat je krijgt</strong></p>
              <ul>
                <li>VO2peak</li>
                <li>VT1 (duurgrens) en VT2 (drempelgebied)</li>
                <li>Zones in watt en hartslag</li>
                <li>Ademprofiel (VE = Rf x Tv)</li>
              </ul>
              <p><strong>Waarom dit protocol</strong></p>
              <p>Stabiele stappen maken VT1 en VT2 vaak duidelijker. Je rijdt door tot maximaal, dus VO2peak is volwaardig en goed vergelijkbaar over tijd.</p>
              <div class="offer-divider"></div>
              <p><strong>Wanneer kies je deze test?</strong></p>
              <ul>
                <li>Je je trainingszones exact wilt bepalen</li>
                <li>Je gericht wilt verbeteren in duur of drempel</li>
                <li>Je progressie wilt meten na 6-8 weken</li>
                <li>Je wilt trainen op jouw fysiologie</li>
              </ul>
              <p><strong>Beste keuze voor de meeste sporters.</strong></p>
            </article>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(
            """
            <article class="offer-card">
              <p class="offer-pill">Max &amp; performance focus</p>
              <h3>Max &amp; Performance Test (Ramp)</h3>
              <p>Continu oplopende belasting met nadruk op maximale prestatie. Geschikt wanneer maximale capaciteit centraal staat.</p>
              <p><strong>Doel</strong></p>
              <p>Inzicht in VO2peak, maximale prestatie en pacingrichting.</p>
              <p><strong>Wat je krijgt</strong></p>
              <ul>
                <li>VO2peak</li>
                <li>Maximaal vermogen en hartslagrespons</li>
                <li>VT1/VT2-indicatie en zoneadvies</li>
              </ul>
              <p><strong>Waarom dit protocol</strong></p>
              <p>Vloeiende opbouw zonder vaste blokken. Past goed bij sporters die dit prettiger rijden of in step-tests stoppen door lokale vermoeidheid.</p>
              <div class="offer-divider"></div>
              <p><strong>Wanneer kies je deze test?</strong></p>
              <ul>
                <li>Je je maximale vermogen centraal wilt stellen</li>
                <li>Je focust op korte klimmen of top-end prestaties</li>
                <li>Je een continu oplopende test prettiger vindt</li>
              </ul>
              <p class="offer-note">Twijfel je welke test past bij jouw doel? Ik adviseer je vooraf persoonlijk.</p>
            </article>
            """,
            unsafe_allow_html=True,
        )

with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Overige testing</h2>', unsafe_allow_html=True)
    st.markdown('<p class="offer-section-sub">Voor specifieke trainingsvragen.</p>', unsafe_allow_html=True)
    left, right = st.columns(2, gap="large")
    with left:
        st.markdown(
            """
            <article class="offer-card">
              <h3>Duurgrens Test (VT1)</h3>
              <p>Voor langeafstand-duursporters die hun duurzone nauwkeurig willen kalibreren.</p>
              <p><strong>Doel</strong></p>
              <p>Maximale zekerheid over je duurgrens.</p>
              <p><strong>Wat je krijgt</strong></p>
              <ul>
                <li>VT1 in watt en hartslag</li>
                <li>Zone 1-2 richtlijnen</li>
                <li>Advies voor duurtraining</li>
              </ul>
            </article>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(
            """
            <article class="offer-card">
              <h3>Critical Power Testpakket (3 momenten)</h3>
              <p>Voor klimmen, tijdritten en pacing.</p>
              <p><strong>Doel</strong></p>
              <p>Prestatieprofiel en pacingstrategie per inspanningsduur.</p>
              <p><strong>Wat je krijgt</strong></p>
              <ul>
                <li>Critical Power profiel (<a href="/Critical_Power">zie uitleg CP-pagina</a>)</li>
                <li>Pacingrichtlijnen</li>
                <li>Klimstrategie</li>
                <li>Metabolisch profiel en trainingsaccenten</li>
              </ul>
            </article>
            """,
            unsafe_allow_html=True,
        )

with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Submaximale insteek (indien nodig)</h2>', unsafe_allow_html=True)
    with st.container(border=True):
        st.write("De Zone & Drempel Test kan ook submaximaal bij hart- of longproblematiek of klachten bij zware inspanning, met een veilige opbouw op maat.")

with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Wanneer testen?</h2>', unsafe_allow_html=True)
    st.markdown('<p class="offer-section-sub">Seizoensmomenten en hertesten (6-8 weken)</p>', unsafe_allow_html=True)
    cols = st.columns(4, gap="small")
    moments = [
        ("Voorseizoen", "Basismeting en plan."),
        ("Midden seizoen", "Zones bijstellen na 6-8 weken."),
        ("Na seizoen", "Evaluatie en nieuwe focus."),
        ("MesoCycle (6-8 weken)", "Startmeting, gerichte trainingsfocus en hertest op een specifiek doel."),
    ]
    for col, (title, text) in zip(cols, moments):
        with col:
            with st.container(border=True):
                st.markdown(f"<h3 class='offer-card-title'>{title}</h3>", unsafe_allow_html=True)
                st.write(text)

with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Seizoensstart - tijdelijke actie</h2>', unsafe_allow_html=True)
    price_text_col, bundle_1_col, bundle_2_col = st.columns(3, gap="large")
    with price_text_col:
        st.markdown(
            """
            <article class="offer-price-card">
              <h3>Enkele test</h3>
              <p class="offer-price-big">100 euro</p>
              <p><strong>Seizoensstartkorting</strong> (normaal 150 euro)</p>
            </article>
            """,
            unsafe_allow_html=True,
        )
    with bundle_1_col:
        st.markdown(
            """
            <article class="offer-price-card">
              <h3>Bundel 1</h3>
              <p>Meting + nameting (6-8 weken): 190 euro</p>
            </article>
            """,
            unsafe_allow_html=True,
        )
    with bundle_2_col:
        st.markdown(
            """
            <article class="offer-price-card">
              <h3>Bundel 2</h3>
              <p>Voorseizoen + midden seizoen + na seizoen: 270 euro</p>
            </article>
            """,
            unsafe_allow_html=True,
        )
    st.write("**Verdiepende testen in overleg:**")
    st.markdown("- Duurgrens Test (VT1)\n- Critical Power (3 momenten)")
    st.markdown('<p class="offer-note">Populair bij sporters die gericht willen verbeteren.</p>', unsafe_allow_html=True)

with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Wat je altijd krijgt</h2>', unsafe_allow_html=True)
    st.markdown(
        "- De test in een helder PDF-rapport\n- Heldere nabespreking van je rapport\n- Advies en hulp bij het formuleren van doelen\n- Toegang tot de inspanningsfysiologie AI-tool (upload je rapport en neem zones en periodisering stap voor stap door, ook getraind voor hardlopen en krachttraining)"
    )

st.markdown("<div style='height:0.55rem'></div>", unsafe_allow_html=True)
pad_l2, plan_bottom_col, pad_r2 = st.columns([0.2, 0.6, 0.2], gap="small")
with plan_bottom_col:
    plan_test_button("Plan je meting", key="offer_bottom_plan", page_id="aanbod", use_container_width=True)

st.markdown('<p class="offer-note" style="text-align:center; margin-top:1.2rem;">We zien je snel bij SportMetrics.</p>', unsafe_allow_html=True)

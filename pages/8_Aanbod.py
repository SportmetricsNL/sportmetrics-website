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
      .st-key-offer_hero {
        margin-top: 0.35rem;
      }

      .st-key-offer_hero > div {
        padding: clamp(2.15rem, 4vw, 3rem);
        border-radius: 1.1rem;
        border: 1px solid #d5e2e6;
        background: linear-gradient(140deg, #f7fbfc 0%, #ebf4f6 100%);
        box-shadow: 0 14px 30px rgba(18, 62, 74, 0.08);
      }

      .offer-title {
        margin: 0;
        font-size: clamp(2rem, 4.3vw, 3rem);
        color: #153f48;
        line-height: 1.04;
      }

      .offer-subcopy {
        margin: 0.85rem 0 0;
        max-width: 48ch;
        color: #2b5d66;
        line-height: 1.6;
      }

      .offer-section-title {
        margin: 0;
        color: #1f505a;
        font-size: 1.3rem;
      }

      .offer-section-sub {
        margin: 0.38rem 0 0;
        color: #5a747d;
      }

      .offer-card-title {
        margin: 0;
        color: #205561;
        font-size: 1.08rem;
      }

      .offer-label {
        display: inline-block;
        font-size: 0.78rem;
        font-weight: 700;
        color: #48666d;
        margin-bottom: 0.35rem;
      }

      .offer-divider {
        border: 0;
        border-top: 1px solid #dce7ea;
        margin: 0.9rem 0 0.7rem;
      }

      .offer-note {
        margin-top: 0.65rem;
        color: #5a747d;
        font-size: 0.9rem;
      }

      .offer-mini-title {
        margin: 0;
        color: #1f505a;
        font-size: 0.98rem;
      }

      .offer-price-main {
        margin: 0.55rem 0 0;
        color: #1f505a;
        font-size: clamp(1.35rem, 2.4vw, 1.8rem);
        font-weight: 800;
      }

      .offer-muted {
        margin: 0.6rem 0 0;
        color: #6a838a;
      }

      .st-key-offer_step_card > div {
        border: 1px solid #c9d8dc !important;
        background: #f9fcfd !important;
        box-shadow: 0 8px 18px rgba(20, 66, 78, 0.09);
      }

      .st-key-offer_soft > div {
        background: #f3f9fa !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container(key="offer_hero"):
    st.markdown('<h1 class="offer-title">Train dit seizoen op jouw fysiologie.</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="offer-subcopy">Start met een basismeting op je eigen fiets. Geen schattingen, maar duidelijke zones en drempels die direct toepasbaar zijn op je training.</p>',
        unsafe_allow_html=True,
    )

st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
pad_l, plan_col, pad_r = st.columns([0.2, 0.6, 0.2], gap="small")
with plan_col:
    plan_test_button("Plan je meting", key="offer_hero_plan", use_container_width=True)

with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Kies jouw test</h2>', unsafe_allow_html=True)
    st.markdown('<p class="offer-section-sub">Twee duidelijke opties, afhankelijk van jouw doel.</p>', unsafe_allow_html=True)
    step_col, ramp_col = st.columns(2, gap="large")

    with step_col:
        with st.container(border=True, key="offer_step_card"):
            st.markdown('<span class="offer-label">Aanbevolen voor de meeste duursporters</span>', unsafe_allow_html=True)
            st.markdown('<h3 class="offer-card-title">Zone & Drempel Test (Step)</h3>', unsafe_allow_html=True)
            st.write("Train op jouw fysiologie: duidelijke zones en drempels voor duur, tempo en drempeltraining.")
            st.write("**Doel**  \nPersoonlijke trainingssturing op basis van VT1, VT2 en zones.")
            st.write("**Wat je krijgt**")
            st.markdown(
                "- VO2peak\n- VT1 (duurgrens) en VT2 (drempelgebied)\n- Zones in watt en hartslag\n- Ademprofiel (VE = Rf x Tv)"
            )
            st.write("**Waarom dit protocol**")
            st.write(
                "Stabiele stappen maken VT1 en VT2 vaak duidelijker. Je rijdt door tot maximaal, dus VO2peak is volwaardig en goed vergelijkbaar over tijd."
            )
            st.markdown('<hr class="offer-divider" />', unsafe_allow_html=True)
            st.write("**Wanneer kies je deze test?**")
            st.markdown(
                "- Je je trainingszones exact wilt bepalen\n- Je gericht wilt verbeteren in duur of drempel\n- Je progressie wilt meten na 6-8 weken\n- Je wilt trainen op jouw fysiologie"
            )
            st.write("**Beste keuze voor de meeste sporters.**")

    with ramp_col:
        with st.container(border=True):
            st.markdown('<span class="offer-label">Max & performance focus</span>', unsafe_allow_html=True)
            st.markdown('<h3 class="offer-card-title">Max & Performance Test (Ramp)</h3>', unsafe_allow_html=True)
            st.write(
                "Continu oplopende belasting met nadruk op maximale prestatie. Geschikt wanneer maximale capaciteit centraal staat."
            )
            st.write("**Doel**  \nInzicht in VO2peak, maximale prestatie en pacingrichting.")
            st.write("**Wat je krijgt**")
            st.markdown("- VO2peak\n- Maximaal vermogen en hartslagrespons\n- VT1/VT2-indicatie en zoneadvies")
            st.write("**Waarom dit protocol**")
            st.write(
                "Vloeiende opbouw zonder vaste blokken. Past goed bij sporters die dit prettiger rijden of in step-tests stoppen door lokale vermoeidheid."
            )
            st.markdown('<hr class="offer-divider" />', unsafe_allow_html=True)
            st.write("**Wanneer kies je deze test?**")
            st.markdown(
                "- Je je maximale vermogen centraal wilt stellen\n- Je focust op korte klimmen of top-end prestaties\n- Je een continu oplopende test prettiger vindt"
            )
            st.markdown(
                '<p class="offer-note">Twijfel je welke test past bij jouw doel? Ik adviseer je vooraf persoonlijk.</p>',
                unsafe_allow_html=True,
            )

st.markdown("<div style='height:0.55rem'></div>", unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Op doel: verdieping</h2>', unsafe_allow_html=True)
    st.markdown('<p class="offer-section-sub">Voor specifieke trainingsvragen.</p>', unsafe_allow_html=True)
    deep_left, deep_right = st.columns(2, gap="large")

    with deep_left:
        with st.container(border=True):
            st.markdown('<h3 class="offer-card-title">Duurgrens Test (VT1)</h3>', unsafe_allow_html=True)
            st.write("Voor langeafstand-duursporters die hun duurzone nauwkeurig willen kalibreren.")
            st.write("**Doel**  \nMaximale zekerheid over je duurgrens.")
            st.write("**Wat je krijgt**")
            st.markdown("- VT1 in watt en hartslag\n- Zone 1-2 richtlijnen\n- Advies voor duurtraining")

    with deep_right:
        with st.container(border=True):
            st.markdown('<h3 class="offer-card-title">Critical Power Testpakket (3 momenten)</h3>', unsafe_allow_html=True)
            st.write("Voor klimmen, tijdritten en pacing.")
            st.write("**Doel**  \nPrestatieprofiel en pacingstrategie per inspanningsduur.")
            st.write("**Wat je krijgt**")
            st.markdown(
                "- Critical Power profiel ([zie uitleg CP-pagina](/Critical_Power))\n- Pacingrichtlijnen\n- Klimstrategie\n- Metabolisch profiel en trainingsaccenten"
            )

st.markdown("<div style='height:0.55rem'></div>", unsafe_allow_html=True)
with st.container(border=True, key="offer_soft"):
    st.markdown('<h2 class="offer-section-title">Submaximale insteek (indien nodig)</h2>', unsafe_allow_html=True)
    st.write(
        "De Zone & Drempel Test kan ook submaximaal bij hart- of longproblematiek of klachten bij zware inspanning, met een veilige opbouw op maat."
    )

st.markdown("<div style='height:0.55rem'></div>", unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Wanneer testen?</h2>', unsafe_allow_html=True)
    st.markdown('<p class="offer-section-sub">Seizoensmomenten en hertesten (6-8 weken)</p>', unsafe_allow_html=True)
    moment_cols = st.columns(4, gap="small")
    labels = [
        ("Voorseizoen", "Basismeting en plan."),
        ("Midden seizoen", "Zones bijstellen na 6-8 weken."),
        ("Na seizoen", "Evaluatie en nieuwe focus."),
        ("MesoCycle (6-8 weken)", "Startmeting, gerichte trainingsfocus en hertest op een specifiek doel."),
    ]
    for col, (title, text) in zip(moment_cols, labels):
        with col:
            with st.container(border=True):
                st.markdown(f'<h3 class="offer-mini-title">{title}</h3>', unsafe_allow_html=True)
                st.write(text)

st.markdown("<div style='height:0.55rem'></div>", unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Seizoensstart - tijdelijke actie</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="offer-price-main">Zone & Drempel Test of Max & Performance Test: 100 euro per test</p>',
        unsafe_allow_html=True,
    )
    bundle_left, bundle_right = st.columns(2, gap="large")
    with bundle_left:
        with st.container(border=True):
            st.markdown('<h3 class="offer-mini-title">Bundel</h3>', unsafe_allow_html=True)
            st.write("Meting + nameting (6-8 weken): 190 euro")
    with bundle_right:
        with st.container(border=True):
            st.markdown('<h3 class="offer-mini-title">Bundel</h3>', unsafe_allow_html=True)
            st.write("Voorseizoen + midden seizoen + na seizoen: 270 euro")

    st.write("**Verdiepende testen in overleg:**")
    st.markdown("- Duurgrens Test (VT1)\n- Critical Power (3 momenten)")
    st.markdown('<p class="offer-muted">Populair bij sporters die gericht willen verbeteren.</p>', unsafe_allow_html=True)

st.markdown("<div style='height:0.55rem'></div>", unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Wat je altijd krijgt</h2>', unsafe_allow_html=True)
    st.markdown(
        "- De test in een helder PDF-rapport\n- Heldere nabespreking van je rapport\n- Advies en hulp bij het formuleren van doelen\n- Toegang tot de inspanningsfysiologie AI-tool (upload je rapport en neem zones en periodisering stap voor stap door, ook getraind voor hardlopen en krachttraining)"
    )

st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Plan je meting</h2>', unsafe_allow_html=True)
pad_l2, plan_bottom_col, pad_r2 = st.columns([0.2, 0.6, 0.2], gap="small")
with plan_bottom_col:
    plan_test_button("Plan je meting", key="offer_bottom_plan", use_container_width=True)

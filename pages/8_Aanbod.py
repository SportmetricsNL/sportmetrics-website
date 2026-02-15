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
      .offer-title {
        margin: 0;
        color: #173f49;
        font-size: clamp(2rem, 4.2vw, 3rem);
        line-height: 1.05;
      }

      .offer-sub {
        margin: 0.82rem 0 0;
        color: #355e68;
        max-width: 50ch;
        line-height: 1.6;
      }

      .offer-label {
        margin: 0;
        color: #2f6b75;
        font-size: 0.82rem;
        font-weight: 800;
        letter-spacing: 0.06em;
        text-transform: uppercase;
      }

      .offer-section-title {
        margin: 0;
        color: #173f49;
        font-size: 1.34rem;
      }

      .offer-section-sub {
        margin: 0.38rem 0 0;
        color: #5a747d;
      }

      .offer-card-title {
        margin: 0;
        color: #1f4f5a;
        font-size: 1.08rem;
      }

      .offer-note {
        margin: 0.6rem 0 0;
        color: #6a838a;
        font-size: 0.9rem;
      }

      .offer-price-big {
        margin: 0.2rem 0 0;
        color: #1f505a;
        font-size: clamp(1.35rem, 2.4vw, 1.9rem);
        font-weight: 800;
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
        with st.container(border=True):
            st.markdown('<p class="offer-label">Aanbevolen voor de meeste duursporters</p>', unsafe_allow_html=True)
            st.markdown('<h3 class="offer-card-title">Zone & Drempel Test (Step)</h3>', unsafe_allow_html=True)
            st.write("Train op jouw fysiologie: duidelijke zones en drempels voor duur, tempo en drempeltraining.")
            st.write("**Doel**")
            st.write("Persoonlijke trainingssturing op basis van VT1, VT2 en zones.")
            st.write("**Wat je krijgt**")
            st.markdown("- VO2peak\n- VT1 (duurgrens) en VT2 (drempelgebied)\n- Zones in watt en hartslag\n- Ademprofiel (VE = Rf x Tv)")
            st.write("**Waarom dit protocol**")
            st.write("Stabiele stappen maken VT1 en VT2 vaak duidelijker. Je rijdt door tot maximaal, dus VO2peak is volwaardig en goed vergelijkbaar over tijd.")
            st.divider()
            st.write("**Wanneer kies je deze test?**")
            st.markdown(
                "- Je je trainingszones exact wilt bepalen\n- Je gericht wilt verbeteren in duur of drempel\n- Je progressie wilt meten na 6-8 weken\n- Je wilt trainen op jouw fysiologie"
            )
            st.write("**Beste keuze voor de meeste sporters.**")
    with right:
        with st.container(border=True):
            st.markdown('<p class="offer-label">Max & performance focus</p>', unsafe_allow_html=True)
            st.markdown('<h3 class="offer-card-title">Max & Performance Test (Ramp)</h3>', unsafe_allow_html=True)
            st.write("Continu oplopende belasting met nadruk op maximale prestatie. Geschikt wanneer maximale capaciteit centraal staat.")
            st.write("**Doel**")
            st.write("Inzicht in VO2peak, maximale prestatie en pacingrichting.")
            st.write("**Wat je krijgt**")
            st.markdown("- VO2peak\n- Maximaal vermogen en hartslagrespons\n- VT1/VT2-indicatie en zoneadvies")
            st.write("**Waarom dit protocol**")
            st.write("Vloeiende opbouw zonder vaste blokken. Past goed bij sporters die dit prettiger rijden of in step-tests stoppen door lokale vermoeidheid.")
            st.divider()
            st.write("**Wanneer kies je deze test?**")
            st.markdown(
                "- Je je maximale vermogen centraal wilt stellen\n- Je focust op korte klimmen of top-end prestaties\n- Je een continu oplopende test prettiger vindt"
            )
            st.markdown('<p class="offer-note">Twijfel je welke test past bij jouw doel? Ik adviseer je vooraf persoonlijk.</p>', unsafe_allow_html=True)

with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Op doel: verdieping</h2>', unsafe_allow_html=True)
    st.markdown('<p class="offer-section-sub">Voor specifieke trainingsvragen.</p>', unsafe_allow_html=True)
    left, right = st.columns(2, gap="large")
    with left:
        with st.container(border=True):
            st.markdown('<h3 class="offer-card-title">Duurgrens Test (VT1)</h3>', unsafe_allow_html=True)
            st.write("Voor langeafstand-duursporters die hun duurzone nauwkeurig willen kalibreren.")
            st.write("**Doel**")
            st.write("Maximale zekerheid over je duurgrens.")
            st.write("**Wat je krijgt**")
            st.markdown("- VT1 in watt en hartslag\n- Zone 1-2 richtlijnen\n- Advies voor duurtraining")
    with right:
        with st.container(border=True):
            st.markdown('<h3 class="offer-card-title">Critical Power Testpakket (3 momenten)</h3>', unsafe_allow_html=True)
            st.write("Voor klimmen, tijdritten en pacing.")
            st.write("**Doel**")
            st.write("Prestatieprofiel en pacingstrategie per inspanningsduur.")
            st.write("**Wat je krijgt**")
            st.markdown("- Critical Power profiel ([zie uitleg CP-pagina](/Critical_Power))\n- Pacingrichtlijnen\n- Klimstrategie\n- Metabolisch profiel en trainingsaccenten")

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
        st.markdown("**Enkele test**")
        st.markdown("<p class='offer-price-big'>100 euro</p>", unsafe_allow_html=True)
        st.write("Seizoensstart aanbieding")
    with bundle_1_col:
        with st.container(border=True):
            st.markdown("<h3 class='offer-card-title'>Bundel 1</h3>", unsafe_allow_html=True)
            st.write("Meting + nameting (6-8 weken): 190 euro")
    with bundle_2_col:
        with st.container(border=True):
            st.markdown("<h3 class='offer-card-title'>Bundel 2</h3>", unsafe_allow_html=True)
            st.write("Voorseizoen + midden seizoen + na seizoen: 270 euro")
    st.write("**Verdiepende testen in overleg:**")
    st.markdown("- Duurgrens Test (VT1)\n- Critical Power (3 momenten)")
    st.markdown('<p class="offer-note">Populair bij sporters die gericht willen verbeteren.</p>', unsafe_allow_html=True)

with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Wat je altijd krijgt</h2>', unsafe_allow_html=True)
    st.markdown(
        "- De test in een helder PDF-rapport\n- Heldere nabespreking van je rapport\n- Advies en hulp bij het formuleren van doelen\n- Toegang tot de inspanningsfysiologie AI-tool (upload je rapport en neem zones en periodisering stap voor stap door, ook getraind voor hardlopen en krachttraining)"
    )

with st.container(border=True):
    st.markdown('<h2 class="offer-section-title">Plan je meting</h2>', unsafe_allow_html=True)
pad_l2, plan_bottom_col, pad_r2 = st.columns([0.2, 0.6, 0.2], gap="small")
with plan_bottom_col:
    plan_test_button("Plan je meting", key="offer_bottom_plan", page_id="aanbod", use_container_width=True)

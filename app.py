import base64
import importlib.util
import mimetypes
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

from site.ui import inject_global_css, plan_test_button, render_plan_dialog_if_open, top_nav

inject_global_css()
top_nav(active="Home")
render_plan_dialog_if_open()


@st.cache_data(show_spinner=False)
def file_to_data_uri(path: Path) -> str:
    mime_type, _ = mimetypes.guess_type(path.name)
    if mime_type is None:
        mime_type = "application/octet-stream"
    payload = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{payload}"


HERO_CANDIDATES = [
    Path("assets/hero-web.jpg"),
    Path("assets/hero-hd.jpg"),
    Path("assets/hero_hd.jpg"),
    Path("assets/hero.jpg"),
    Path("assets/hero-high.jpg"),
]

hero_path = next((p for p in HERO_CANDIDATES if p.exists()), Path("assets/hero.jpg"))
logo_path = Path("assets/logo-web.png")
if not logo_path.exists():
    logo_path = Path("assets/logo.png")

hero_uri = file_to_data_uri(hero_path)
logo_uri = file_to_data_uri(logo_path)

st.markdown(
    f"""
    <style>
      .home-hero-bleed {{
        width: 100vw;
        margin-left: calc(50% - 50vw);
        margin-right: calc(50% - 50vw);
        min-height: clamp(430px, 68vh, 760px);
        border-radius: 0 0 28px 28px;
        overflow: hidden;
        position: relative;
        background-image:
          linear-gradient(98deg, rgba(11, 38, 47, 0.76) 0%, rgba(20, 67, 79, 0.58) 44%, rgba(20, 67, 79, 0.2) 100%),
          url('{hero_uri}');
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: center;
      }}

      .home-hero-inner {{
        width: 100%;
        max-width: 1180px;
        margin: 0 auto;
        padding: clamp(1.4rem, 3vw, 2.4rem);
      }}

      .home-hero-card {{
        max-width: 730px;
        background: rgba(255, 255, 255, 0.74);
        border: 1px solid rgba(213, 226, 230, 0.72);
        border-radius: 1.2rem;
        padding: clamp(1.1rem, 2vw, 1.6rem);
        box-shadow: 0 20px 36px rgba(13, 47, 57, 0.16);
      }}

      .home-brand {{
        width: clamp(138px, 18vw, 208px);
        height: auto;
        margin-bottom: 0.85rem;
        filter: drop-shadow(0 8px 20px rgba(0, 0, 0, 0.24));
      }}

      .home-kicker {{
        margin: 0;
        font-weight: 700;
        font-size: 0.86rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #2d7480;
      }}

      .home-title {{
        margin: 0.3rem 0 0.35rem;
        font-size: clamp(2rem, 4.8vw, 3.4rem);
        line-height: 1.03;
        color: #173f49;
      }}

      .home-subtitle {{
        margin: 0;
        font-size: clamp(1rem, 1.8vw, 1.3rem);
        color: #2a6873;
        font-weight: 700;
      }}

      .home-line {{
        margin: 0.9rem 0 0.7rem;
        color: #295761;
        font-weight: 600;
      }}

      .home-copy {{
        margin: 0.38rem 0;
        color: #315761;
        line-height: 1.66;
      }}

      .home-cta {{
        margin-top: 1.1rem;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.72rem 1.2rem;
        border-radius: 999px;
        background: linear-gradient(140deg, #2d7c85 0%, #3d9199 100%);
        color: #ffffff;
        text-decoration: none !important;
        font-weight: 700;
        letter-spacing: 0.01em;
        box-shadow: 0 10px 22px rgba(22, 74, 87, 0.24);
      }}

      .home-cta:hover,
      .home-cta:visited,
      .home-cta:focus {{
        color: #ffffff;
        text-decoration: none !important;
      }}

      .home-content {{
        margin-top: 2.3rem;
      }}

      .home-mini-title {{
        margin: 0;
        color: #2b6671;
        font-size: 0.84rem;
        font-weight: 800;
        letter-spacing: 0.09em;
        text-transform: uppercase;
      }}

      .home-centered {{
        text-align: center;
      }}

      .home-service-list {{
        margin: 0.45rem 0 0;
        padding-left: 1rem;
      }}

      .home-service-list li {{
        color: #325b65;
        margin: 0.22rem 0;
      }}

      .home-ai-inline {{
        display: inline-block;
        padding: 0.22rem 0.56rem;
        border-radius: 999px;
        border: 1px solid #236ad9;
        background: #236ad9;
        color: #ffffff !important;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 0.82rem;
      }}

      .home-ai-inline:hover,
      .home-ai-inline:focus,
      .home-ai-inline:active,
      .home-ai-inline:visited {{
        background: #1f60c6;
        border-color: #1f60c6;
        color: #ffffff !important;
      }}

      .home-section {{
        margin-top: 1.45rem;
        padding: 1.25rem;
        background: rgba(255, 255, 255, 0.82);
        border: 1px solid #d7e3e6;
        border-radius: 1.08rem;
        box-shadow: 0 10px 26px rgba(19, 61, 73, 0.08);
      }}

      .home-section h2 {{
        margin: 0 0 0.7rem;
        font-size: 1.34rem;
        color: #173f49;
      }}

      .home-card {{
        background: #ffffff;
        border: 1px solid #d8e2e5;
        border-radius: 0.95rem;
        padding: 1rem;
        height: 100%;
      }}

      .home-card h3 {{
        margin: 0 0 0.44rem;
        color: #1f4f5a;
        font-size: 1.05rem;
      }}

      .home-card p {{
        margin: 0.38rem 0 0;
        color: #355e68;
        line-height: 1.6;
      }}

      .home-vspace {{
        height: 1.45rem;
      }}

      .home-map {{
        width: 100%;
        height: 190px;
        border: 0;
        border-radius: 0.7rem;
        margin-top: 0.8rem;
      }}

      .home-footer {{
        margin-top: 1.7rem;
        text-align: center;
        color: #4a6c74;
        font-weight: 600;
      }}

      @media (max-width: 900px) {{
        .home-hero-bleed {{
          min-height: clamp(360px, 56vh, 520px);
          border-radius: 0 0 20px 20px;
        }}

        .home-section {{
          padding: 1rem;
        }}

        .home-card {{
          padding: 0.88rem;
        }}

        .home-cta {{
          width: 100%;
          text-align: center;
        }}
      }}
    </style>

    <section class="home-hero-bleed">
      <div class="home-hero-inner">
        <img src="{logo_uri}" class="home-brand" alt="SportMetrics logo" />
        <div class="home-hero-card">
          <p class="home-kicker">SportMetrics Inspanningstest</p>
          <h1 class="home-title">Meten is weten</h1>
          <p class="home-subtitle">Train slim met jouw data</p>
          <p class="home-line">VO2max, drempelwaardes, zones, energieverdeling, efficientie en meer</p>
          <p class="home-copy">Ontdek de inspanningstesten van SportMetrics. Opgezet voor alle sporters die meer willen weten over hun eigen kunnen en waar hun grenzen liggen.</p>
          <p class="home-copy">Maak dit fietsjaar jouw jaar met jouw data!</p>
          <p class="home-copy">Wetenschappelijk onderbouwd, persoonlijk en professioneel uitgevoerd.</p>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

hero_pad_l, hero_action_left, hero_action_right, hero_pad_r = st.columns([0.06, 0.44, 0.44, 0.06], gap="small")
with hero_action_left:
    plan_test_button("Plan je bezoek vandaag nog", key="home_hero_plan", use_container_width=True)
with hero_action_right:
    st.link_button("Meer weten? Klik hier", "/Aanbod", use_container_width=True)

st.markdown('<div class="home-content">', unsafe_allow_html=True)

st.markdown('<p class="home-mini-title home-centered">Diensten</p>', unsafe_allow_html=True)
st.markdown(
    """
    <article class="home-card">
      <h3>Inspanningstesten, meten is weten</h3>
      <p>Ontdek jouw VO2max, je metabole profiel en je energieverdeling via wetenschappelijk onderbouwde inspanningstesten voor fietsers die gericht willen trainen en progressie inzichtelijk willen maken.</p>
      <ul class="home-service-list">
        <li>VO2max-test</li>
        <li>Drempelwaardes</li>
        <li>Wattage zones</li>
        <li>Nog meer (zie Aanbod)</li>
        <li><a class="home-ai-inline" href="/Mijn_SportTesting_AI">AI-coach</a></li>
      </ul>
    </article>
    """,
    unsafe_allow_html=True,
)
services_pad_l, services_plan_col, services_pad_r = st.columns([0.06, 0.88, 0.06], gap="small")
with services_plan_col:
    plan_test_button("Klik hier voor je afspraak", key="home_services_plan", use_container_width=True)

st.markdown('<div class="home-vspace"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <article class="home-card">
      <h3>De juiste literatuur en kennis</h3>
      <p>Start je leerproces met de kernconcepten bij VO2max en loop de webblokken bovenin de pagina door met alle kernconcepten die langs kunnen komen.</p>
    </article>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="home-vspace"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <section class="home-section">
      <h2>Start hier jouw leerproces</h2>
      <p class="home-copy">De kernbegrippen bovenin zijn interactief uitgelegd, zodat je ze direct kunt toepassen op je eigen situatie.</p>
      <p class="home-copy">Wil je daarna nog een vraag stellen? Gebruik dan de AI-chatbot rechtsboven. Die is getraind op recente literatuur en helpt je met trainingsopbouw, periodisering en het interpreteren van zones.</p>
      <p class="home-copy">Ook nadat je je eigen rapport hebt geupload, helpt de AI je graag verder in jouw fietstraject.</p>
    </section>
    """,
    unsafe_allow_html=True,
)
st.page_link("pages/4_Energiesystemen.py", label="Begin je kernbegrippen bij Energiesystemen", width="stretch")

st.markdown('<div class="home-vspace"></div>', unsafe_allow_html=True)
st.markdown('<section class="home-section"><h2>Locaties</h2></section>', unsafe_allow_html=True)
loc_left, loc_right = st.columns(2, gap="large")

with loc_left:
    st.markdown(
        """
        <article class="home-card">
          <h3>Het Marnix</h3>
          <p>Afspraak in het Marnixgebouw (Amsterdam). Persoonlijke testafname met directe uitleg en vertaling naar training.</p>
          <iframe
            class="home-map"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            src="https://www.google.com/maps?q=Marnixplein+1,+1015+ZN+Amsterdam&output=embed">
          </iframe>
        </article>
        """,
        unsafe_allow_html=True,
    )

with loc_right:
    st.markdown(
        f"""
        <article class="home-card">
          <h3>Aan huis</h3>
          <p>Mogelijk mits in bezit van een fietstrainer met wattagemeter en Bluetooth. In overleg: stuur een mailtje.</p>
          <iframe
            class="home-map"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            src="https://www.google.com/maps?q=Amsterdam&output=embed">
          </iframe>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<p class="home-footer">We zien je snel bij SportMetrics.</p>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

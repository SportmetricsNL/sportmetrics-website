import importlib.util
import sys
from pathlib import Path

import streamlit as st

try:
    from PIL import Image, ImageOps
except Exception:
    Image = None
    ImageOps = None


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


def rotate_test_photo(image_path: Path):
    if Image is None or ImageOps is None:
        return str(image_path)
    with Image.open(image_path) as image:
        fixed = ImageOps.exif_transpose(image).convert("RGB")
        return fixed.rotate(360, expand=True, fillcolor=(255, 255, 255))


def prepare_report_photo(image_path: Path):
    if Image is None or ImageOps is None:
        return str(image_path)
    with Image.open(image_path) as image:
        fixed = ImageOps.exif_transpose(image).convert("RGB")
        if fixed.width > fixed.height:
            fixed = fixed.rotate(90, expand=True, fillcolor=(255, 255, 255))
        return ImageOps.fit(fixed, (900, 1200), method=Image.LANCZOS)


def rotate_folkert_portrait(image_path: Path):
    if Image is None or ImageOps is None:
        return str(image_path)
    with Image.open(image_path) as image:
        fixed = ImageOps.exif_transpose(image).convert("RGB")
        if fixed.width > fixed.height:
            fixed = fixed.rotate(90, expand=True, fillcolor=(255, 255, 255))
        return fixed


asset_dir = Path("assets")
test_1 = asset_dir / "test_1.jpg"
test_2 = asset_dir / "test_2.jpg"
report_candidates = sorted(
    [
        path
        for path in asset_dir.glob("*")
        if path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
        and ("voorbeeldrapport" in path.name.lower() or "voorbeelrapport" in path.name.lower())
    ]
)
report_image = report_candidates[0] if report_candidates else None

folkert_candidates = sorted(
    [
        path
        for path in asset_dir.glob("folkert*")
        if path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    ]
)
folkert_photo = folkert_candidates[0] if folkert_candidates else None

st.markdown(
    """
    <style>
      .offer-hero {
        margin-top: 0.2rem;
        padding: 1.2rem 1.25rem;
        border-radius: 1.1rem;
        border: 1px solid #d5e3e7;
        background: linear-gradient(140deg, #f6fbfc 0%, #e7f1f3 100%);
        box-shadow: 0 14px 26px rgba(18, 62, 74, 0.08);
      }

      .offer-hero h1 {
        margin: 0;
        color: #184751;
        font-size: clamp(1.75rem, 3.1vw, 2.5rem);
      }

      .offer-hero p {
        margin: 0.55rem 0 0;
        color: #2e5f69;
      }

      .offer-section {
        margin-top: 1.35rem;
        padding: 1.15rem;
        border-radius: 1rem;
        border: 1px solid #d5e2e6;
        background: rgba(255, 255, 255, 0.9);
        box-shadow: 0 10px 22px rgba(21, 65, 77, 0.07);
      }

      .offer-section h2 {
        margin: 0;
        color: #1f505a;
        font-size: 1.3rem;
      }

      .offer-kicker {
        margin: 0.45rem 0 0;
        color: #2f6a74;
        font-weight: 800;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        font-size: 0.82rem;
      }

      .offer-card {
        height: 100%;
        padding: 1rem;
        border-radius: 0.92rem;
        border: 1px solid #d8e4e8;
        background: #ffffff;
      }

      .offer-card-gold {
        border: 1px solid #d6b565;
      }

      .offer-card-compact {
        padding: 0.82rem;
      }

      .offer-card-compact h3 {
        font-size: 0.98rem;
      }

      .offer-card h3 {
        margin: 0;
        color: #205561;
        font-size: 1.05rem;
      }

      .offer-card p {
        margin: 0.55rem 0 0;
        color: #315a65;
        line-height: 1.58;
      }

      .offer-list {
        margin: 0.55rem 0 0;
        padding-left: 1rem;
      }

      .offer-list li {
        margin: 0.28rem 0;
        color: #315a65;
      }

      .offer-cta {
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

      .offer-footer {
        margin-top: 1.7rem;
        text-align: center;
        color: #4a6c74;
        font-weight: 600;
      }

      .offer-note {
        margin: 0.55rem 0 0;
        color: #58757e;
        font-size: 0.9rem;
      }

      @media (max-width: 900px) {
        .offer-section {
          padding: 0.95rem;
        }

        .offer-cta {
          width: 100%;
        }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="offer-hero">
      <h1>Start jouw seizoen met een goede basismeting.</h1>
      <p>Je test met je eigen fiets, in je eigen positie en setup, zodat resultaten direct toepasbaar zijn op je training.</p>
      <p>Wil je meer duidelijkheid over wat de terminologie inhoudt? Bekijk dan de pagina Kernbegrippen bovenaan de website.</p>
    </section>
    """,
    unsafe_allow_html=True,
)
st.page_link("pages/9_Methode.py", label="Bekijk Kernbegrippen", width="stretch")

st.markdown('<section class="offer-section"><h2>Testaanbod</h2></section>', unsafe_allow_html=True)
left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.markdown(
        """
        <article class="offer-card offer-card-gold">
          <h3>Zone &amp; Drempel Test (Step) (meest gekozen)</h3>
          <p>Train op jouw fysiologie: duidelijke zones en drempels voor duur, tempo en drempeltraining.</p>
          <p><strong>Doel</strong><br/>Persoonlijke trainingssturing op basis van VT1/VT2 en zones.</p>
          <p><strong>Wat je krijgt</strong></p>
          <ul class="offer-list">
            <li>VO2peak</li>
            <li>VT1 (duurgrens) en VT2 (drempelgebied)</li>
            <li>Zones in watt en hartslag (Z1-Z5)</li>
            <li>Ademprofiel (VE, Rf, Tv)</li>
          </ul>
          <p><strong>Waarom step</strong><br/>Stabiele stappen maken VT1/VT2 vaak duidelijker. Je rijdt door tot maximaal, dus je VO2peak is volwaardig en goed vergelijkbaar over tijd.</p>
          <p><strong>Ademprofiel (kort)</strong><br/>VE is ventilatie per minuut en bestaat uit Rf (frequentie) en Tv (teugvolume): VE = Rf x Tv. Dit laat zien hoe jij opschaalt bij hogere intensiteit en helpt bij interpretatie en pacing.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with right_col:
    st.markdown(
        """
        <article class="offer-card offer-card-compact">
          <h3>Max &amp; Performance Test (Ramp)</h3>
          <p>Continu oplopende belasting met focus op maximale prestatie-uitkomsten en top-end capaciteit.</p>
          <p><strong>Doel</strong><br/>Inzicht in VO2peak, maximale prestatie en pacingrichting.</p>
          <p><strong>Wat je krijgt</strong></p>
          <ul class="offer-list">
            <li>VO2peak</li>
            <li>Maximaal vermogen en hartslagrespons</li>
            <li>VT1/VT2-indicatie en zoneadvies</li>
          </ul>
          <p><strong>Waarom ramp</strong><br/>Een vloeiende opbouw zonder vaste blokken. Past goed bij sporters die dit prettig rijden, of die in step-tests vaker stoppen door lokale vermoeidheid.</p>
          <p><strong>Belangrijk</strong><br/>Beide protocollen leveren een volwaardige VO2peak. De keuze gaat om de opbouw die het best past bij jouw doel en voorkeur.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<section class="offer-section"><h2>Op doel: verdiepende testen</h2></section>', unsafe_allow_html=True)
deep_left, deep_right = st.columns(2, gap="large")

with deep_left:
    st.markdown(
        """
        <article class="offer-card">
          <h3>Duurgrens Test (VT1)</h3>
          <p>Voor langeafstand-duursporters met focus op het scherp kalibreren van VT1.</p>
          <p><strong>Doel</strong><br/>Maximale zekerheid over je duurgrens (basis voor duurtraining en lange ritten).</p>
          <p><strong>Hoe</strong><br/>Langere stappen rond het VT1-gebied voor extra stabiliteit en zekerheid.</p>
          <p><strong>Wat je krijgt</strong></p>
          <ul class="offer-list">
            <li>VT1 in watt en hartslag</li>
            <li>Zone 1-2 richtlijnen</li>
            <li>Advies voor duurtraining en opbouw</li>
          </ul>
        </article>
        """,
        unsafe_allow_html=True,
    )

with deep_right:
    st.markdown(
        """
        <article class="offer-card">
          <h3>Critical Power Testpakket (3 momenten)</h3>
          <p>Voor klimmen, tijdritten en pacing: weten wat je kunt op meerdere inspanningsduren.</p>
          <p><strong>Doel</strong><br/>Pacingstrategie en prestatieprofiel voor verschillende duur-inspanningen.</p>
          <p><strong>Wat je krijgt</strong></p>
          <ul class="offer-list">
            <li>Critical Power profiel</li>
            <li>Pacingrichtlijnen per duur</li>
            <li>Praktische klimstrategie</li>
            <li>Inzicht in je metabolisch profiel en trainingsaccenten passend bij jouw doelen</li>
          </ul>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <section class="offer-section">
      <h2>Submaximale insteek (indien nodig)</h2>
      <p>In sommige situaties kan de Zone &amp; Drempel Test (Step) submaximaal worden uitgevoerd, bijvoorbeeld bij hart- of longproblematiek of klachten bij zware inspanning. We kiezen dan een veilige opbouw, afgestemd op jouw situatie.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="offer-section">
      <h2>Seizoensmomenten en hertesten (6-8 weken)</h2>
      <ul class="offer-list">
        <li>Voorseizoen: basismeting en plan</li>
        <li>Midden seizoen: bijsturen en zones updaten (na 6-8 weken)</li>
        <li>Na seizoen: evaluatie en nieuwe opbouw</li>
        <li>MesoCycle (6-8 weken): startmeting, gerichte trainingsfocus en hertest op een specifiek doel (bijvoorbeeld VT1 verhogen, VT2 verbeteren, VO2 ontwikkelen of pacing optimaliseren)</li>
      </ul>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <section class="offer-section">
      <h2>Prijzenpakket</h2>
      <p class="offer-kicker">Seizoensstartactie</p>
      <a class="offer-cta" href="{CTA_URL}">Boek hier</a>
    </section>
    """,
    unsafe_allow_html=True,
)
price_col_1, price_col_2, price_col_3 = st.columns(3, gap="large")

with price_col_1:
    st.markdown(
        """
        <article class="offer-card">
          <h3>Seizoensstartactie</h3>
          <p>Zone &amp; Drempel Test (Step) of Max &amp; Performance Test (Ramp).</p>
          <p><strong>Prijs:</strong> 100 euro per test</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with price_col_2:
    st.markdown(
        """
        <article class="offer-card">
          <h3>Bundel 1</h3>
          <p>Meting + nameting (6-8 weken).</p>
          <p><strong>Prijs:</strong> 190 euro</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with price_col_3:
    st.markdown(
        """
        <article class="offer-card">
          <h3>Bundel 2</h3>
          <p>Voorseizoen + midden seizoen + na seizoen.</p>
          <p><strong>Prijs:</strong> 270 euro</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <p class="offer-note"><strong>Verdiepende testen (in overleg):</strong> Duurgrens Test (VT1), Critical Power (3 momenten).</p>
    """,
    unsafe_allow_html=True,
)

st.markdown('<section class="offer-section"><h2>Altijd inbegrepen</h2></section>', unsafe_allow_html=True)
st.markdown(
    """
    <article class="offer-card">
      <ul class="offer-list">
        <li>Meetbegeleiding tijdens de test</li>
        <li>Nabespreking met uitleg van je rapport</li>
        <li>Advies en hulp bij het vormen van doelen (indien nodig)</li>
        <li>Inspanningsfysiologie AI-tool: upload je rapport en neem zones, periodisering en trainingsinrichting stap voor stap door</li>
      </ul>
    </article>
    """,
    unsafe_allow_html=True,
)

st.markdown('<section class="offer-section"><h2>Zo ziet het testen eruit</h2></section>', unsafe_allow_html=True)
photo_col_1, photo_col_2, photo_col_3 = st.columns(3, gap="large")

with photo_col_1:
    if test_1.exists():
        st.image(rotate_test_photo(test_1), width="stretch")

with photo_col_2:
    if report_image and report_image.exists():
        st.image(prepare_report_photo(report_image), width="stretch")
    else:
        st.markdown(
            """
            <article class="offer-card">
              <h3>Voorbeeldrapport ontbreekt</h3>
              <p>Voeg <strong>assets/Voorbeelrapport.png</strong> toe.</p>
            </article>
            """,
            unsafe_allow_html=True,
        )

with photo_col_3:
    if test_2.exists():
        st.image(rotate_test_photo(test_2), width="stretch")

st.markdown('<section class="offer-section"><h2>Wie is SportMetrics</h2></section>', unsafe_allow_html=True)
about_left, about_right = st.columns([1.2, 0.8], gap="large")

with about_left:
    st.markdown(
        """
        <article class="offer-card">
          <h3>Folkert Vinke</h3>
          <ul class="offer-list">
            <li>Fysiotherapeut</li>
            <li>BIG: 49936591804</li>
            <li>Gespecialiseerd en geaccrediteerd in inspanningsfysiologie</li>
            <li>MSc student Gezondheidswetenschappen</li>
          </ul>
        </article>
        """,
        unsafe_allow_html=True,
    )

with about_right:
    if folkert_photo and folkert_photo.exists():
        st.image(rotate_folkert_portrait(folkert_photo), width="stretch")
    else:
        st.markdown(
            """
            <article class="offer-card">
              <h3>Foto ontbreekt</h3>
              <p>Voeg een portretfoto toe als <strong>assets/folkert.jpg</strong>.</p>
            </article>
            """,
            unsafe_allow_html=True,
        )

st.page_link("pages/1_VO2max.py", label="Start met VO2max", width="stretch")
st.markdown(f'<a class="offer-cta" href="{CTA_URL}">Maak een afspraak</a>', unsafe_allow_html=True)
st.markdown('<p class="offer-footer">We zien je snel bij SportMetrics.</p>', unsafe_allow_html=True)

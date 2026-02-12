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


def prepare_offer_photo(image_path: Path):
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

offer_photo_candidates = sorted(
    [
        path
        for path in asset_dir.glob("*")
        if path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"} and "fotoaanbod" in path.name.lower()
    ]
)
offer_photo = offer_photo_candidates[0] if offer_photo_candidates else None

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

      .offer-photo-wrap {
        margin-top: 0.85rem;
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
      <p>Goede metingen beginnen bij betrouwbare apparatuur in jouw context. Je test met jouw eigen fiets, in jouw positie en setup, zodat resultaten direct toepasbaar zijn op je eigen training.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<section class="offer-section"><h2>Testaanbod</h2></section>', unsafe_allow_html=True)
left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.markdown(
        """
        <article class="offer-card offer-card-gold">
          <h3>De gouden standaard: VO2max-ramp test</h3>
          <p>Met een ramp test meten we:</p>
          <ul class="offer-list">
            <li>VO2max</li>
            <li>Ventilatoire drempel 1 (VT1)</li>
            <li>Ventilatoire drempel 2 (VT2)</li>
            <li>Power (wattage)</li>
            <li>Respiratoire frequentie</li>
            <li>Teugvolume</li>
            <li>Calorieverbruik per drempel</li>
          </ul>
          <p>Deze koppelen we aan:</p>
          <ul class="offer-list">
            <li>Vermogen (watt) zones</li>
            <li>Hartslagzones</li>
          </ul>
          <p><strong>Altijd inbegrepen:</strong> basisadvies + uitleg van je rapport na afloop + AI-hulptool</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with right_col:
    st.markdown(
        """
        <article class="offer-card offer-card-compact">
          <h3>Aanvullende testen</h3>
          <p>Afhankelijk van je doel zijn aanvullende testen mogelijk:</p>
          <ul class="offer-list">
            <li>Submaximale test</li>
            <li>Alleen drempeltest (VT1)</li>
            <li>Metabolic profiling (zie post CP)</li>
          </ul>
        </article>
        """,
        unsafe_allow_html=True,
    )
    if offer_photo and offer_photo.exists():
        st.markdown('<div class="offer-photo-wrap"></div>', unsafe_allow_html=True)
        _, photo_center, _ = st.columns([0.08, 0.84, 0.08], gap="small")
        with photo_center:
            st.image(prepare_offer_photo(offer_photo), width="stretch")

st.markdown(
    """
    <section class="offer-section">
      <h2>Prijzenpakket</h2>
      <p class="offer-kicker">NU ACTIE SEIZOENSSTART!</p>
    </section>
    """,
    unsafe_allow_html=True,
)
price_col_1, price_col_2, price_col_3 = st.columns(3, gap="large")

with price_col_1:
    st.markdown(
        """
        <article class="offer-card">
          <h3>Eenmalige test</h3>
          <p>Perfecte start om jezelf te sturen in training.</p>
          <p><strong>Prijs:</strong> EUR 100 (elders vaak EUR 150)</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with price_col_2:
    st.markdown(
        """
        <article class="offer-card">
          <h3>Meting + nameting</h3>
          <p>Perfect als je progressie van een seizoen of periode trainen wilt meten.</p>
          <p><strong>Prijs:</strong> EUR 190</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with price_col_3:
    st.markdown(
        """
        <article class="offer-card">
          <h3>Tussenmeting + nameting</h3>
          <p>Perfect als je tussentijdse metingen wilt hebben van jouw presteren.</p>
          <p><strong>Prijs:</strong> EUR 270</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <p class="offer-note">Aanvullende testen (Submaximale test, Alleen drempeltest (VT1), Metabolic profiling - zie post CP) in overleg.</p>
    """,
    unsafe_allow_html=True,
)

st.markdown('<section class="offer-section"><h2>Afspraak in het Marnixgebouw (Amsterdam)</h2></section>', unsafe_allow_html=True)
apt_left, apt_right = st.columns(2, gap="large")

with apt_left:
    st.markdown(
        """
        <article class="offer-card">
          <p>Het is een <strong>ramp protocol</strong> waarbij de belasting elke minuut toeneemt, zodat we stap voor stap jouw inspanningsprofiel in kaart brengen.</p>
          <ul class="offer-list">
            <li>Voorbereiding: eigen fiets, water, wielerfit, uitgerust zijn</li>
            <li>Totale duur: ongeveer 1 uur</li>
            <li>10 min warming-up</li>
            <li>Ongeveer 12 min ramp test, trapsgewijs zwaarder tot maximaal</li>
            <li>10 min cooling-down</li>
          </ul>
        </article>
        """,
        unsafe_allow_html=True,
    )

with apt_right:
    st.markdown(
        """
        <article class="offer-card">
          <h3>Aan huis</h3>
          <p>Mits fiets geinstalleerd op trainer met ERG-modus functionaliteit, wattagemeting en Bluetooth.</p>
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

from __future__ import annotations

import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st

NAV_ITEMS = [
    ("Home", "app.py"),
    ("Aanbod", "pages/8_Aanbod.py"),
    ("Methode", "pages/9_Methode.py"),
    ("VO2max", "pages/1_VO2max.py"),
    ("VT1", "pages/2_VT1.py"),
    ("VT2", "pages/3_VT2.py"),
    ("Energiesystemen", "pages/4_Energiesystemen.py"),
    ("Zonemodellen", "pages/5_Zonemodellen.py"),
    ("Critical Power", "pages/6_Critical_Power.py"),
    ("Mijn SportTesting AI", "pages/7_Mijn_SportTesting_AI.py"),
]

BOOKING_EMAIL = "folkertvinke@gmail.com"
BOOKING_STEP_COUNT = 4
BOOKING_PREFIX = "sm_booking_"
BOOKING_OPEN_KEY = f"{BOOKING_PREFIX}open"
BOOKING_PAGE_KEY = f"{BOOKING_PREFIX}page"


def _is_mobile_client() -> bool:
    try:
        ua = st.context.headers.get("User-Agent", "")
    except Exception:
        return False
    ua_lower = ua.lower()
    return any(token in ua_lower for token in ("mobile", "android", "iphone", "ipad"))


def inject_global_css() -> None:
    st.markdown(
        """
        <style>
          @import url("https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap");

          :root {
            --sm-bg: #f4f7f8;
            --sm-surface: #ffffff;
            --sm-ink: #1f363d;
            --sm-muted: #5b747d;
            --sm-accent: #2f7c85;
            --sm-accent-soft: #e3eff1;
            --sm-border: #d6e1e4;
            --sm-shadow: 0 12px 30px rgba(23, 67, 82, 0.1);
            --sm-cta-blue: #236ad9;
            --sm-cta-blue-hover: #1f60c6;
            --sm-cta-blue-active: #194fa8;
          }

          html, body, [class*="st-"] {
            font-family: "Manrope", sans-serif;
            color: var(--sm-ink);
          }

          [data-testid="stSidebar"],
          [data-testid="stSidebarNav"],
          [data-testid="stSidebarCollapsedControl"],
          [data-testid="stToolbar"],
          [data-testid="stDecoration"],
          [data-testid="stStatusWidget"],
          #MainMenu,
          header,
          footer {
            display: none !important;
          }

          [data-testid="stAppViewContainer"] {
            background:
              radial-gradient(circle at 10% 10%, #ffffff 0%, transparent 36%),
              radial-gradient(circle at 85% -5%, #e8f1f3 0%, transparent 44%),
              var(--sm-bg);
          }

          [data-testid="stAppViewContainer"] > .main {
            padding-top: 0;
          }

          .block-container {
            max-width: 1180px;
            padding-top: 1.2rem;
            padding-bottom: 3rem;
            padding-left: 1.25rem;
            padding-right: 1.25rem;
          }

          div[data-testid="stPageLink"] {
            width: 100%;
          }

          div[data-testid="stPageLink"] a {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 2.3rem;
            width: 100%;
            border-radius: 999px;
            border: 1px solid var(--sm-border);
            background: rgba(255, 255, 255, 0.9);
            color: var(--sm-muted);
            text-decoration: none;
            font-weight: 600;
            letter-spacing: 0.01em;
            font-size: 0.76rem;
            white-space: normal;
            overflow: visible;
            text-overflow: clip;
            text-align: center;
            line-height: 1.18;
            padding: 0.18rem 0.48rem;
            box-shadow: 0 3px 9px rgba(24, 56, 70, 0.05);
            transition: all 0.2s ease;
          }

          div[data-testid="stPageLink"] a:hover {
            border-color: var(--sm-accent);
            color: var(--sm-accent);
            transform: translateY(-1px);
          }

          div[data-testid="stPageLink"] a[aria-current="page"],
          div[data-testid="stPageLink"] a[aria-disabled="true"] {
            border-color: var(--sm-accent);
            background: linear-gradient(135deg, var(--sm-accent) 0%, #3f97a2 100%);
            color: #ffffff;
            box-shadow: var(--sm-shadow);
            opacity: 1;
            pointer-events: none;
          }

          div[data-testid="stButton"] > button,
          div[data-testid="stFormSubmitButton"] > button,
          div[data-testid="stLinkButton"] > a {
            border-radius: 999px !important;
            border: 1px solid var(--sm-cta-blue) !important;
            background: var(--sm-cta-blue) !important;
            color: #ffffff !important;
            font-weight: 700 !important;
            text-decoration: none !important;
            box-shadow: 0 10px 22px rgba(35, 106, 217, 0.25);
            transition: all 0.15s ease;
          }

          div[data-testid="stButton"],
          div[data-testid="stFormSubmitButton"],
          div[data-testid="stLinkButton"] {
            margin-top: 0.32rem;
            margin-bottom: 0.32rem;
          }

          div[data-testid="stButton"] > button p,
          div[data-testid="stFormSubmitButton"] > button p,
          div[data-testid="stLinkButton"] > a p {
            color: #ffffff !important;
          }

          div[data-testid="stButton"] > button:hover,
          div[data-testid="stFormSubmitButton"] > button:hover,
          div[data-testid="stLinkButton"] > a:hover {
            background: var(--sm-cta-blue-hover) !important;
            border-color: var(--sm-cta-blue-hover) !important;
            color: #ffffff !important;
          }

          div[data-testid="stButton"] > button:focus-visible,
          div[data-testid="stButton"] > button:active,
          div[data-testid="stFormSubmitButton"] > button:focus-visible,
          div[data-testid="stFormSubmitButton"] > button:active,
          div[data-testid="stLinkButton"] > a:focus-visible,
          div[data-testid="stLinkButton"] > a:active {
            background: var(--sm-cta-blue-active) !important;
            border-color: var(--sm-cta-blue-active) !important;
            color: #ffffff !important;
            box-shadow: 0 0 0 2px rgba(25, 79, 168, 0.22) !important;
          }

          div[data-testid="stButton"] > button:focus-visible p,
          div[data-testid="stButton"] > button:active p,
          div[data-testid="stFormSubmitButton"] > button:focus-visible p,
          div[data-testid="stFormSubmitButton"] > button:active p,
          div[data-testid="stLinkButton"] > a:focus-visible p,
          div[data-testid="stLinkButton"] > a:active p {
            color: #ffffff !important;
          }

          .sm-nav-space {
            height: 0.12rem;
          }

          .sm-nav-row-space {
            height: 0.3rem;
          }

          .sm-logo-wrap {
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            min-height: 100%;
            padding-top: 0;
          }

          .sm-nav-logo {
            width: 152px;
            height: auto;
            display: block;
            transform: translateY(-30%);
          }

          .sm-mobile-menu {
            margin-top: 0.2rem;
          }

          div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
            background: #ffffff !important;
            border: 1px solid var(--sm-border) !important;
            color: var(--sm-ink) !important;
          }

          div[data-testid="stSelectbox"] [data-baseweb="select"] * {
            color: var(--sm-ink) !important;
          }

          div[data-baseweb="popover"] [role="listbox"],
          div[data-baseweb="popover"] [role="option"] {
            background: #ffffff !important;
            color: var(--sm-ink) !important;
          }

          div[data-baseweb="popover"] [role="option"]:hover {
            background: #eef5f7 !important;
          }

          .sm-inline-buttons {
            margin-top: 1rem;
          }

          .sm-instagram-fab {
            position: fixed;
            right: 1rem;
            bottom: 1rem;
            z-index: 9998;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 44px;
            height: 44px;
            padding: 0;
            border-radius: 50%;
            border: 1px solid #236ad9;
            background: #236ad9;
            color: #ffffff !important;
            text-decoration: none !important;
            font-weight: 700;
            box-shadow: 0 10px 22px rgba(35, 106, 217, 0.25);
          }

          .sm-instagram-fab svg {
            width: 21px;
            height: 21px;
            fill: #ffffff;
          }

          .sm-instagram-fab:hover,
          .sm-instagram-fab:focus,
          .sm-instagram-fab:active,
          .sm-instagram-fab:visited {
            color: #ffffff !important;
            background: #1f60c6;
            border-color: #1f60c6;
            text-decoration: none !important;
          }

          @media (max-width: 1180px) {
            .block-container {
              max-width: 100%;
            }

            div[data-testid="stPageLink"] a {
              min-height: 2.2rem;
              font-size: 0.73rem;
            }
          }

          @media (max-width: 900px) {
            div[data-testid="stPageLink"] a {
              min-height: 2.1rem;
              font-size: 0.68rem;
              padding: 0.16rem 0.34rem;
            }

            .sm-nav-row-space {
              height: 0.22rem;
            }
          }

          @media (max-width: 600px) {
            .block-container {
              padding-left: 0.72rem;
              padding-right: 0.72rem;
              padding-bottom: 2rem;
            }

            div[data-testid="stPageLink"] a {
              min-height: 2.18rem;
              font-size: 0.7rem;
              padding: 0.18rem 0.36rem;
            }

            .sm-nav-logo {
              width: 146px;
              transform: translateY(-40%);
            }
          }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_data(show_spinner=False)
def _logo_data_uri(path: str) -> str:
    p = Path(path)
    payload = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{payload}"


def top_nav(active: str) -> None:
    assets_dir = Path(__file__).resolve().parents[1] / "assets"
    logo_path = assets_dir / "logo.png"
    if not logo_path.exists():
        logo_path = assets_dir / "logo-web.png"
    logo_col, nav_col = st.columns([0.14, 0.86], gap="small")

    with logo_col:
        st.markdown('<div class="sm-logo-wrap">', unsafe_allow_html=True)
        if logo_path.exists():
            st.markdown(
                f'<img class="sm-nav-logo" src="{_logo_data_uri(str(logo_path))}" alt="SportMetrics logo" />',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    with nav_col:
        if _is_mobile_client():
            labels = [label for label, _ in NAV_ITEMS]
            current_index = labels.index(active) if active in labels else 0
            st.markdown('<div class="sm-mobile-menu">', unsafe_allow_html=True)
            selected = st.selectbox("Menu", labels, index=current_index, label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
            if selected != active:
                page_map = {label: page for label, page in NAV_ITEMS}
                st.switch_page(page_map[selected])
        else:
            row_size = 5
            for row_start in range(0, len(NAV_ITEMS), row_size):
                row_items = NAV_ITEMS[row_start : row_start + row_size]
                weights = [1.15 if label == "Mijn SportTesting AI" else 1.0 for label, _ in row_items]
                columns = st.columns(weights, gap="small")
                for col, (label, page) in zip(columns, row_items):
                    with col:
                        st.page_link(page=page, label=label, disabled=(label == active), width="stretch")
                if row_start + row_size < len(NAV_ITEMS):
                    st.markdown('<div class="sm-nav-row-space"></div>', unsafe_allow_html=True)

    st.markdown('<div class="sm-nav-space"></div>', unsafe_allow_html=True)
    st.markdown(
        '<a class="sm-instagram-fab" href="https://www.instagram.com/sportmetricsnl/" target="_blank" rel="noopener noreferrer" aria-label="SportMetrics Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.75 2h8.5A5.75 5.75 0 0 1 22 7.75v8.5A5.75 5.75 0 0 1 16.25 22h-8.5A5.75 5.75 0 0 1 2 16.25v-8.5A5.75 5.75 0 0 1 7.75 2Zm0 1.5A4.25 4.25 0 0 0 3.5 7.75v8.5a4.25 4.25 0 0 0 4.25 4.25h8.5a4.25 4.25 0 0 0 4.25-4.25v-8.5A4.25 4.25 0 0 0 16.25 3.5h-8.5Zm8.94 1.8a.95.95 0 1 1 0 1.9.95.95 0 0 1 0-1.9ZM12 7a5 5 0 1 1 0 10 5 5 0 0 1 0-10Zm0 1.5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7Z"/></svg></a>',
        unsafe_allow_html=True,
    )


def _booking_defaults() -> dict[str, object]:
    return {
        f"{BOOKING_PREFIX}step": 1,
        f"{BOOKING_PREFIX}test_type": "Zone & Drempel Test (Step)",
        f"{BOOKING_PREFIX}goal": "",
        f"{BOOKING_PREFIX}ftp": "",
        f"{BOOKING_PREFIX}performance_level": "",
        f"{BOOKING_PREFIX}rides_per_week": "",
        f"{BOOKING_PREFIX}hours_per_week": 0.0,
        f"{BOOKING_PREFIX}axle_type": "",
        f"{BOOKING_PREFIX}location_preference": "",
        f"{BOOKING_PREFIX}name": "",
        f"{BOOKING_PREFIX}email": "",
        f"{BOOKING_PREFIX}phone": "",
        f"{BOOKING_PREFIX}height_cm": 0.0,
        f"{BOOKING_PREFIX}weight_kg": 0.0,
        f"{BOOKING_PREFIX}birth_date": "",
        f"{BOOKING_PREFIX}sex": "Man",
        f"{BOOKING_PREFIX}notes": "",
        f"{BOOKING_PREFIX}terms": False,
        f"{BOOKING_PREFIX}errors": [],
    }


def reset_booking_form() -> None:
    for key, value in _booking_defaults().items():
        st.session_state[key] = value
    widget_prefix = f"{BOOKING_PREFIX}w_"
    for key in list(st.session_state.keys()):
        if key.startswith(widget_prefix):
            del st.session_state[key]


def _init_booking_state() -> None:
    defaults = _booking_defaults()
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)
    st.session_state.setdefault(BOOKING_OPEN_KEY, False)
    st.session_state.setdefault(BOOKING_PAGE_KEY, "")


def _booking_value(name: str) -> object:
    return st.session_state[f"{BOOKING_PREFIX}{name}"]


def _widget_key(name: str) -> str:
    return f"{BOOKING_PREFIX}w_{name}"


def _seed_widget(name: str) -> str:
    key = _widget_key(name)
    if key not in st.session_state:
        value = _booking_value(name)
        if name == "birth_date" and not isinstance(value, str):
            value = str(value)
        st.session_state[key] = value
    return key


def _display_value(value: object, kind: str = "text") -> str:
    if kind == "number":
        try:
            as_float = float(value)
            if as_float <= 0:
                return "Niet ingevuld"
            if as_float.is_integer():
                return str(int(as_float))
            return str(as_float)
        except Exception:
            return "Niet ingevuld"
    text = str(value).strip()
    return text if text else "Niet ingevuld"


def _build_booking_mailto() -> str:
    test_type = _booking_value("test_type")
    goal = _booking_value("goal")
    ftp = _booking_value("ftp")
    performance_level = _booking_value("performance_level")
    rides_per_week = _booking_value("rides_per_week")
    hours_per_week = _booking_value("hours_per_week")
    axle_type = _booking_value("axle_type")
    location_preference = _booking_value("location_preference")
    name = _booking_value("name")
    email = _booking_value("email")
    phone = _booking_value("phone")
    height_cm = _booking_value("height_cm")
    weight_kg = _booking_value("weight_kg")
    birth_date = _booking_value("birth_date")
    sex = _booking_value("sex")
    notes = _booking_value("notes")

    subject = quote(f"Nieuwe testaanvraag: {_display_value(name)}", safe="")
    body = quote(
        "\n".join(
            [
                "Nieuwe testaanvraag via SportMetrics website",
                "",
                "BLOK 1 - TESTKEUZE",
                f"Type test: {test_type}",
                "",
                "BLOK 2 - DOEL & TRAININGSACHTERGROND",
                f"Doel test: {_display_value(goal)}",
                f"FTP: {_display_value(ftp)}",
                f"Huidig niveau: {_display_value(performance_level)}",
                f"Hoe vaak per week: {_display_value(rides_per_week)}",
                f"Uur per week: {_display_value(hours_per_week, 'number')}",
                "",
                "BLOK 3 - FIETSINFORMATIE",
                f"Type achteras: {_display_value(axle_type)}",
                f"Locatie voorkeur: {_display_value(location_preference)}",
                "",
                "BLOK 4 - PERSOONSGEGEVENS",
                f"Naam: {_display_value(name)}",
                f"E-mail: {_display_value(email)}",
                f"Telefoon: {_display_value(phone)}",
                f"Lengte (cm): {_display_value(height_cm, 'number')}",
                f"Gewicht (kg): {_display_value(weight_kg, 'number')}",
                f"Geboortedatum: {_display_value(birth_date)}",
                f"Sekse: {_display_value(sex)}",
                "",
                "BLOK 5 - BIJZONDERHEDEN",
                f"Opmerkingen/vragen/medisch: {_display_value(notes)}",
                "",
                "BLOK 6 - VOORWAARDEN",
                "Akkoord met voorwaarden: Ja",
            ]
        ),
        safe="",
    )
    return f"mailto:{BOOKING_EMAIL}?subject={subject}&body={body}"


def _render_step_navigation(step: int) -> None:
    left, right = st.columns([1, 1], gap="small")
    with left:
        if step > 1 and st.button("Terug", key=f"{BOOKING_PREFIX}back_{step}", use_container_width=True):
            st.session_state[f"{BOOKING_PREFIX}step"] = step - 1
            st.rerun()

    with right:
        if step < BOOKING_STEP_COUNT:
            if st.button("Volgende", key=f"{BOOKING_PREFIX}next_{step}", use_container_width=True):
                st.session_state[f"{BOOKING_PREFIX}errors"] = []
                st.session_state[f"{BOOKING_PREFIX}step"] = step + 1
                st.rerun()
        else:
            if bool(_booking_value("terms")):
                st.link_button("Plan mijn test", _build_booking_mailto(), use_container_width=True)
            elif st.button("Plan mijn test", key=f"{BOOKING_PREFIX}submit", use_container_width=True):
                st.session_state[f"{BOOKING_PREFIX}errors"] = ["Je moet akkoord gaan met de algemene voorwaarden."]


def _render_plan_form() -> None:
    _init_booking_state()
    step = int(_booking_value("step"))
    if bool(_booking_value("terms")) and st.session_state.get(f"{BOOKING_PREFIX}errors"):
        st.session_state[f"{BOOKING_PREFIX}errors"] = []
    st.caption(f"Stap {step} van {BOOKING_STEP_COUNT}")
    st.progress(step / BOOKING_STEP_COUNT)

    if st.button("Sluiten", key=f"{BOOKING_PREFIX}close_top", use_container_width=False):
        st.session_state[BOOKING_OPEN_KEY] = False
        st.rerun()

    for error in st.session_state.get(f"{BOOKING_PREFIX}errors", []):
        st.error(error)

    if step == 1:
        st.markdown("**Blok 1 - Testkeuze**")
        test_type = st.radio(
            "Welk type test wil je plannen?",
            [
                "Zone & Drempel Test (Step)",
                "Max & Performance Test (Ramp)",
                "Duurgrens Test (VT1)",
                "Critical Power Testpakket (3 momenten)",
            ],
            key=_seed_widget("test_type"),
        )
        st.session_state[f"{BOOKING_PREFIX}test_type"] = test_type
        st.markdown("**Blok 2 - Doel & trainingsachtergrond**")
        goal = st.text_area("Wat is het doel van je test?", key=_seed_widget("goal"), height=90)
        st.session_state[f"{BOOKING_PREFIX}goal"] = goal
        ftp = st.text_input("FTP (optioneel)", key=_seed_widget("ftp"))
        st.session_state[f"{BOOKING_PREFIX}ftp"] = ftp
        performance_level = st.text_area(
            "Of omschrijf kort je huidige niveau",
            key=_seed_widget("performance_level"),
            height=70,
        )
        st.session_state[f"{BOOKING_PREFIX}performance_level"] = performance_level
        rides_per_week = st.selectbox(
            "Hoe vaak fiets je per week?",
            ["", "1-2 keer", "3-4 keer", "5+ keer"],
            format_func=lambda x: "Kies een optie" if x == "" else x,
            key=_seed_widget("rides_per_week"),
        )
        st.session_state[f"{BOOKING_PREFIX}rides_per_week"] = rides_per_week
        hours_per_week = st.number_input(
            "Hoeveel uur per week?",
            min_value=0.0,
            step=0.5,
            key=_seed_widget("hours_per_week"),
        )
        st.session_state[f"{BOOKING_PREFIX}hours_per_week"] = hours_per_week
    elif step == 2:
        st.markdown("**Blok 3 - Fietsinformatie**")
        axle_type = st.selectbox(
            "Type achteras",
            ["", "Quick release (wiel los met draaiklem)", "Through axle (as los met inbus)"],
            format_func=lambda x: "Kies een optie" if x == "" else x,
            key=_seed_widget("axle_type"),
        )
        st.session_state[f"{BOOKING_PREFIX}axle_type"] = axle_type
        location_preference = st.selectbox(
            "Locatie voorkeur",
            [
                "",
                "Marnixgebouw (Amsterdam)",
                "Aan huis (mits hometrainer met Bluetooth, wattagemeting en ERG-modus)",
            ],
            format_func=lambda x: "Kies een optie" if x == "" else x,
            key=_seed_widget("location_preference"),
        )
        st.session_state[f"{BOOKING_PREFIX}location_preference"] = location_preference
        st.markdown("**Blok 4 - Persoonsgegevens**")
        name = st.text_input("Naam", key=_seed_widget("name"))
        st.session_state[f"{BOOKING_PREFIX}name"] = name
        email = st.text_input("E-mailadres", key=_seed_widget("email"))
        st.session_state[f"{BOOKING_PREFIX}email"] = email
        phone = st.text_input("Telefoonnummer", key=_seed_widget("phone"))
        st.session_state[f"{BOOKING_PREFIX}phone"] = phone
        height_cm = st.number_input("Lengte (cm)", min_value=0.0, step=1.0, key=_seed_widget("height_cm"))
        st.session_state[f"{BOOKING_PREFIX}height_cm"] = height_cm
        weight_kg = st.number_input("Gewicht (kg)", min_value=0.0, step=0.1, key=_seed_widget("weight_kg"))
        st.session_state[f"{BOOKING_PREFIX}weight_kg"] = weight_kg
    elif step == 3:
        st.markdown("**Aanvullende gegevens**")
        birth_date = st.text_input(
            "Geboortedatum (dd-mm-jjjj)",
            key=_seed_widget("birth_date"),
            placeholder="bijv. 14-08-1990",
        )
        st.session_state[f"{BOOKING_PREFIX}birth_date"] = birth_date
        sex = st.radio("Sekse", ["Man", "Vrouw", "Anders"], key=_seed_widget("sex"), horizontal=True)
        st.session_state[f"{BOOKING_PREFIX}sex"] = sex
        notes = st.text_area(
            "Opmerkingen / vragen / medische bijzonderheden",
            key=_seed_widget("notes"),
            height=110,
        )
        st.session_state[f"{BOOKING_PREFIX}notes"] = notes
    else:
        st.markdown("**Controleer je gegevens**")
        st.markdown(
            f"""
            - **Type test:** {_display_value(_booking_value("test_type"))}
            - **Doel:** {_display_value(_booking_value("goal"))}
            - **FTP:** {_display_value(_booking_value("ftp"))}
            - **Huidig niveau:** {_display_value(_booking_value("performance_level"))}
            - **Fietsen per week:** {_display_value(_booking_value("rides_per_week"))}
            - **Uren per week:** {_display_value(_booking_value("hours_per_week"), "number")}
            - **Type achteras:** {_display_value(_booking_value("axle_type"))}
            - **Locatie voorkeur:** {_display_value(_booking_value("location_preference"))}
            - **Naam:** {_display_value(_booking_value("name"))}
            - **E-mail:** {_display_value(_booking_value("email"))}
            - **Telefoon:** {_display_value(_booking_value("phone"))}
            - **Lengte (cm):** {_display_value(_booking_value("height_cm"), "number")}
            - **Gewicht (kg):** {_display_value(_booking_value("weight_kg"), "number")}
            - **Geboortedatum:** {_display_value(_booking_value("birth_date"))}
            - **Sekse:** {_display_value(_booking_value("sex"))}
            - **Bijzonderheden:** {_display_value(_booking_value("notes"))}
            """
        )
        terms = st.checkbox(
            "Ik ga akkoord met de algemene voorwaarden en heb deze gelezen op de website.",
            key=_seed_widget("terms"),
        )
        st.session_state[f"{BOOKING_PREFIX}terms"] = bool(terms)
        st.caption("Na klikken op 'Plan mijn test' openen we je mailapp met alle ingevulde gegevens.")

    _render_step_navigation(step)


if hasattr(st, "dialog"):

    @st.dialog("Plan je test")
    def _open_plan_dialog() -> None:
        _render_plan_form()

else:

    def _open_plan_dialog() -> None:
        st.warning("Popup wordt niet ondersteund in deze Streamlit-versie.")
        _render_plan_form()


def plan_test_button(
    label: str = "Plan je meting",
    *,
    key: str,
    page_id: str,
    use_container_width: bool = False,
) -> None:
    if st.button(label, key=key, use_container_width=use_container_width):
        open_now = bool(st.session_state.get(BOOKING_OPEN_KEY, False))
        current_page = st.session_state.get(BOOKING_PAGE_KEY, "")
        if not open_now:
            reset_booking_form()
            st.session_state[BOOKING_OPEN_KEY] = True
            st.session_state[BOOKING_PAGE_KEY] = page_id
        elif current_page != page_id:
            st.session_state[BOOKING_PAGE_KEY] = page_id
        st.rerun()


def render_plan_dialog_if_open(page_id: str) -> None:
    _init_booking_state()
    if st.session_state.get(BOOKING_OPEN_KEY, False) and st.session_state.get(BOOKING_PAGE_KEY) == page_id:
        _open_plan_dialog()
    elif st.session_state.get(BOOKING_OPEN_KEY, False) and st.session_state.get(BOOKING_PAGE_KEY) != page_id:
        st.session_state[BOOKING_OPEN_KEY] = False

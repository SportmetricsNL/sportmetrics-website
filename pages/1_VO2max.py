import importlib.util
import sys
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="VO2max - SportMetrics",
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
top_nav(active="VO2max")

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "logo.png"
if not LOGO_PATH.exists():
    LOGO_PATH = BASE_DIR / "1.png"

logo_data_uri = ""
if LOGO_PATH.exists():
    logo_b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    logo_data_uri = f"data:image/png;base64,{logo_b64}"

HARD_IMAGE_PATH = BASE_DIR / "hoe-hard-je-bent.png"
if not HARD_IMAGE_PATH.exists():
    HARD_IMAGE_PATH = BASE_DIR / "hoe-hard-je-bent.jpg"

hard_image_uri = ""
if HARD_IMAGE_PATH.exists():
    hard_b64 = base64.b64encode(HARD_IMAGE_PATH.read_bytes()).decode("utf-8")
    mime = "image/png"
    if HARD_IMAGE_PATH.suffix.lower() in {".jpg", ".jpeg"}:
        mime = "image/jpeg"
    hard_image_uri = f"data:{mime};base64,{hard_b64}"

HTML_PAGE = r"""
<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>VO2max - SportMetrics</title>
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Spectral:wght@400;600&display=swap");

    :root {
      --sand: #f6f1ea;
      --clay: #e9ddd2;
      --ink: #1e2a2f;
      --muted: #5c6b73;
      --sea: #2f7c85;
      --deep: #0f4c5c;
      --sun: #f4b66a;
      --peach: #f1c9a9;
      --card: #fffdf6;
      --card-strong: #ffffff;
      --border: rgba(30, 42, 47, 0.12);
      --shadow: 0 18px 50px rgba(15, 76, 92, 0.18);
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: "Spectral", "Times New Roman", serif;
      color: var(--ink);
      background: radial-gradient(1200px 800px at 10% -10%, #ffffff 0%, var(--sand) 60%, var(--clay) 100%);
    }

    .logo-pattern {
      position: fixed;
      inset: 0;
      background-image: url('{{LOGO_DATA_URI}}');
      background-repeat: repeat;
      background-position: center;
      background-size: 140px;
      opacity: 0.07;
      mix-blend-mode: multiply;
      pointer-events: none;
      z-index: 1;
    }

    .bg-shape {
      position: fixed;
      inset: auto;
      width: 480px;
      height: 480px;
      border-radius: 50%;
      background: radial-gradient(circle at 30% 30%, rgba(47, 124, 133, 0.28), rgba(47, 124, 133, 0.02));
      z-index: -1;
    }
    .bg-shape.one { top: -120px; right: -120px; }
    .bg-shape.two { bottom: -200px; left: -140px; background: radial-gradient(circle, rgba(244, 182, 106, 0.35), rgba(244, 182, 106, 0.02)); }

    nav {
      position: fixed;
      top: 28px;
      right: 26px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 14px 14px;
      box-shadow: var(--shadow);
      z-index: 4;
      max-width: 190px;
    }
    nav h4 {
      margin: 0 0 6px;
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
    }
    .nav-link {
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-decoration: none;
      color: var(--muted);
      display: flex;
      gap: 6px;
      align-items: center;
      transition: color 0.2s ease;
    }
    .nav-link span {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--clay);
      border: 1px solid var(--border);
    }
    .nav-link.active { color: var(--deep); font-weight: 600; }
    .nav-link.active span { background: var(--sea); border-color: var(--sea); }

    .progress {
      height: 6px;
      background: rgba(47, 124, 133, 0.12);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 6px;
    }
    .progress span { display: block; height: 100%; width: 0%; background: var(--sea); transition: width 0.2s ease; }

    main {
      position: relative;
      z-index: 3;
      max-width: 1100px;
      margin: 0 auto;
      padding: 64px 24px 120px;
    }

    section {
      margin: 0 0 72px;
      padding: 36px;
      border-radius: 26px;
      background: var(--card);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      transition: all 0.7s ease;
    }
    body.enable-animations section { opacity: 0; transform: translateY(20px); }
    body.enable-animations section.in-view { opacity: 1; transform: translateY(0); }

    .hero {
      padding: 54px 44px;
      background: linear-gradient(140deg, #ffffff, #f6e7d6);
    }
    .hero h1 {
      font-family: "Space Grotesk", sans-serif;
      font-size: clamp(2.2rem, 3.4vw, 3.4rem);
      margin: 0 0 12px;
      color: var(--deep);
    }
    .hero p {
      font-size: 1.05rem;
      color: var(--muted);
      margin: 0;
      max-width: 720px;
    }
    .hero .hero-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
      margin-top: 28px;
    }
    .hero .stat {
      padding: 16px 18px;
      background: var(--card-strong);
      border-radius: 16px;
      border: 1px solid var(--border);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.95rem;
      color: var(--muted);
    }
    .hero .stat strong { display: block; color: var(--deep); font-size: 1.1rem; }

    h2 {
      font-family: "Space Grotesk", sans-serif;
      margin: 0 0 12px;
      color: var(--deep);
      font-size: 1.8rem;
    }
    h3 {
      font-family: "Space Grotesk", sans-serif;
      margin: 0 0 8px;
      color: var(--deep);
    }
    p { margin: 0 0 14px; color: var(--ink); line-height: 1.55; }
    .muted { color: var(--muted); }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
    }
    .card {
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 16px 18px;
    }
    .pill {
      display: inline-block;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.72rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: 999px;
      margin-bottom: 10px;
    }

    .slider-box {
      margin-top: 18px;
      padding: 18px;
      border-radius: 18px;
      border: 1px dashed rgba(47, 124, 133, 0.4);
      background: #eef5f4;
    }
    .slider-box label {
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
    }
    .slider-box input[type="range"] { width: 100%; margin: 10px 0 6px; }
    .mix-row {
      display: grid;
      grid-template-columns: 130px 1fr 54px;
      gap: 12px;
      align-items: center;
      margin: 10px 0;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.85rem;
    }
    .mix-bar {
      background: #eef5f4;
      border-radius: 999px;
      overflow: hidden;
      height: 10px;
      border: 1px solid rgba(15, 76, 92, 0.2);
    }
    .mix-bar span {
      display: block;
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--sea), var(--deep));
      border-radius: 999px;
      transition: width 0.3s ease;
    }
    .mix-value { text-align: right; color: var(--muted); }

    .callout {
      background: #f3e4d2;
      border: 1px solid #e8cfae;
      padding: 16px 18px;
      border-radius: 18px;
      font-family: "Space Grotesk", sans-serif;
    }

    .tab-list {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin: 12px 0 18px;
    }
    .tab-btn {
      border: 1px solid var(--border);
      background: var(--card-strong);
      font-family: "Space Grotesk", sans-serif;
      padding: 8px 14px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .tab-btn.active { background: var(--deep); color: #fff; border-color: var(--deep); }
    .tab-panel { display: none; }
    .tab-panel.active { display: block; }

    .fatigue-controls {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin: 14px 0 18px;
    }
    .fatigue-btn {
      border: 1px solid var(--border);
      background: var(--card-strong);
      font-family: "Space Grotesk", sans-serif;
      padding: 8px 14px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .fatigue-btn.active { background: var(--deep); color: #fff; border-color: var(--deep); }

    .chain-track {
      display: grid;
      grid-template-columns: minmax(90px, 1fr) 28px minmax(110px, 1fr) 28px minmax(90px, 1fr);
      align-items: center;
      gap: 10px;
      margin: 12px 0 8px;
    }
    .chain-node {
      padding: 12px 10px;
      border-radius: 14px;
      border: 1px solid var(--border);
      background: var(--card-strong);
      font-family: "Space Grotesk", sans-serif;
      text-align: center;
      font-size: 0.9rem;
    }
    .chain-node.active {
      background: #eef5f4;
      border-color: rgba(47, 124, 133, 0.35);
      color: var(--deep);
      box-shadow: 0 10px 24px rgba(47, 124, 133, 0.12);
    }
    .chain-arrow {
      font-family: "Space Grotesk", sans-serif;
      font-size: 1.1rem;
      color: var(--muted);
      text-align: center;
    }
    .genetics-pill {
      display: inline-block;
      margin-top: 8px;
      padding: 6px 12px;
      border-radius: 999px;
      border: 1px dashed rgba(47, 124, 133, 0.35);
      background: #eef5f4;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.8rem;
      color: var(--deep);
    }
    .genetics-pill.active {
      border-color: rgba(47, 124, 133, 0.6);
      background: #dfeeee;
    }

    .interval-strip {
      display: grid;
      grid-template-columns: repeat(7, minmax(70px, 1fr));
      gap: 10px;
      margin-top: 16px;
    }
    .interval-block {
      border-radius: 14px;
      padding: 12px 10px;
      text-align: center;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.8rem;
      border: 1px solid var(--border);
    }
    .interval-work {
      background: var(--deep);
      color: #fff;
      border-color: var(--deep);
    }
    .interval-rest {
      background: #f3e4d2;
      color: var(--ink);
      border-color: #e8cfae;
    }

    .quote-image {
      width: 100%;
      height: auto;
      display: block;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: #ffffff;
    }
    .image-fallback {
      margin-top: 8px;
      color: var(--muted);
      font-size: 0.9rem;
    }

    .summary-list {
      margin: 0;
      padding-left: 18px;
    }
    .summary-list li {
      margin: 0 0 10px;
    }

    .footer {
      text-align: center;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
      color: var(--muted);
    }

    @media (max-width: 980px) {
      nav { display: none; }
      section { padding: 28px; }
      .mix-row { grid-template-columns: 110px 1fr 48px; }
    }

    @media (max-width: 720px) {
      main { padding: 40px 16px 90px; }
      section { padding: 18px; margin: 0 0 36px; }
      .hero { padding: 24px 18px; }
      .hero h1 { font-size: clamp(1.8rem, 6vw, 2.4rem); }
      .hero .hero-grid { grid-template-columns: 1fr; }
      .grid-3 { grid-template-columns: 1fr; }
      .mix-row { grid-template-columns: 1fr; gap: 6px; }
      .mix-value { text-align: left; }
      .tab-btn { width: 100%; text-align: center; }
      .fatigue-btn { width: 100%; text-align: center; }
      .chain-track { grid-template-columns: 1fr; }
      .chain-arrow { display: none; }
      .interval-strip { grid-template-columns: repeat(2, minmax(110px, 1fr)); }
      .card { padding: 14px; }
    }

    @media (prefers-reduced-motion: reduce) {
      * { scroll-behavior: auto; }
      section { transition: none; }
      body.enable-animations section { opacity: 1; transform: none; }
    }
  </style>
</head>
<body>
  <div class="logo-pattern" aria-hidden="true"></div>
  <div class="bg-shape one"></div>
  <div class="bg-shape two"></div>

  <nav aria-label="Navigatie">
    <h4>Route</h4>
    <a class="nav-link" href="#intro" data-section="intro"><span></span>Intro</a>
    <a class="nav-link" href="#definitie" data-section="definitie"><span></span>Definitie</a>
    <a class="nav-link" href="#keten" data-section="keten"><span></span>Keten</a>
    <a class="nav-link" href="#trainen" data-section="trainen"><span></span>Trainen</a>
    <a class="nav-link" href="#zone2" data-section="zone2"><span></span>Zone 2</a>
    <a class="nav-link" href="#meten" data-section="meten"><span></span>Meten</a>
    <a class="nav-link" href="#sportmetrics" data-section="sportmetrics"><span></span>SportMetrics</a>
    <a class="nav-link" href="#samenvatting" data-section="samenvatting"><span></span>Samenvatting</a>
    <div class="progress"><span id="progress-bar"></span></div>
  </nav>

  <main>
    <section id="intro" class="hero" data-title="Intro">
      <span class="pill">VO2max</span>
      <h1>VO2max: de gouden standaard, maar meer dan hard gaan</h1>
      <p>VO2max is je maximale zuurstofopname: hoeveel O2 je per minuut kunt opnemen, transporteren en gebruiken om ATP te maken. Het is je aerobe plafond. Niet de enige voorspeller van prestatie, maar wel een kernanker in je fysiologisch profiel.</p>
      <div class="hero-grid">
        <div class="stat"><strong>Aerobe plafond</strong>Maximale O2-opname bepaalt hoe hoog je aerobe motor kan.</div>
        <div class="stat"><strong>Niet alles</strong>Zelfde VO2max kan anders presteren door drempels, efficiency en pacing.</div>
        <div class="stat"><strong>Trainbaar</strong>Je kunt het plafond verhogen door slim te doseren.</div>
      </div>
    </section>

    <section id="definitie" data-title="Definitie">
      <h2>Wat het precies is, en wat het niet is</h2>
      <div class="grid-3">
        <div class="card">
          <h3>Definitie</h3>
          <p>VO2max = maximale O2-opname (ml/min of ml per kg per minuut). Het is de maximale aerobe energie die je kunt leveren.</p>
        </div>
        <div class="card">
          <h3>Wat het niet is</h3>
          <img id="hard-image" class="quote-image" src="{{HARD_IMAGE_URI}}" alt="Hoe hard je bent" />
          <p id="hard-fallback" class="image-fallback">Het is geen directe maat voor hoe hard je bent.</p>
          <p class="muted">Je drempels, efficiency en pacing bepalen hoe je dat plafond benut.</p>
        </div>
        <div class="card">
          <h3>Waarom het telt</h3>
          <p>Het is een anker om training te positioneren en progressie te volgen.</p>
        </div>
      </div>
    </section>

    <section id="keten" data-title="Keten">
      <h2>De keten die VO2max begrenst</h2>
      <p>VO2max wordt bepaald door de hele keten van aanvoer en gebruik. Trainen verschuift waar de bottleneck ligt.</p>
      <div class="tab-list" role="tablist" aria-label="Keten">
        <button class="tab-btn active" data-tab="longen" role="tab">Longen</button>
        <button class="tab-btn" data-tab="hart" role="tab">Hart & bloed</button>
        <button class="tab-btn" data-tab="spieren" role="tab">Spieren</button>
      </div>
      <div class="tab-panel active" id="tab-longen" role="tabpanel">
        <div class="card">
          <h3>Ventilatie en gaswisseling</h3>
          <p>De longen leveren de O2 aan die het systeem in kan. Goede ventilatie en gaswisseling zijn de start van de keten.</p>
        </div>
      </div>
      <div class="tab-panel" id="tab-hart" role="tabpanel">
        <div class="card">
          <h3>Cardiac output</h3>
          <p>Slagvolume maal hartfrequentie bepaalt hoeveel zuurstofrijk bloed per minuut kan worden vervoerd.</p>
        </div>
      </div>
      <div class="tab-panel" id="tab-spieren" role="tabpanel">
        <div class="card">
          <h3>Gebruik in de spieren</h3>
          <p>Capillairen en mitochondrien bepalen hoe goed de spieren O2 omzetten naar ATP.</p>
        </div>
      </div>

      <div class="slider-box" aria-live="polite">
        <label for="bottleneck">Waar ligt de bottleneck vandaag?</label>
        <input id="bottleneck" type="range" min="0" max="100" value="50" />
        <div class="mix-row">
          <div>Aanvoer</div>
          <div class="mix-bar"><span id="mix-delivery"></span></div>
          <div class="mix-value" id="mix-delivery-value">0%</div>
        </div>
        <div class="mix-row">
          <div>Gebruik</div>
          <div class="mix-bar"><span id="mix-use"></span></div>
          <div class="mix-value" id="mix-use-value">0%</div>
        </div>
      </div>

      <h3>Waar treedt vermoeidheid op na maximaal gaan?</h3>
      <p>Na maximaal gaan valt de keten vaak het eerst uit bij longen, hart of spieren. Welke plek limiterend is, verschilt per persoon en is deels genetisch bepaald.</p>
      <div class="fatigue-controls" role="tablist" aria-label="Vermoeidheid">
        <button class="fatigue-btn active" data-fatigue="longen" role="tab">Longen</button>
        <button class="fatigue-btn" data-fatigue="hart" role="tab">Hart</button>
        <button class="fatigue-btn" data-fatigue="spieren" role="tab">Spieren</button>
        <button class="fatigue-btn" data-fatigue="genetisch" role="tab">Genetisch</button>
      </div>
      <div class="chain-track" aria-hidden="true">
        <div class="chain-node active" data-node="longen">Longen</div>
        <div class="chain-arrow">→</div>
        <div class="chain-node" data-node="hart">Hart & bloed</div>
        <div class="chain-arrow">→</div>
        <div class="chain-node" data-node="spieren">Spieren</div>
      </div>
      <div class="genetics-pill" id="genetics-pill">Genetisch profiel bepaalt startpunt en plafond</div>
      <div class="card" id="fatigue-panel">
        <h3 id="fatigue-title">Longen</h3>
        <p id="fatigue-body">Maximale ademarbeid en gaswisseling kunnen limiteren. Dit is deels trainbaar, maar ook genetisch begrensd.</p>
      </div>
    </section>

    <section id="trainen" data-title="Trainen">
      <h2>Hoe verhoog je VO2max?</h2>
      <p>In de praktijk draait het om genoeg tijd dichtbij je maximale aerobe output. Je dwingt een hoge zuurstofvraag af en prikkelt zowel centrale als perifere factoren.</p>
      <div class="grid-3">
        <div class="card">
          <h3>Tijd bij het plafond</h3>
          <p>Niet sprinten, maar lang genoeg hoog blijven zodat je minuten "bij max" opbouwt.</p>
        </div>
        <div class="card">
          <h3>Voorbeeld: Noorse 4x4</h3>
          <p>4 blokken van 4 minuten op een intensiteit die je snel richting zeer hoge ademdruk en VO2 brengt, met herstel ertussen.</p>
        </div>
        <div class="card">
          <h3>Herhaalbaarheid</h3>
          <p>De kwaliteit zit in het kunnen herhalen van hoge minuten, niet in een enkele piek.</p>
        </div>
      </div>
      <div class="callout">Doel: zoveel mogelijk minuten dicht bij je VO2-plafond verzamelen zonder te sprinten.</div>
      <div class="interval-strip" aria-label="Noorse 4x4 schema">
        <div class="interval-block interval-work">4 min hoog</div>
        <div class="interval-block interval-rest">3 min herstel</div>
        <div class="interval-block interval-work">4 min hoog</div>
        <div class="interval-block interval-rest">3 min herstel</div>
        <div class="interval-block interval-work">4 min hoog</div>
        <div class="interval-block interval-rest">3 min herstel</div>
        <div class="interval-block interval-work">4 min hoog</div>
      </div>
      <p class="muted">Richt je op lang genoeg hoog blijven zodat je minuten bij het plafond opbouwt.</p>
    </section>

    <section id="zone2" data-title="Zone 2">
      <h2>Waarom zone 2 essentieel blijft</h2>
      <p>Alleen hoog-intensief werk is zelden de snelste route omhoog. Het fundament is een grote aerobe basis.</p>
      <div class="grid-3">
        <div class="card">
          <h3>Meer capaciteit</h3>
          <p>Meer mitochondrien en doorbloeding vergroten je aerobe motor.</p>
        </div>
        <div class="card">
          <h3>Efficienter systeem</h3>
          <p>Betere vetoxidatie en lagere herstelkosten maken consistent volume mogelijk.</p>
        </div>
        <div class="card">
          <h3>Betere VO2-trainbaarheid</h3>
          <p>Een sterke basis zorgt dat je hoge blokken vaker kunt herhalen en verwerken.</p>
        </div>
      </div>
      <div class="callout">Zone 2 rond VT1 is de motor van volume en adaptatie.</div>
    </section>

    <section id="meten" data-title="Meten">
      <h2>Meten verslaat formules</h2>
      <p>Horloges, standaardformules en percentages geven een model. Met ademgasanalyse krijg je een meting met minder individuele foutmarge.</p>
      <div class="tab-list" role="tablist" aria-label="Meten">
        <button class="tab-btn active" data-tab="schatting" role="tab">Schattingen</button>
        <button class="tab-btn" data-tab="meting" role="tab">Meting</button>
      </div>
      <div class="tab-panel active" id="tab-schatting" role="tabpanel">
        <div class="card">
          <h3>Model</h3>
          <p>Percentages van HRmax, 220-leeftijd, FTP-only en horloge-schattingen zijn generieke aannames.</p>
        </div>
      </div>
      <div class="tab-panel" id="tab-meting" role="tabpanel">
        <div class="card">
          <h3>Ademgasanalyse</h3>
          <p>Je ziet output (watt/tempo), respons (HR) en interne adem- en zuurstofrespons. Daarmee kun je VO2max en VT1/VT2 precies plaatsen.</p>
        </div>
      </div>
    </section>

    <section id="sportmetrics" data-title="SportMetrics">
      <h2>Wat je praktisch krijgt bij SportMetrics</h2>
      <div class="grid-3">
        <div class="card">
          <h3>VO2max plafond</h3>
          <p>Objectieve bepaling van jouw aerobe plafond.</p>
        </div>
        <div class="card">
          <h3>Progressie richting plafond</h3>
          <p>Hoe snel je richting VO2max gaat bij oplopend vermogen.</p>
        </div>
        <div class="card">
          <h3>Vertaling naar zones</h3>
          <p>VT1/VT2 en wattage-zones gekoppeld aan jouw profiel.</p>
        </div>
      </div>
      <p class="muted">Het doel is niet een mooi getal, maar een profiel om zone 2 en VO2max-werk gericht te doseren.</p>
    </section>

    <section id="samenvatting" data-title="Samenvatting">
      <h2>Samenvatting</h2>
      <ul class="summary-list">
        <li>VO2max is je aerobe plafond: hoeveel O2 je maximaal kunt opnemen en gebruiken.</li>
        <li>Het plafond verhoog je met veel minuten dicht bij max, zoals 4x4-blokken.</li>
        <li>Zone 2 rond VT1 bouwt de basis zodat hoge blokken beter te herhalen zijn.</li>
        <li>Met ademgasanalyse plaats je VO2max en VT1/VT2 precies, in plaats van generieke formules.</li>
      </ul>
      <p class="footer">We zien je snel bij SportMetrics.</p>
    </section>
  </main>

  <script>
    document.body.classList.add("enable-animations");

    const sections = Array.from(document.querySelectorAll("section[data-title]"));
    const navLinks = Array.from(document.querySelectorAll(".nav-link"));
    const progressBar = document.getElementById("progress-bar");

    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
        }
      });
    }, { threshold: 0.2 });

    sections.forEach((section) => revealObserver.observe(section));

    const spyObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          navLinks.forEach((link) => link.classList.toggle("active", link.dataset.section === entry.target.id));
        }
      });
    }, { threshold: 0.55 });

    sections.forEach((section) => spyObserver.observe(section));

    window.addEventListener("scroll", () => {
      const doc = document.documentElement;
      const scrollTop = doc.scrollTop || document.body.scrollTop;
      const scrollHeight = doc.scrollHeight - doc.clientHeight;
      const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
      progressBar.style.width = `${progress}%`;
    });

    const chainButtons = Array.from(document.querySelectorAll("#keten .tab-btn"));
    const chainPanels = {
      longen: document.getElementById("tab-longen"),
      hart: document.getElementById("tab-hart"),
      spieren: document.getElementById("tab-spieren")
    };

    chainButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const target = button.dataset.tab;
        chainButtons.forEach((btn) => btn.classList.toggle("active", btn === button));
        Object.entries(chainPanels).forEach(([key, panel]) => {
          panel.classList.toggle("active", key === target);
        });
      });
    });

    const measureButtons = Array.from(document.querySelectorAll("#meten .tab-btn"));
    const measurePanels = {
      schatting: document.getElementById("tab-schatting"),
      meting: document.getElementById("tab-meting")
    };

    measureButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const target = button.dataset.tab;
        measureButtons.forEach((btn) => btn.classList.toggle("active", btn === button));
        Object.entries(measurePanels).forEach(([key, panel]) => {
          panel.classList.toggle("active", key === target);
        });
      });
    });

    const bottleneck = document.getElementById("bottleneck");

    function updateBottleneck() {
      const value = parseInt(bottleneck.value, 10);
      const delivery = value;
      const use = 100 - value;
      document.getElementById("mix-delivery").style.width = `${delivery}%`;
      document.getElementById("mix-use").style.width = `${use}%`;
      document.getElementById("mix-delivery-value").textContent = `${delivery}%`;
      document.getElementById("mix-use-value").textContent = `${use}%`;
    }

    bottleneck.addEventListener("input", updateBottleneck);
    updateBottleneck();

    const fatigueButtons = Array.from(document.querySelectorAll(".fatigue-btn"));
    const fatigueNodes = Array.from(document.querySelectorAll(".chain-node"));
    const geneticsPill = document.getElementById("genetics-pill");
    const fatigueTitle = document.getElementById("fatigue-title");
    const fatigueBody = document.getElementById("fatigue-body");

    const fatigueCopy = {
      longen: {
        title: "Longen",
        text: "Maximale ademarbeid en gaswisseling kunnen limiteren. De aanleg is deels genetisch, training kan efficientie verbeteren."
      },
      hart: {
        title: "Hart",
        text: "Cardiac output begrenst vaak het plafond. Slagvolume en hartgrootte zijn deels genetisch, maar wel trainbaar."
      },
      spieren: {
        title: "Spieren",
        text: "Lokale benutting (mitochondrien, capillairen) en ionenbalans bepalen hoe lang je hoog kunt blijven. Sterk trainbaar."
      },
      genetisch: {
        title: "Genetisch",
        text: "Je startpunt en plafond voor VO2max zijn deels genetisch bepaald. Training bepaalt hoe dicht je bij dat plafond komt."
      }
    };

    function setFatigue(key) {
      const data = fatigueCopy[key];
      if (!data) return;
      fatigueTitle.textContent = data.title;
      fatigueBody.textContent = data.text;
      fatigueButtons.forEach((btn) => btn.classList.toggle("active", btn.dataset.fatigue === key));
      fatigueNodes.forEach((node) => node.classList.toggle("active", node.dataset.node === key));
      if (geneticsPill) {
        geneticsPill.classList.toggle("active", key === "genetisch");
      }
    }

    fatigueButtons.forEach((button) => {
      button.addEventListener("click", () => {
        setFatigue(button.dataset.fatigue);
      });
    });

    setFatigue("longen");

    const hardImage = document.getElementById("hard-image");
    const hardFallback = document.getElementById("hard-fallback");
    if (hardImage && hardFallback) {
      const src = hardImage.getAttribute("src");
      if (src) {
        hardFallback.style.display = "none";
      } else {
        hardImage.style.display = "none";
      }
    }
  </script>
</body>
</html>
"""

HTML_PAGE = HTML_PAGE.replace("{{LOGO_DATA_URI}}", logo_data_uri)
HTML_PAGE = HTML_PAGE.replace("{{HARD_IMAGE_URI}}", hard_image_uri)

components.html(HTML_PAGE, height=4800, scrolling=True)

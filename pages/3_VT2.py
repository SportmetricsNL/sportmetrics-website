
import importlib.util
import sys
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="VT2 - SportMetrics",
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
top_nav(active="VT2")

BASE_DIR = Path(__file__).parent
ROOT_DIR = BASE_DIR.parent
LOGO_PATH = ROOT_DIR / "assets" / "logo.png"

logo_data_uri = ""
if LOGO_PATH.exists():
    logo_b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    logo_data_uri = f"data:image/png;base64,{logo_b64}"

HTML_PAGE = r"""
<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>VT2 - SportMetrics</title>
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Spectral:wght@400;600&display=swap");

    :root {
      --sand: #edf4f6;
      --clay: #dce8eb;
      --ink: #1d363d;
      --muted: #58717a;
      --sea: #3a8791;
      --deep: #2b6c76;
      --sun: #8fbcc5;
      --peach: #c9dfe4;
      --card: #f7fbfc;
      --card-strong: #ffffff;
      --border: rgba(40, 78, 87, 0.14);
      --shadow: 0 14px 34px rgba(19, 61, 73, 0.11);
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
    .bg-shape.two { bottom: -200px; left: -140px; background: radial-gradient(circle, rgba(143, 188, 197, 0.32), rgba(143, 188, 197, 0.04)); }

    nav {
      display: none;
      position: fixed;
      top: 28px;
      right: 26px;
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
      max-width: 1180px;
      margin: 0 auto;
      padding: 64px 24px 120px;
    }

    section {
      margin: 0 0 64px;
      padding: 36px;
      border-radius: 26px;
      background: linear-gradient(160deg, rgba(255, 255, 255, 0.93), rgba(242, 249, 250, 0.86));
      box-shadow: var(--shadow);
      border: 1px solid rgba(56, 101, 112, 0.18);
      transition: all 0.7s ease;
    }
    body.enable-animations section { opacity: 0; transform: translateY(20px); }
    body.enable-animations section.in-view { opacity: 1; transform: translateY(0); }

    .hero {
      padding: 54px 44px;
      background: linear-gradient(140deg, #ffffff, #e6f0f3);
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

    .drift-chart {
      margin-top: 16px;
      display: grid;
      grid-template-columns: repeat(10, minmax(32px, 1fr));
      gap: 6px;
      align-items: end;
      height: 120px;
    }
    .drift-bar {
      width: 100%;
      border-radius: 8px 8px 4px 4px;
      background: rgba(47, 124, 133, 0.2);
      border: 1px solid rgba(47, 124, 133, 0.35);
      height: 40%;
      transition: height 0.4s ease, background 0.4s ease;
    }
    .drift-bar.active {
      background: var(--deep);
      border-color: var(--deep);
    }

    .vt2-bar {
      margin-top: 14px;
      position: relative;
      height: 16px;
      border-radius: 999px;
      background: #eef5f4;
      border: 1px solid rgba(15, 76, 92, 0.2);
      overflow: hidden;
    }
    .vt2-window {
      position: absolute;
      top: 0;
      bottom: 0;
      width: 18%;
      left: 62%;
      border-radius: 999px;
      background: rgba(47, 124, 133, 0.32);
    }
    .vt2-marker {
      position: absolute;
      top: -4px;
      width: 2px;
      height: 24px;
      background: var(--deep);
      left: 70%;
    }

    .stepper {
      display: grid;
      grid-template-columns: repeat(8, minmax(68px, 1fr));
      gap: 10px;
      margin-top: 16px;
    }
    .step {
      padding: 10px 8px;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: var(--card-strong);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.8rem;
      text-align: center;
      color: var(--muted);
    }
    .step.active {
      background: var(--deep);
      color: #fff;
      border-color: var(--deep);
    }

    .callout {
      background: #e8f1f4;
      border: 1px solid #bfd5db;
      padding: 16px 18px;
      border-radius: 18px;
      font-family: "Space Grotesk", sans-serif;
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
      .stepper { grid-template-columns: repeat(4, minmax(70px, 1fr)); }
      .card { padding: 14px; }
      .drift-chart { grid-template-columns: repeat(5, minmax(36px, 1fr)); }
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
    <a class="nav-link" href="#mechanisme" data-section="mechanisme"><span></span>Mechanisme</a>
    <a class="nav-link" href="#gebied" data-section="gebied"><span></span>Gebied</a>
    <a class="nav-link" href="#ramp" data-section="ramp"><span></span>Ramp-test</a>
    <a class="nav-link" href="#training" data-section="training"><span></span>Training</a>
    <a class="nav-link" href="#meten" data-section="meten"><span></span>Meten</a>
    <a class="nav-link" href="#samenvatting" data-section="samenvatting"><span></span>Samenvatting</a>
    <div class="progress"><span id="progress-bar"></span></div>
  </nav>

  <main>
    <section id="intro" class="hero" data-title="Intro">
      <span class="pill">VT2</span>
      <h1>VT2: de tweede drempel is een shift naar non-steady state</h1>
      <p>VT2 markeert het punt waarop inspanning voor de meeste sporters niet meer lang stabiel blijft. Ademdruk en vermoeidheidsopbouw nemen snel toe: de overgang naar echt zwaar werk.</p>
      <div class="hero-grid">
        <div class="stat"><strong>Non-steady state</strong>Je lichaam kan de interne balans niet meer lang stabiel houden.</div>
        <div class="stat"><strong>Hoge ademdruk</strong>Ventilatie stijgt disproportioneel bij gelijke belasting.</div>
        <div class="stat"><strong>Drempelanker</strong>VT2 positioneert threshold en zwaar tempo-werk.</div>
      </div>
    </section>

    <section id="definitie" data-title="Definitie">
      <h2>Wat VT2 precies is</h2>
      <div class="grid-3">
        <div class="card">
          <h3>Tweede overgang</h3>
          <p>VE versnelt opnieuw ten opzichte van VO2 en wattage.</p>
        </div>
        <div class="card">
          <h3>Ademhaling limiteert pacing</h3>
          <p>Niet omdat je “buiten adem” bent, maar omdat de regulatie steeds zwaarder wordt.</p>
        </div>
        <div class="card">
          <h3>Praktisch</h3>
          <p>Je komt in een domein waar steady werken steeds moeilijker wordt.</p>
        </div>
      </div>
    </section>

    <section id="mechanisme" data-title="Mechanisme">
      <h2>Waarom VT2 anders voelt</h2>
      <p>Rond VT2 leunt je lichaam sterker op snelle koolhydraat-ATP, waardoor de metabole stabiliteit afneemt. Drift wordt snel zichtbaar.</p>
      <div class="slider-box" aria-live="polite">
        <label for="drift-level">Drift bij gelijk vermogen</label>
        <input id="drift-level" type="range" min="1" max="10" value="6" />
        <div class="drift-chart" id="drift-chart">
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
          <div class="drift-bar"></div>
        </div>
        <p class="muted">Drift = progressieve toename van interne belasting (HR/VE) bij gelijk vermogen.</p>
      </div>
    </section>

    <section id="gebied" data-title="Gebied">
      <h2>VT2 is een gebied, geen exact punt</h2>
      <p>VT2 schuift met vermoeidheid, warmte, voeding, protocol en meetruis. Daarom behandelen we het als ankergebied.</p>
      <div class="slider-box" aria-live="polite">
        <label for="vt2-shift">Dagvorm / omstandigheden</label>
        <input id="vt2-shift" type="range" min="-10" max="10" value="0" />
        <div class="vt2-bar">
          <div class="vt2-window" id="vt2-window"></div>
          <div class="vt2-marker" id="vt2-marker"></div>
        </div>
        <p class="muted">Het ankergebied schuift mee, maar blijft hetzelfde fysiologische domein.</p>
      </div>
    </section>

    <section id="ramp" data-title="Ramp-test">
      <h2>VT2 in een ramp-test</h2>
      <p>Door vaste stappen zie je precies waar ventilatie versnelt. HR loopt soms later mee (HR-lag), daarom koppelen we VT2 aan ademrespons.</p>
      <div class="slider-box" aria-live="polite">
        <label for="ramp-step">Kies een stap in de test</label>
        <input id="ramp-step" type="range" min="1" max="8" value="6" />
        <div class="stepper" id="stepper">
          <div class="step">Step 1</div>
          <div class="step">Step 2</div>
          <div class="step">Step 3</div>
          <div class="step">Step 4</div>
          <div class="step">Step 5</div>
          <div class="step">Step 6</div>
          <div class="step">Step 7</div>
          <div class="step">Step 8</div>
        </div>
        <div class="card" id="ramp-detail">
          <h3>Ventilatie versnelt</h3>
          <p>Rond VT2 zie je dat VE opnieuw versnelt en HR nog kan achterlopen.</p>
        </div>
      </div>
      <div class="callout">Ademrespons + wattage geeft een scherp anker. HR alleen kan vertraging hebben.</div>
    </section>

    <section id="training" data-title="Training">
      <h2>Waar VT2 voor dient (en waar niet)</h2>
      <div class="grid-3">
        <div class="card">
          <h3>Thresholdblokken</h3>
          <p>Duurzaam hard, maar niet maximaal. Grote prestatiewinst, hoge herstelkosten.</p>
        </div>
        <div class="card">
          <h3>Pacing</h3>
          <p>Net onder/omheen VT2 voor lange inspanningen.</p>
        </div>
        <div class="card">
          <h3>Begrenzen</h3>
          <p>Voorkom onbewust te veel "duur" werk in dit domein.</p>
        </div>
      </div>
      <p class="muted">VT2 is geen tempo dat je dagelijks kunt stapelen alsof het duur is.</p>
    </section>

    <section id="meten" data-title="Meten">
      <h2>VT2 versus FTP en CP</h2>
      <p>FTP is bruikbaar maar vaak protocol-afhankelijk. VT2 is een fysiologisch anker uit ademrespons. CP komt uit de power-duration relatie.</p>
      <div class="grid-3">
        <div class="card">
          <h3>FTP</h3>
          <p>Performance-schatting met foutmarges, afhankelijk van motivatie, pacing en protocol.</p>
        </div>
        <div class="card">
          <h3>VT2</h3>
          <p>Fysiologisch anker: shift naar non-steady state zichtbaar in ademrespons en VO2.</p>
        </div>
        <div class="card">
          <h3>CP</h3>
          <p>Power-duration model; goed voor het grensgebied van beperkte capaciteit.</p>
        </div>
      </div>
    </section>

    <section id="samenvatting" data-title="Samenvatting">
      <h2>Samenvatting</h2>
      <ul class="summary-list">
        <li>VT2 is de tweede ventilatoire overgang: VE versnelt opnieuw bij hogere belasting.</li>
        <li>Het markeert een shift naar non-steady state, waar drift snel toeneemt.</li>
        <li>VT2 is een gebied dat schuift met dagvorm en omstandigheden.</li>
        <li>Ademrespons + wattage plaatsen VT2 scherper dan HR alleen (HR-lag).</li>
        <li>VT2 is een fysiologisch anker; FTP/CP zijn bruikbaar maar andere kaders.</li>
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

    const driftLevel = document.getElementById("drift-level");
    const driftBars = Array.from(document.querySelectorAll("#drift-chart .drift-bar"));

    function updateDrift() {
      const level = parseInt(driftLevel.value, 10);
      driftBars.forEach((bar, idx) => {
        const height = 30 + idx * 5 + level * 2;
        bar.style.height = `${Math.min(height, 110)}px`;
        bar.classList.toggle("active", idx >= driftBars.length - Math.ceil(level / 2));
      });
    }

    driftLevel.addEventListener("input", updateDrift);
    updateDrift();

    const vt2Shift = document.getElementById("vt2-shift");
    const vt2Window = document.getElementById("vt2-window");
    const vt2Marker = document.getElementById("vt2-marker");

    function updateVT2Shift() {
      const shift = parseInt(vt2Shift.value, 10);
      let center = 70 + shift * 2;
      center = Math.max(25, Math.min(90, center));
      const width = 18;
      vt2Window.style.left = `${center - width / 2}%`;
      vt2Marker.style.left = `${center}%`;
    }

    vt2Shift.addEventListener("input", updateVT2Shift);
    updateVT2Shift();

    const rampStep = document.getElementById("ramp-step");
    const rampSteps = Array.from(document.querySelectorAll("#stepper .step"));
    const rampDetail = document.getElementById("ramp-detail");

    const rampCopy = [
      "Rustig begin: ademrespons volgt vermogen vrijwel lineair.",
      "Ventilatie stijgt licht, nog weinig drift.",
      "VO2 stijgt stevig, ventilatie blijft beheersbaar.",
      "Overgangsgebied richting VT2, ademdruk neemt toe.",
      "Rond VT2 begint VE opnieuw duidelijk te versnellen.",
      "HR kan nog achterlopen terwijl VE versnelt (HR-lag).",
      "Drift wordt snel zichtbaar bij langer aanhouden.",
      "Boven VT2 neemt ademdruk en vermoeidheid snel toe."
    ];

    function updateRamp() {
      const step = parseInt(rampStep.value, 10);
      rampSteps.forEach((el, idx) => {
        el.classList.toggle("active", idx === step - 1);
      });
      const text = rampCopy[step - 1] || rampCopy[0];
      rampDetail.querySelector("p").textContent = text;
    }

    rampStep.addEventListener("input", updateRamp);
    updateRamp();
  </script>
</body>
</html>
"""

HTML_PAGE = HTML_PAGE.replace("{{LOGO_DATA_URI}}", logo_data_uri)

components.html(HTML_PAGE, height=4800, scrolling=True)

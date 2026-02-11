
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="VT1 - SportMetrics",
    layout="wide",
)

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "logo.png"
if not LOGO_PATH.exists():
    LOGO_PATH = BASE_DIR / "1.png"

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
  <title>VT1 - SportMetrics</title>
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

    .vt1-bar {
      margin-top: 14px;
      position: relative;
      height: 16px;
      border-radius: 999px;
      background: #eef5f4;
      border: 1px solid rgba(15, 76, 92, 0.2);
      overflow: hidden;
    }
    .vt1-window {
      position: absolute;
      top: 0;
      bottom: 0;
      width: 18%;
      left: 41%;
      border-radius: 999px;
      background: rgba(47, 124, 133, 0.3);
    }
    .vt1-marker {
      position: absolute;
      top: -4px;
      width: 2px;
      height: 24px;
      background: var(--deep);
      left: 50%;
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
      background: #f3e4d2;
      border: 1px solid #e8cfae;
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
    <a class="nav-link" href="#sportmetrics" data-section="sportmetrics"><span></span>SportMetrics</a>
    <a class="nav-link" href="#samenvatting" data-section="samenvatting"><span></span>Samenvatting</a>
    <div class="progress"><span id="progress-bar"></span></div>
  </nav>

  <main>
    <section id="intro" class="hero" data-title="Intro">
      <span class="pill">VT1</span>
      <h1>VT1: de eerste drempel is een shift in ademregulatie</h1>
      <p>VT1 markeert het moment waarop je ademhaling disproportioneel begint toe te nemen ten opzichte van de belasting. Geen schakelaar, maar een duidelijke overgang in hoe je lichaam de interne balans stabiel houdt.</p>
      <div class="hero-grid">
        <div class="stat"><strong>Eerste overgang</strong>VE stijgt relatief sneller dan VO2 en vermogen.</div>
        <div class="stat"><strong>Duurzaam domein</strong>Je zit nog duurzaam, maar regulatie wordt merkbaar zwaarder.</div>
        <div class="stat"><strong>Praktisch anker</strong>VT1 kalibreert jouw zone 2 in plaats van generieke percentages.</div>
      </div>
    </section>

    <section id="definitie" data-title="Definitie">
      <h2>Wat VT1 precies is</h2>
      <div class="grid-3">
        <div class="card">
          <h3>Ventilatoire overgang</h3>
          <p>VE (ventilatie) gaat relatief sneller stijgen dan VO2 en het vermogen.</p>
        </div>
        <div class="card">
          <h3>Regulatiepunt</h3>
          <p>Ademhaling en circulatie moeten merkbaar harder werken, terwijl je nog duurzaam kunt werken.</p>
        </div>
        <div class="card">
          <h3>Geen vetzone</h3>
          <p>VT1 is geen vetverbrandingsschakelaar, maar een shift in regulatie.</p>
        </div>
      </div>
    </section>

    <section id="mechanisme" data-title="Mechanisme">
      <h2>Waarom ventilatie toeneemt</h2>
      <p>Bij hogere intensiteit stijgt de koolhydraatbijdrage en verandert de zuur-base balans. Je lichaam ventileert meer om CO2 af te voeren en pH te stabiliseren. Dat is het begin van duidelijke drift.</p>
      <div class="slider-box" aria-live="polite">
        <label for="intensity">Sleep: inspanningsintensiteit</label>
        <input id="intensity" type="range" min="0" max="100" value="35" />
        <div class="mix-row">
          <div>Ventilatie (VE)</div>
          <div class="mix-bar"><span id="mix-ve"></span></div>
          <div class="mix-value" id="mix-ve-value">0%</div>
        </div>
        <div class="mix-row">
          <div>CO2 / pH-regulatie</div>
          <div class="mix-bar"><span id="mix-co2"></span></div>
          <div class="mix-value" id="mix-co2-value">0%</div>
        </div>
        <div class="mix-row">
          <div>Drift</div>
          <div class="mix-bar"><span id="mix-drift"></span></div>
          <div class="mix-value" id="mix-drift-value">0%</div>
        </div>
      </div>
    </section>

    <section id="gebied" data-title="Gebied">
      <h2>VT1 is een gebied, geen exact punt</h2>
      <p>VT1 verschuift met dagvorm, protocol, cadans, voeding en warmte. Daarom rapporteren we VT1 als ankergebied in plaats van een exact wattpunt.</p>
      <div class="slider-box" aria-live="polite">
        <label for="vt1-shift">Dagvorm / omstandigheden</label>
        <input id="vt1-shift" type="range" min="-10" max="10" value="0" />
        <div class="vt1-bar">
          <div class="vt1-window" id="vt1-window"></div>
          <div class="vt1-marker" id="vt1-marker"></div>
        </div>
        <p class="muted">Het ankergebied schuift mee, maar blijft hetzelfde fysiologische domein.</p>
      </div>
    </section>

    <section id="ramp" data-title="Ramp-test">
      <h2>VT1 in een ramp-test</h2>
      <p>In de ramp-test zie je rond VT1 een versnelling in de ademrespons. Door vaste stappen en duur kun je het moment scherp koppelen aan wattage.</p>
      <div class="slider-box" aria-live="polite">
        <label for="ramp-step">Kies een stap in de test</label>
        <input id="ramp-step" type="range" min="1" max="8" value="4" />
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
          <h3>Ademrespons versnelt</h3>
          <p>Hier zie je dat VE sneller toeneemt dan VO2. HR kan nog licht achterlopen (HR-lag).</p>
        </div>
      </div>
      <div class="callout">Ademrespons + wattage geeft een scherp anker. HR alleen kan vertraging hebben.</div>
    </section>

    <section id="training" data-title="Training">
      <h2>Waarom VT1 zo belangrijk is</h2>
      <div class="grid-3">
        <div class="card">
          <h3>Duurvolume en consistentie</h3>
          <p>VT1 is vaak de hoogste intensiteit die je lang kunt stapelen met lage herstelkosten.</p>
        </div>
        <div class="card">
          <h3>Efficientie</h3>
          <p>Meer aerobe efficientie: minder ventilatoire druk bij hetzelfde vermogen.</p>
        </div>
        <div class="card">
          <h3>Pacing</h3>
          <p>Boven VT1 starten geeft sneller drift en onnodige kosten.</p>
        </div>
      </div>
      <p class="muted">VT1 valt vaak in wat veel modellen "zone 2" noemen. VT1 is het fysiologische anker om die zone te kalibreren.</p>
    </section>

    <section id="sportmetrics" data-title="SportMetrics">
      <h2>Wat je praktisch krijgt bij SportMetrics</h2>
      <div class="grid-3">
        <div class="card">
          <h3>VT1 als ankergebied</h3>
          <p>Positionering op basis van VO2, VE, ademfrequentie en teugvolume, gekoppeld aan vermogen en HR.</p>
        </div>
        <div class="card">
          <h3>Direct toepasbaar</h3>
          <p>VT1 wordt vertaald naar uitvoerbare trainingszones en advies.</p>
        </div>
        <div class="card">
          <h3>Transparant meten</h3>
          <p>We meten geen VCO2, dus rapporteren geen exacte RER of substraatpercentages.</p>
        </div>
      </div>
      <div class="callout">VT1 gebruiken we als intensiteitsanker dat direct uitvoerbaar is in training.</div>
    </section>

    <section id="samenvatting" data-title="Samenvatting">
      <h2>Samenvatting</h2>
      <ul class="summary-list">
        <li>VT1 is de eerste ventilatoire overgang: VE versnelt relatief ten opzichte van VO2 en watt.</li>
        <li>Het is geen vetverbrandingsschakelaar maar een regulatiepunt met meer drift.</li>
        <li>VT1 is een gebied dat schuift met dagvorm en omstandigheden, daarom rapporteren we een ankergebied.</li>
        <li>In de ramp-test koppelen we VT1 scherp aan vermogen via ademrespons; HR kan vertragen.</li>
      </ul>
      <p class="footer">We zien je graag bij SportMetrics.</p>
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

    const intensity = document.getElementById("intensity");

    function updateIntensity() {
      const value = parseInt(intensity.value, 10);
      const ve = Math.max(0, (value - 25) / 75);
      const co2 = Math.max(0, (value - 35) / 65);
      const drift = Math.max(0, (value - 50) / 50);

      document.getElementById("mix-ve").style.width = `${Math.round(ve * 100)}%`;
      document.getElementById("mix-co2").style.width = `${Math.round(co2 * 100)}%`;
      document.getElementById("mix-drift").style.width = `${Math.round(drift * 100)}%`;

      document.getElementById("mix-ve-value").textContent = `${Math.round(ve * 100)}%`;
      document.getElementById("mix-co2-value").textContent = `${Math.round(co2 * 100)}%`;
      document.getElementById("mix-drift-value").textContent = `${Math.round(drift * 100)}%`;
    }

    intensity.addEventListener("input", updateIntensity);
    updateIntensity();

    const vt1Shift = document.getElementById("vt1-shift");
    const vt1Window = document.getElementById("vt1-window");
    const vt1Marker = document.getElementById("vt1-marker");

    function updateVT1Shift() {
      const shift = parseInt(vt1Shift.value, 10);
      let center = 50 + shift * 2;
      center = Math.max(15, Math.min(85, center));
      const width = 18;
      vt1Window.style.left = `${center - width / 2}%`;
      vt1Marker.style.left = `${center}%`;
    }

    vt1Shift.addEventListener("input", updateVT1Shift);
    updateVT1Shift();

    const rampStep = document.getElementById("ramp-step");
    const rampSteps = Array.from(document.querySelectorAll("#stepper .step"));
    const rampDetail = document.getElementById("ramp-detail");

    const rampCopy = [
      "Rustig begin: ademrespons volgt vermogen vrijwel lineair.",
      "Ademfrequentie stijgt licht, nog weinig drift.",
      "VO2 stijgt stevig, ventilatie blijft beheersbaar.",
      "Hier rond VT1 begint VE sneller te stijgen dan VO2.",
      "Duidelijker regulatie: ademarbeid neemt toe.",
      "HR kan nog achterlopen terwijl VE versnelt (HR-lag).",
      "Drift wordt zichtbaar bij langer aanhouden.",
      "Boven VT1 neemt ventilatoire druk snel toe."
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

import importlib.util
import sys
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Zone-modellen en Z1-5 - SportMetrics",
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
top_nav(active="Zonemodellen")

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
  <title>Zone-modellen en Z1-5 - SportMetrics</title>
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

    body::before {
      content: "";
      position: fixed;
      inset: 0;
      background-image: url('{{LOGO_DATA_URI}}');
      background-repeat: repeat;
      background-position: center;
      background-size: 140px;
      opacity: 0.07;
      mix-blend-mode: multiply;
      pointer-events: none;
      z-index: 2;
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

    .domain-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-top: 18px;
    }
    .domain {
      padding: 14px 16px;
      border-radius: 16px;
      border: 1px solid rgba(47, 124, 133, 0.22);
      background: #eef5f4;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.9rem;
    }

    .callout {
      background: #e8f1f4;
      border: 1px solid #bfd5db;
      padding: 16px 18px;
      border-radius: 18px;
      font-family: "Space Grotesk", sans-serif;
    }

    .zone-picker {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin: 12px 0 18px;
    }
    .zone-btn {
      border: 1px solid var(--border);
      background: var(--card-strong);
      font-family: "Space Grotesk", sans-serif;
      padding: 8px 14px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .zone-btn.active { background: var(--deep); color: #fff; border-color: var(--deep); }
    .zone-panel { display: none; }
    .zone-panel.active { display: block; }

    .zone-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
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
    }

    @media (max-width: 720px) {
      main { padding: 40px 16px 90px; }
      section { padding: 22px; margin: 0 0 48px; }
      .hero { padding: 30px 22px; }
      .hero h1 { font-size: clamp(1.8rem, 6vw, 2.4rem); }
      .hero .hero-grid { grid-template-columns: 1fr; }
      .grid-3 { grid-template-columns: 1fr; }
      .domain-strip { grid-template-columns: 1fr; }
      .zone-grid { grid-template-columns: 1fr; }
      .zone-btn { width: 100%; text-align: center; }
    }

    @media (prefers-reduced-motion: reduce) {
      * { scroll-behavior: auto; }
      section { transition: none; }
      body.enable-animations section { opacity: 1; transform: none; }
    }
  </style>
</head>
<body>
  <div class="bg-shape one"></div>
  <div class="bg-shape two"></div>

  <nav aria-label="Navigatie">
    <h4>Route</h4>
    <a class="nav-link" href="#intro" data-section="intro"><span></span>Intro</a>
    <a class="nav-link" href="#waarom" data-section="waarom"><span></span>Waarom</a>
    <a class="nav-link" href="#ankers" data-section="ankers"><span></span>Ankers</a>
    <a class="nav-link" href="#zones" data-section="zones"><span></span>Z1-5</a>
    <a class="nav-link" href="#praktijk" data-section="praktijk"><span></span>Praktijk</a>
    <div class="progress"><span id="progress-bar"></span></div>
  </nav>

  <main>
    <section id="intro" class="hero" data-title="Intro">
      <span class="pill">Zone-modellen</span>
      <h1>Trainingszones zijn modellen, geen hokjes</h1>
      <p>Zone-indelingen zijn vereenvoudigingen van hoe het lichaam reageert op oplopende inspanningsintensiteit. Of je nu 3, 5, 6 of 7 zones gebruikt: de onderliggende fysiologie verandert niet. In de kern draait het om drie domeinen onder en boven twee drempels: VT1 en VT2.</p>
      <div class="hero-grid">
        <div class="stat"><strong>Zelfde fysiologie</strong>Meer zones betekent een fijnere verdeling, niet een ander systeem.</div>
        <div class="stat"><strong>Drie domeinen</strong>Onder VT1, tussen VT1 en VT2, boven VT2.</div>
        <div class="stat"><strong>Hulpmiddel</strong>Zones maken complexiteit hanteerbaar, niet het doel op zich.</div>
      </div>
    </section>

    <section id="waarom" data-title="Waarom">
      <h2>Waarom zones bestaan</h2>
      <p>Zones bestaan om belasting te doseren, niet om inspanning in hokjes te stoppen. Ze helpen voorkomen dat je alles "grijs" rijdt en maken training herhaalbaar en voorspelbaar.</p>
      <div class="grid-3">
        <div class="card">
          <h3>Rust echt rustig</h3>
          <p>Zones helpen rustige dagen echt rustig te houden.</p>
        </div>
        <div class="card">
          <h3>Hard echt hard</h3>
          <p>Ze maken het makkelijker om intensieve blokken scherp genoeg te doseren.</p>
        </div>
        <div class="card">
          <h3>Gerichte adaptatie</h3>
          <p>Je stuurt aanpassingen in energie- en herstel systemen doelgerichter.</p>
        </div>
      </div>
      <div class="callout">Belangrijk: het aantal zones is minder belangrijk dan de fysiologische domeinen eronder.</div>
    </section>

    <section id="ankers" data-title="Ankers">
      <h2>Waar hangen zones aan</h2>
      <p>Vrijwel alle zone-modellen komen voort uit het 3-fasenmodel, gebaseerd op twee ventilatoire drempels:</p>
      <div class="grid-3">
        <div class="card">
          <h3>VT1</h3>
          <p>Eerste duidelijke verandering in ademhaling en interne belasting. Het anker voor "easy" en basis.</p>
        </div>
        <div class="card">
          <h3>VT2</h3>
          <p>Tweede omslagpunt waarbij langdurig steady werken moeilijk wordt. Het anker voor "hard".</p>
        </div>
        <div class="card">
          <h3>Meetbaar</h3>
          <p>Zichtbaar via ventilatie, lactaatgedrag en te vertalen naar watt, hartslag en pace.</p>
        </div>
      </div>
      <p class="muted">VT1 en VT2 zijn in de praktijk exacter dan vaste HRmax-percentages, omdat percentages groepsgemiddelden zijn.</p>
      <div class="domain-strip">
        <div class="domain"><strong>Onder VT1:</strong> laag en duurzaam</div>
        <div class="domain"><strong>Tussen VT1-VT2:</strong> matig, meer drift</div>
        <div class="domain"><strong>Boven VT2:</strong> hoog, beperkt houdbaar</div>
      </div>
    </section>

    <section id="zones" data-title="Z1-5">
      <h2>Zones 1-5 in de praktijk</h2>
      <p>Klik een zone om de herkenning, het trainingsdoel en de praktische inzet te zien.</p>
      <div class="zone-picker" role="tablist" aria-label="Zones">
        <button class="zone-btn active" data-zone="z1" role="tab">Zone 1</button>
        <button class="zone-btn" data-zone="z2" role="tab">Zone 2</button>
        <button class="zone-btn" data-zone="z3" role="tab">Zone 3</button>
        <button class="zone-btn" data-zone="z4" role="tab">Zone 4</button>
        <button class="zone-btn" data-zone="z5" role="tab">Zone 5</button>
      </div>

      <div class="zone-panel active" id="zone-z1" role="tabpanel">
        <div class="zone-grid">
          <div class="card"><strong>Herkenning</strong><br/>Zeer rustig. Praattempo moeiteloos. Ademhaling laag en stabiel.</div>
          <div class="card"><strong>Wat train je</strong><br/>Herstelcapaciteit, doorbloeding, techniek en cadans zonder metabole stress.</div>
          <div class="card"><strong>Helpt bij</strong><br/>Sneller herstellen, extra volume zonder vermoeidheid, week-na-week consistent trainen.</div>
          <div class="card"><strong>Gebruik</strong><br/>Herstelritten, in- en uitfietsen, rustige dagen tussen intensieve blokken.</div>
          <div class="card"><strong>Let op</strong><br/>Alleen Z1 trainen geeft weinig prestatieprikkel. Ondersteunend, niet compleet.</div>
        </div>
      </div>

      <div class="zone-panel" id="zone-z2" role="tabpanel">
        <div class="zone-grid">
          <div class="card"><strong>Herkenning</strong><br/>Rustig tot steady. Praten kan nog, maar je voelt dat je werkt.</div>
          <div class="card"><strong>Wat train je</strong><br/>Aerobe capaciteit, efficiency en vet-koolhydraat mix.</div>
          <div class="card"><strong>Helpt bij</strong><br/>Uithoudingsvermogen, basis voor intensiever werk, betere pacing.</div>
          <div class="card"><strong>Belangrijk</strong><br/>De naam Z2 verschilt per model. VT1 is het anker om deze zone goed te kalibreren.</div>
        </div>
      </div>

      <div class="zone-panel" id="zone-z3" role="tabpanel">
        <div class="zone-grid">
          <div class="card"><strong>Herkenning</strong><br/>Stevig. Korte zinnen praten lukt net. Comfortabel zwaar.</div>
          <div class="card"><strong>Wat train je</strong><br/>Tempo-uithoudingsvermogen, wedstrijdspecifiek tempo, mentale tolerantie.</div>
          <div class="card"><strong>Helpt bij</strong><br/>Gran fondo, lange solo's, langere beklimmingen, dieselvermogen.</div>
          <div class="card"><strong>Valkuil</strong><br/>Z3 wordt snel de standaard. Te veel Z3 beperkt veel Z2 en kwaliteit in Z4-Z5.</div>
        </div>
      </div>

      <div class="zone-panel" id="zone-z4" role="tabpanel">
        <div class="zone-grid">
          <div class="card"><strong>Herkenning</strong><br/>Hard. Praten lukt nauwelijks. Ademdruk hoog. Rond VT2.</div>
          <div class="card"><strong>Wat train je</strong><br/>Drempelvermogen, tolerantie voor hoge ventilatie, pacing rond wedstrijdintensiteit.</div>
          <div class="card"><strong>Helpt bij</strong><br/>Inspanningen van 20-60 min, tijdritten, lange klimmen, breakaways.</div>
          <div class="card"><strong>Praktisch</strong><br/>Bij korte blokken kan HR achterlopen. Watt en ademrespons zijn vaak betrouwbaarder.</div>
        </div>
      </div>

      <div class="zone-panel" id="zone-z5" role="tabpanel">
        <div class="zone-grid">
          <div class="card"><strong>Herkenning</strong><br/>Zeer hard. Praten kan niet. Korte, scherpe blokken. Ventilatie max.</div>
          <div class="card"><strong>Wat train je</strong><br/>VO2max prikkel, hoog vermogen herhalen onder vermoeidheid, top-end.</div>
          <div class="card"><strong>Helpt bij</strong><br/>Klimvermogen op 3-8 min, sneller herstel tussen harde inspanningen, racesituaties.</div>
          <div class="card"><strong>Belangrijk</strong><br/>Z5 vraagt veel herstel en werkt het best ingebed in veel Z1-Z2.</div>
        </div>
      </div>
    </section>

    <section id="praktijk" data-title="Praktijk">
      <h2>Van zone-model naar training in de praktijk</h2>
      <p>Zone-modellen zijn hulpmiddelen. De echte waarde zit in het fysiologische anker (VT1 en VT2) en hoe je dit vertaalt naar bruikbare trainingsintensiteiten.</p>
      <div class="grid-3">
        <div class="card">
          <h3>Zonder meting</h3>
          <p>Zones vervallen snel in standaardpercentages of gevoel. Dat vergroot ruis.</p>
        </div>
        <div class="card">
          <h3>Best practice</h3>
          <p>3-zone denken voor fysiologie, 5-zone gebruiken voor coachingdetail.</p>
        </div>
        <div class="card">
          <h3>Context</h3>
          <p>Koppel zones aan watt. Gebruik HR en RPE als context voor drift en HR-lag.</p>
        </div>
      </div>
      <div class="callout">Eindboodschap: zones werken pas echt als ze gemeten, gekalibreerd en consequent toegepast worden.</div>
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

    const zoneButtons = Array.from(document.querySelectorAll(".zone-btn"));
    const zonePanels = {
      z1: document.getElementById("zone-z1"),
      z2: document.getElementById("zone-z2"),
      z3: document.getElementById("zone-z3"),
      z4: document.getElementById("zone-z4"),
      z5: document.getElementById("zone-z5")
    };

    zoneButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const target = button.dataset.zone;
        zoneButtons.forEach((btn) => btn.classList.toggle("active", btn === button));
        Object.entries(zonePanels).forEach(([key, panel]) => {
          panel.classList.toggle("active", key === target);
        });
      });
    });
  </script>
</body>
</html>
"""

HTML_PAGE = HTML_PAGE.replace("{{LOGO_DATA_URI}}", logo_data_uri)

components.html(HTML_PAGE, height=4200, scrolling=True)

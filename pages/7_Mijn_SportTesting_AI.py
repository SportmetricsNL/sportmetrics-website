import importlib.util
import sys
from pathlib import Path

import docx
import google.generativeai as genai
import pypdf
import streamlit as st

# Pagina instellingen
st.set_page_config(page_title="Sportfysioloog AI", page_icon="🚴")

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
top_nav(active="Mijn SportTesting AI")

st.markdown(
    """
    <style>
      .ai-header {
        margin-top: 0.2rem;
        margin-bottom: 0.9rem;
      }

      .ai-title {
        margin: 0;
        color: #1d4d58;
        font-size: clamp(1.7rem, 3.6vw, 2.3rem);
      }

      .ai-subtitle {
        margin: 0.25rem 0 0;
        color: #416a73;
      }

      div[data-testid="stExpander"] {
        border: 1px solid #d6e1e4;
        border-radius: 0.9rem;
        background: #ffffff;
      }

      div[data-testid="stFileUploader"] {
        margin-top: 0.35rem;
      }

      div[data-testid="stFileUploaderDropzone"] {
        border: 1px dashed #b7ccd1;
        background: #f6fbfc;
      }

      div[data-testid="stFileUploaderDropzoneInstructions"] > div {
        display: none;
      }

      div[data-testid="stFileUploaderDropzone"] small,
      div[data-testid="stFileUploaderDropzone"] p {
        display: none;
      }

      div[data-testid="stFileUploaderDropzoneInstructions"]::before {
        content: "Sleep je PDF hier of klik op bladeren";
        color: #2f5f69;
        font-weight: 600;
        font-size: 0.92rem;
      }

      .ai-footer {
        margin-top: 1.6rem;
        text-align: center;
        color: #4a6c74;
        font-weight: 600;
      }
    </style>
    <div class="ai-header">
      <h1 class="ai-title">Jouw Wieler- en Hardloopexpert</h1>
      <p class="ai-subtitle">Stel vragen, upload je rapport en ontvang praktische uitleg op basis van trainingsleer. Ik weet ook heel veel van krachttraining en hardlopen!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

api_ready = False
model = None

# --- 1. CONFIGURATIE & API ---
try:
    if "GEMINI_API_KEY" in st.secrets and st.secrets["GEMINI_API_KEY"].strip():
        api_key = st.secrets["GEMINI_API_KEY"].strip()
        genai.configure(api_key=api_key)
        api_ready = True
    else:
        st.warning("API-key ontbreekt. Voeg GEMINI_API_KEY toe in secrets.toml om de AI-chat te activeren.")
except Exception as e:
    st.error(f"Fout bij API-configuratie: {e}")


# --- 2. KENNIS LADEN (PDF & DOCX) ---
@st.cache_resource
def load_all_knowledge() -> str:
    """Leest relevante PDF- en DOCX-bronnen uit meerdere mappen."""
    search_roots = [
        Path("."),
        Path("content/ai"),
        Path("pages/Mijnsportestingai"),
        Path("assets"),
    ]
    seen: set[Path] = set()
    files: list[Path] = []
    for root in search_roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.suffix.lower() in {".pdf", ".docx"} and path.is_file():
                resolved = path.resolve()
                if resolved not in seen:
                    seen.add(resolved)
                    files.append(path)

    combined_text = ""
    for filepath in files:
        try:
            if filepath.suffix.lower() == ".pdf":
                reader = pypdf.PdfReader(str(filepath))
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        combined_text += text + "\n"
            elif filepath.suffix.lower() == ".docx":
                doc = docx.Document(str(filepath))
                for para in doc.paragraphs:
                    combined_text += para.text + "\n"
        except Exception as e:
            print(f"Kon bestand {filepath} niet lezen: {e}")
    return combined_text


knowledge_base = load_all_knowledge()

# --- 3. DE AI INSTRUCTIES ---
SYSTEM_PROMPT = f"""
ROL: Je bent een expert sportfysioloog van SportMetrics.

BRONMATERIAAL:
Je hebt toegang tot specifieke literatuur over trainingsleer (zie hieronder).
Gebruik DEZE INFORMATIE als de absolute waarheid.

=== START LITERATUUR ===
{knowledge_base}
=== EINDE LITERATUUR ===

BELANGRIJKE REGELS:
1. SportMetrics doet GEEN lactaatmetingen (prikken), alleen ademgasanalyse.
2. Gebruik de principes (zoals Seiler zones) zoals beschreven in de geuploade literatuur.
3. Wees praktisch, enthousiast en gebruik bulletpoints.
4. Geen medisch advies.
5. Geef altijd een props aan de persoon voor de test en bedank dat hij of zij dat bij SportMetrics heeft gedaan.
"""

if api_ready:
    try:
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=SYSTEM_PROMPT,
        )
    except Exception as e:
        st.error(f"Modelfout: {e}")

# --- 4. CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    intro = (
        "Hoi! Ik geef antwoord op basis van mijn AI-kennis en de best beschikbare literatuur over trainingsleer."
        "\n\nUpload je testresultaten of stel direct een vraag!"
    )
    st.session_state.messages.append({"role": "assistant", "content": intro})

with st.expander("Klik hier om je PDF-rapport te uploaden", expanded=False):
    st.caption("Na upload wordt de inhoud automatisch meegenomen in je eerstvolgende vraag.")
    uploaded_file = st.file_uploader(
        "Upload je testresultaat (PDF)",
        type="pdf",
        key="mobile_uploader",
        label_visibility="visible",
    )

    if uploaded_file is not None:
        try:
            reader = pypdf.PdfReader(uploaded_file)
            client_pdf_text = ""
            for page in reader.pages:
                extracted = page.extract_text() or ""
                client_pdf_text += extracted + "\n"

            st.session_state["last_uploaded_text"] = client_pdf_text
            st.success("Rapport ontvangen. Typ hieronder je vraag.")
        except Exception as e:
            st.error(f"Fout bij lezen rapport: {e}")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input(
    "Stel je vraag of zeg 'Maak mijn zones'...",
    disabled=(not api_ready or model is None),
)

if prompt:
    extra_context = ""
    if "last_uploaded_text" in st.session_state:
        extra_context = (
            "\n\nHIER IS HET RAPPORT VAN DE KLANT:\n"
            f"{st.session_state['last_uploaded_text']}\n\n"
        )
        del st.session_state["last_uploaded_text"]

    full_prompt_for_ai = prompt + extra_context

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            loading_placeholder = st.empty()
            loading_placeholder.markdown(
                """
                <div style="width: 100%; overflow: hidden; padding: 10px 0;">
                    <div style="display: inline-block; white-space: nowrap; animation: moveRight 3s linear infinite;">
                        🚴 💨 🚴 💨 🚴
                    </div>
                </div>
                <style>
                    @keyframes moveRight {
                        0% { transform: translateX(-20%); }
                        100% { transform: translateX(120%); }
                    }
                </style>
                """,
                unsafe_allow_html=True,
            )

            response = model.generate_content(full_prompt_for_ai)
            loading_placeholder.empty()

            final_text = response.text + "\n\n---\n*Disclaimer: Dit is geen medisch advies.*"
            st.markdown(final_text)
            st.session_state.messages.append({"role": "assistant", "content": final_text})

    except Exception as e:
        st.error(f"De AI reageert niet of er is een fout opgetreden: {e}")

st.markdown('<p class="ai-footer">We zien je snel bij SportMetrics.</p>', unsafe_allow_html=True)

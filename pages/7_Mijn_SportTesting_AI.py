import os
import re
import sys
import importlib.util
from pathlib import Path

import streamlit as st
import pypdf
import docx
import google.generativeai as genai

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
        margin-top: 0.4rem;
        padding: 0.75rem;
        border: 1px solid #d6e1e4;
        border-radius: 0.9rem;
        background: #ffffff;
      }

      div[data-testid="stFileUploaderDropzone"] {
        border: 1px dashed #b7ccd1;
        background: #f6fbfc;
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
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        try:
            api_key = st.secrets.get("GEMINI_API_KEY")
        except Exception:
            api_key = None

    if not api_key or not str(api_key).strip():
        st.warning("Geen API key gevonden. Zet GEMINI_API_KEY in Railway Variables (prod) of in .streamlit/secrets.toml (lokaal).")
    else:
        genai.configure(api_key=str(api_key).strip())
        api_ready = True

except Exception as e:
    st.error(f"Fout bij API-configuratie: {e}")


# --- 2. KENNIS LADEN (PDF & DOCX) ---
def _read_document(filepath: Path) -> str:
    text_chunks: list[str] = []
    if filepath.suffix.lower() == ".pdf":
        reader = pypdf.PdfReader(str(filepath))
        for page in reader.pages:
            text = page.extract_text()
            if text:
                text_chunks.append(text)
    elif filepath.suffix.lower() == ".docx":
        doc = docx.Document(str(filepath))
        for para in doc.paragraphs:
            if para.text:
                text_chunks.append(para.text)
    return "\n".join(text_chunks).strip()


def _is_additional_source(filepath: Path) -> bool:
    name = filepath.name.lower()
    return (
        "leerboeknotities" in name
        and "transcript" in name
        and "krachttraining" in name
        and "duursporters" in name
    )


@st.cache_resource
def load_all_knowledge() -> tuple[str, str]:
    """Leest primaire en aanvullende literatuur zonder dubbele bestandsnamen."""
    search_roots = [
        Path("content/ai"),
        Path("assets"),
        Path("pages/Mijnsportestingai"),
    ]
    excluded_filenames = {"websitevoorbeeld.pdf"}

    chosen_by_name: dict[str, Path] = {}
    for root in search_roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in {".pdf", ".docx"}:
                continue
            normalized_name = path.name.lower().strip()
            if normalized_name in excluded_filenames:
                continue
            # Eerste match wint op basis van map-prioriteit in search_roots.
            if normalized_name not in chosen_by_name:
                chosen_by_name[normalized_name] = path

    primary_blocks: list[str] = []
    additional_blocks: list[str] = []

    for normalized_name in sorted(chosen_by_name.keys()):
        filepath = chosen_by_name[normalized_name]
        try:
            text = _read_document(filepath)
        except Exception as e:
            print(f"Kon bestand {filepath} niet lezen: {e}")
            continue

        if not text:
            continue

        block = f"[BRON: {filepath.name}]\n{text}"
        if _is_additional_source(filepath):
            additional_blocks.append(block)
        else:
            primary_blocks.append(block)

    return "\n\n".join(primary_blocks), "\n\n".join(additional_blocks)


primary_knowledge_base, additional_knowledge_base = load_all_knowledge()

# --- 3. DE AI INSTRUCTIES ---
SYSTEM_PROMPT = f"""
ROL: Je bent een expert sportfysioloog van SportMetrics.

BRONMATERIAAL:
Je hebt toegang tot specifieke literatuur over trainingsleer (zie hieronder).
Werk altijd op basis van deze literatuur.

VOLGORDE VAN BELANG:
1. Primaire trainingsliteratuur is leidend.
2. Aanvullende leerboeknotities op basis van transcripten zijn ondersteunend.
3. Als primaire en aanvullende literatuur verschillen, volg je de primaire literatuur.

=== START PRIMAIRE LITERATUUR ===
{primary_knowledge_base}
=== EINDE PRIMAIRE LITERATUUR ===

=== START AANVULLENDE LITERATUUR (ONDERSTEUNEND) ===
{additional_knowledge_base}
=== EINDE AANVULLENDE LITERATUUR ===

BELANGRIJKE REGELS:
1. SportMetrics doet GEEN lactaatmetingen (prikken), alleen ademgasanalyse.
2. Gebruik de principes (zoals Seiler zones) zoals beschreven in de geuploade literatuur.
3. Wees praktisch, enthousiast en gebruik bulletpoints.
4. Geen medisch advies.
5. Geef altijd een props aan de persoon voor de test en bedank dat hij of zij dat bij SportMetrics heeft gedaan.
6. Noem NOOIT expliciet de bronnaam "Reader trainingsleer 2024-2025" (of varianten daarop). Gebruik wel de inhoud, maar verwijs alleen algemeen naar trainingsliteratuur.
7. Noem CP en W' alleen als de hulpvraag expliciet gaat over sprinten, klimmen of korte piekinspanningen.
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

st.caption("Upload je PDF-rapport. Na upload wordt de inhoud automatisch meegenomen in je eerstvolgende vraag.")
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


def sanitize_response(text: str) -> str:
    replacements = [
        (r"reader\s*trainingsleer\s*2024[-–/]?2025(?:-compressed)?", "de beschikbare trainingsliteratuur"),
        (r"trainingsleer\s*reader", "de beschikbare trainingsliteratuur"),
    ]
    cleaned = text
    for pattern, repl in replacements:
        cleaned = re.sub(pattern, repl, cleaned, flags=re.IGNORECASE)
    return cleaned


def avatar_for(role: str) -> str:
    return "🤖" if role == "assistant" else "🙂"


def question_mentions_cp_context(question: str) -> bool:
    q = question.lower()
    keywords = (
        "sprint",
        "sprints",
        "sprinten",
        "klim",
        "klimmen",
        "klimmet",
        "heuvel",
        "heuvels",
        "piekinspanning",
        "piekinspanningen",
        "anaeroob",
        "explosief",
    )
    return any(keyword in q for keyword in keywords)


for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=avatar_for(message["role"])):
        st.markdown(message["content"])

prompt = st.chat_input(
    "Stel je vraag of zeg 'Maak mijn zones'...",
    disabled=(model is None),
)

if prompt:
    if model is None:
        st.error("AI-model niet beschikbaar. Controleer je API key (GEMINI_API_KEY).")
        st.stop()

    extra_context = ""
    if "last_uploaded_text" in st.session_state:
        extra_context = (
            "\n\nHIER IS HET RAPPORT VAN DE KLANT:\n"
            f"{st.session_state['last_uploaded_text']}\n\n"
        )
        del st.session_state["last_uploaded_text"]

    if question_mentions_cp_context(prompt):
        cp_instruction = (
            "Gebruik CP en W' alleen als dit direct helpt bij sprinten, klimmen of korte piekinspanningen."
        )
    else:
        cp_instruction = (
            "Noem CP en W' niet in je antwoord, tenzij de vraag expliciet over sprinten, klimmen of korte piekinspanningen gaat."
        )

    full_prompt_for_ai = f"{cp_instruction}\n\nVraag van de sporter:\n{prompt}{extra_context}"

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=avatar_for("user")):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant", avatar=avatar_for("assistant")):
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

            model_text = sanitize_response(response.text or "")
            final_text = model_text + "\n\n---\n*Disclaimer: Dit is geen medisch advies.*"
            st.markdown(final_text)
            st.session_state.messages.append({"role": "assistant", "content": final_text})

    except Exception as e:
        st.error(f"De AI reageert niet of er is een fout opgetreden: {e}")

st.markdown('<p class="ai-footer">We zien je snel bij SportMetrics.</p>', unsafe_allow_html=True)

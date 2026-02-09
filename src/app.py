from __future__ import annotations

from typing import Dict, Optional

import streamlit as st

from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card
from utils.Config import Config

# Constantes de interface e validação
APP_TITLE = "Upload de Arquivos DIO - Desafio 1 - Azure - Fake Docs"
APP_SUBTITLE = "Envie a imagem do cartão para validação automática."
ALLOWED_TYPES = ("png", "jpg", "jpeg")
MAX_FILE_MB = 8

# Campos esperados no retorno do modelo
FIELDS = (
    ("card_name", "Nome do Titular"),
    ("card_number", "Número do Cartão"),
    ("bank_name", "Banco Emissor"),
    ("expiry_date", "Data de Validade"),
)


def configure_page() -> None:
    """Configura a página do Streamlit (título e layout)."""
    st.set_page_config(page_title=APP_TITLE, layout="wide")


def inject_css() -> None:
    """Injeta estilos CSS customizados na página."""
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Source+Code+Pro:wght@400;600&display=swap');

            :root {
                --bg-primary: #0b1220;
                --bg-secondary: #0f172a;
                --bg-accent: #0b3a53;
                --card-bg: rgba(255, 255, 255, 0.06);
                --card-border: rgba(148, 163, 184, 0.25);
                --text-primary: #e2e8f0;
                --text-muted: rgba(226, 232, 240, 0.7);
                --accent: #22c55e;
                --accent-2: #38bdf8;
            }

            html, body, [class*="css"] {
                font-family: "Space Grotesk", sans-serif;
            }

            .stApp {
                color: var(--text-primary);
                background: radial-gradient(1200px 600px at 15% 0%, var(--bg-accent), var(--bg-secondary) 50%, var(--bg-primary) 100%);
            }

            section[data-testid="stSidebar"] {
                background: var(--bg-primary);
                border-right: 1px solid rgba(148, 163, 184, 0.15);
            }

            .block-container {
                padding-top: 2rem;
            }

            .hero {
                padding: 1.5rem 1.75rem;
                background: linear-gradient(120deg, rgba(56, 189, 248, 0.18), rgba(34, 197, 94, 0.18));
                border: 1px solid var(--card-border);
                border-radius: 18px;
                margin-bottom: 1.5rem;
                box-shadow: 0 20px 60px rgba(2, 6, 23, 0.35);
            }

            .hero .eyebrow {
                text-transform: uppercase;
                letter-spacing: 0.2em;
                font-size: 0.7rem;
                color: var(--text-muted);
                margin-bottom: 0.4rem;
            }

            .hero h1 {
                font-size: 2.1rem;
                margin-bottom: 0.35rem;
            }

            .hero p {
                margin: 0;
                color: var(--text-muted);
                font-size: 1rem;
            }

            .stButton > button,
            .stDownloadButton > button {
                background: linear-gradient(120deg, #16a34a, #0ea5e9);
                color: #041016;
                border: none;
                border-radius: 999px;
                font-weight: 600;
            }

            .stFileUploader button {
                background: #0b1220;
                color: #e2e8f0;
                border: 1px solid rgba(148, 163, 184, 0.6);
                box-shadow: none;
            }

            .stFileUploader button:hover {
                background: #0f172a;
                color: #f8fafc;
                border-color: rgba(148, 163, 184, 0.9);
            }

            .stFileUploader {
                background: rgba(15, 23, 42, 0.6);
                border: 1px dashed rgba(148, 163, 184, 0.4);
                border-radius: 14px;
                padding: 0.5rem;
            }

            .stAlert {
                border-radius: 14px;
            }

            .stProgress > div > div > div {
                background-color: var(--accent);
            }

            code, pre, .stCodeBlock {
                font-family: "Source Code Pro", monospace;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    """Renderiza o cabeçalho principal do app."""
    st.markdown(
        f"""
        <div class="hero">
            <div class="eyebrow">Validação inteligente</div>
            <h1>{APP_TITLE}</h1>
            <p>{APP_SUBTITLE}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    """Renderiza a barra lateral com instruções e status."""
    with st.sidebar:
        st.header("Como funciona")
        st.write("1. Envie uma imagem do cartão.")
        st.write("2. O arquivo é enviado para o Azure Blob Storage.")
        st.write("3. O Azure Document Intelligence extrai os dados.")
        st.divider()
        st.write(f"Formatos aceitos: {', '.join(ALLOWED_TYPES).upper()}")
        st.write(f"Tamanho máximo: {MAX_FILE_MB} MB")
        st.caption("Dica: use uma foto nítida, sem reflexos e com boa iluminação.")

        missing = Config.missing_keys()
        if missing:
            st.error("Configuração incompleta: " + ", ".join(missing))
        else:
            st.success("Configuração carregada.")


def get_file_bytes(
    uploaded_file: st.runtime.uploaded_file_manager.UploadedFile,
) -> Optional[bytes]:
    """Valida e retorna os bytes do arquivo enviado."""
    data = uploaded_file.getvalue()
    if not data:
        st.error("Arquivo vazio. Envie uma imagem válida.")
        return None
    if len(data) > MAX_FILE_MB * 1024 * 1024:
        # Limite de tamanho em MB
        st.error(f"Arquivo maior que {MAX_FILE_MB} MB. Envie um arquivo menor.")
        return None
    return data


def format_field(value: Optional[str]) -> str:
    """Normaliza valores exibidos nos resultados."""
    if not value:
        return "-"
    return value.strip()


def is_card_info_valid(card_info: Optional[Dict[str, Optional[str]]]) -> bool:
    """Verifica se os campos mínimos do cartão estão presentes."""
    if not card_info:
        return False
    return bool(card_info.get("card_name") and card_info.get("card_number"))


def compute_completeness(card_info: Optional[Dict[str, Optional[str]]]) -> float:
    """Calcula a taxa de preenchimento dos campos."""
    if not card_info:
        return 0.0
    filled = sum(1 for key, _ in FIELDS if card_info.get(key))
    return filled / len(FIELDS)


def render_empty_state() -> None:
    """Exibe o estado vazio quando não há upload."""
    st.info("Envie uma imagem para iniciar a validação.")


def render_results(
    image_bytes: bytes,
    file_name: str,
    blob_url: str,
    card_info: Optional[Dict[str, Optional[str]]],
) -> None:
    """Exibe a imagem e o resultado da validação."""
    left, right = st.columns([1, 1], gap="large")

    with left:
        st.subheader("Pré-visualização")
        st.image(image_bytes, caption=file_name, use_container_width=True)
        st.caption(f"Arquivo: {file_name} · {len(image_bytes) / 1024:.1f} KB")

    with right:
        st.subheader("Resultado")
        if is_card_info_valid(card_info):
            st.success("Cartão válido")
        else:
            st.error("Cartão inválido")

        completion = compute_completeness(card_info)
        st.progress(completion, text=f"Campos preenchidos: {int(completion * 100)}%")

        for key, label in FIELDS:
            value = format_field(card_info.get(key) if card_info else None)
            st.markdown(f"**{label}:** {value}")

        with st.expander("Detalhes técnicos"):
            st.write("URL do Blob:")
            st.code(blob_url)
            st.write("Resposta completa:")
            st.json(card_info or {})


def main() -> None:
    """Orquestra o fluxo principal do app."""
    configure_page()
    inject_css()
    render_sidebar()
    render_header()

    # Valida se as variáveis de ambiente essenciais estão presentes
    missing = Config.missing_keys()
    if missing:
        st.error(
            "Configuração incompleta. Variáveis ausentes: " + ", ".join(missing) + "."
        )
        st.stop()

    # Upload de imagem
    st.subheader("Enviar imagem")
    uploaded_file = st.file_uploader(
        "Escolha um arquivo para upload",
        type=list(ALLOWED_TYPES),
        help="Envie uma imagem em PNG ou JPG.",
    )

    if uploaded_file is None:
        render_empty_state()
        return

    # Leitura e validação do arquivo
    file_bytes = get_file_bytes(uploaded_file)
    if not file_bytes:
        return

    # Envio para o Blob Storage
    with st.spinner("Enviando arquivo para o Azure Blob Storage..."):
        blob_url = upload_blob(
            file_bytes,
            uploaded_file.name,
            content_type=uploaded_file.type,
        )

    if not blob_url:
        st.error("Erro ao enviar o arquivo para o Azure Blob Storage.")
        return

    st.success("Upload concluído.")

    # Análise com Document Intelligence
    with st.spinner("Analisando documento..."):
        card_info = analyze_credit_card(blob_url)

    render_results(file_bytes, uploaded_file.name, blob_url, card_info)


if __name__ == "__main__":
    main()

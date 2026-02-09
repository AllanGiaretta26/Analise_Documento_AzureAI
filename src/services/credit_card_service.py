import logging
from typing import Any, Dict, Mapping, Optional

from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

from utils.Config import Config

logger = logging.getLogger(__name__)


def _get_field_content(
    fields: Optional[Mapping[str, Any]],
    name: str,
) -> Optional[str]:
    """Extrai o conteúdo de um campo retornado pelo modelo."""
    if not fields:
        return None
    field = fields.get(name)
    if field is None:
        return None
    if hasattr(field, "content"):
        # SDK costuma expor o valor em atributo
        return field.content
    if isinstance(field, dict):
        # Fallback para estrutura em dicionário
        return field.get("content")
    return None


def analyze_credit_card(card_url: str) -> Optional[Dict[str, Optional[str]]]:
    """Analisa uma imagem de cartão de crédito via URL e extrai campos-chave."""
    try:
        # Cria credencial e cliente do Document Intelligence
        credential = AzureKeyCredential(Config.SUBSCRIPTION_KEY)
        document_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

        # Executa a análise usando o modelo pré-construído
        poller = document_client.begin_analyze_document(
            "prebuilt-creditCard",
            AnalyzeDocumentRequest(url_source=card_url),
        )
        result = poller.result()

        if not result.documents:
            # Nenhum documento detectado
            return None

        # Usa o primeiro documento retornado
        document = result.documents[0]
        fields = getattr(document, "fields", None)

        # Mapeia os campos relevantes para a resposta
        return {
            "card_name": _get_field_content(fields, "CardHolderName"),
            "card_number": _get_field_content(fields, "CardNumber"),
            "expiry_date": _get_field_content(fields, "ExpirationDate"),
            "bank_name": _get_field_content(fields, "IssuingBank"),
        }
    except Exception:
        # Loga a falha e sinaliza erro para o chamador
        logger.exception("Falha ao analisar o cartão de crédito.")
        return None

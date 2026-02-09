import logging
from typing import Optional

from azure.storage.blob import BlobServiceClient, ContentSettings

from utils.Config import Config

logger = logging.getLogger(__name__)


def upload_blob(
    data: bytes,
    blob_name: str,
    content_type: Optional[str] = None,
) -> Optional[str]:
    """Faz upload de bytes no Azure Blob Storage e retorna a URL do blob."""
    # Não prossegue com dados vazios
    if not data:
        return None

    try:
        # Cria o cliente do serviço de blob a partir da conexão configurada
        blob_service_client = BlobServiceClient.from_connection_string(
            Config.AZURE_STORAGE_CONNECTION_STRING
        )
        # Obtém o cliente do blob no container definido
        blob_client = blob_service_client.get_blob_client(
            container=Config.CONTAINER_NAME,
            blob=blob_name,
        )

        # Define o content-type, quando informado
        settings = ContentSettings(content_type=content_type) if content_type else None
        # Envia o blob, substituindo se já existir
        blob_client.upload_blob(data, overwrite=True, content_settings=settings)
        return blob_client.url
    except Exception:
        # Loga o erro e sinaliza falha
        logger.exception("Erro ao enviar o arquivo para o Azure Blob Storage.")
        return None

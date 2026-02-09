import os
from typing import List

from dotenv import load_dotenv

# Carrega variáveis de ambiente de um arquivo .env local, se existir
load_dotenv()


class Config:
    # Configurações do Azure Document Intelligence
    ENDPOINT = os.getenv("ENDPOINT")
    SUBSCRIPTION_KEY = os.getenv("SUBSCRIPTION_KEY")

    # Configurações do Azure Blob Storage
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")

    @classmethod
    def missing_keys(cls) -> List[str]:
        """Retorna a lista de variáveis obrigatórias não configuradas."""
        required = [
            "ENDPOINT",
            "SUBSCRIPTION_KEY",
            "AZURE_STORAGE_CONNECTION_STRING",
            "CONTAINER_NAME",
        ]
        return [key for key in required if not getattr(cls, key)]

# Upload de Arquivos DIO - Azure Fake Docs

App em Streamlit para validar imagens de cartões de crédito usando Azure Document Intelligence e Azure Blob Storage. O fluxo é: o usuário envia a imagem, o arquivo é enviado ao Blob Storage e o Document Intelligence extrai os campos principais do cartão.

**Funcionalidades**
- Upload de imagens (`.png`, `.jpg`, `.jpeg`) com limite de 8 MB
- Envio do arquivo para o Azure Blob Storage
- Extração automática de dados do cartão com o modelo `prebuilt-creditCard`
- Exibição de status e detalhes técnicos no app

**Tecnologias**
- Python
- Streamlit
- Azure Blob Storage
- Azure Document Intelligence

**Pré-requisitos**
- Python 3.x
- Conta no Azure com:
- Azure Document Intelligence (endpoint + chave)
- Azure Storage (connection string + container)

**Configuração**
Crie um arquivo `.env` na raiz deste projeto (`c:\Users\giare\VSCodeProject\DOCS\src`) com as variáveis abaixo:

```env
ENDPOINT="https://<seu-endpoint>.cognitiveservices.azure.com/"
SUBSCRIPTION_KEY="<sua-chave>"
AZURE_STORAGE_CONNECTION_STRING="<sua-connection-string>"
CONTAINER_NAME="cartoes"
```

**Como executar**
1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Inicie o app:

```bash
streamlit run app.py
```

**Estrutura**
- `app.py`: UI e fluxo principal do Streamlit
- `services/blob_service.py`: upload para o Azure Blob Storage
- `services/credit_card_service.py`: análise no Document Intelligence
- `utils/Config.py`: leitura das variáveis de ambiente

**Explicação do código**
O fluxo principal fica em `app.py` e pode ser entendido em duas etapas ilustradas abaixo.

Etapa 1: upload e validação inicial do arquivo.
![Tela do app - upload](images/Captura%20de%20tela%202026-02-09%20081630.png)

Etapa 2: envio para o Blob Storage, análise no Document Intelligence e exibição dos resultados.
![Tela do app - resultado](images/Captura%20de%20tela%202026-02-09%20081745.png)

As integrações com Azure ficam em `services/blob_service.py` (upload) e `services/credit_card_service.py` (análise), enquanto a leitura das variáveis de ambiente está em `utils/Config.py`.

**Notas**
- Não versionar o arquivo `.env` com chaves reais.
- Use imagens nítidas e bem iluminadas para melhorar a extração dos campos.
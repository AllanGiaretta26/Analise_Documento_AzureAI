# Análise de Documento com Azure AI

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)
![Azure](https://img.shields.io/badge/Azure-Document%20Intelligence-0078D4.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> Validação automática de cartões de crédito com OCR e inteligência artificial da Microsoft Azure.

## Descrição

Aplicação web construída com **Streamlit** que integra serviços cognitivos da **Microsoft Azure** para extrair e validar dados de cartões de crédito a partir de imagens. O projeto demonstra, em uma arquitetura modular e enxuta, como combinar **Azure Document Intelligence** (modelo pré-treinado `prebuilt-creditCard`) com **Azure Blob Storage** para resolver um problema recorrente: validar e extrair dados de documentos de forma automática, sem depender de bibliotecas locais de OCR.

Ideal para portfólio, aprendizado de Azure Cognitive Services e prototipagem rápida de soluções *document-heavy*.

## Status do Projeto

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)

Projeto concluído e funcional. Aceita melhorias e novas integrações via *pull request*.

## Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| Upload validado | Aceita `.png`, `.jpg`, `.jpeg` com limite de 8 MB |
| Análise com IA | Extrai dados em segundos com modelo pré-treinado da Azure |
| Armazenamento em nuvem | Salva imagens automaticamente no Azure Blob Storage |
| Validação visual | Indica campos obrigatórios preenchidos e taxa de completude |
| Interface responsiva | Tema escuro com tipografia Space Grotesk e feedback em tempo real |
| Detalhes técnicos | Expande a URL do blob e a resposta JSON bruta da API |

## Tecnologias

| Tecnologia | Versão | Função |
|---|---|---|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | 3.8+ | Linguagem principal |
| ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white) | 1.28+ | Framework web |
| ![Azure](https://img.shields.io/badge/-Document%20Intelligence-0078D4?logo=microsoftazure&logoColor=white) | latest | OCR e extração de dados |
| ![Azure Blob](https://img.shields.io/badge/-Blob%20Storage-0078D4?logo=microsoftazure&logoColor=white) | latest | Armazenamento em nuvem |
| ![dotenv](https://img.shields.io/badge/-python--dotenv-ECD53F?logo=dotenv&logoColor=black) | latest | Variáveis de ambiente |

## Como Instalar e Rodar

### Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/)
- Conta ativa no [Azure](https://azure.microsoft.com/free/)
- Recurso **Azure Document Intelligence** provisionado
- Recurso **Azure Storage Account** provisionado

### Instalação

```bash
# Clone o repositório
git clone https://github.com/AllanGiaretta26/Analise_Documento_AzureAI.git
cd Analise_Documento_AzureAI

# (Opcional) crie e ative um ambiente virtual
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux / macOS

# Instale as dependências
pip install -r requirements.txt
```

### Execução

```bash
streamlit run src/app.py
```

A aplicação abrirá automaticamente em `http://localhost:8501`.

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as chaves abaixo:

```env
ENDPOINT=
SUBSCRIPTION_KEY=
AZURE_STORAGE_CONNECTION_STRING=
CONTAINER_NAME=
```

| Variável | Onde encontrar |
|---|---|
| `ENDPOINT` | Portal Azure → Document Intelligence → *Keys and Endpoint* |
| `SUBSCRIPTION_KEY` | Portal Azure → Document Intelligence → *Keys and Endpoint* |
| `AZURE_STORAGE_CONNECTION_STRING` | Portal Azure → Storage Account → *Access keys* → *Connection string* |
| `CONTAINER_NAME` | Nome do container criado no Storage Account (ex: `cartoes`) |

> O `.env` está no `.gitignore`. Nunca versione credenciais reais.

## Estrutura do Projeto

```
Analise_Documento_AzureAI/
├── src/
│   ├── app.py                       # Interface Streamlit e orquestração do pipeline
│   ├── services/
│   │   ├── blob_service.py          # Upload de imagens para Azure Blob Storage
│   │   └── credit_card_service.py   # Análise com Azure Document Intelligence
│   └── utils/
│       └── Config.py                # Carregamento e validação de variáveis de ambiente
├── images/                          # Screenshots da aplicação
├── requirements.txt                 # Dependências Python
└── README.md
```

## Campos Extraídos

O modelo `prebuilt-creditCard` retorna automaticamente:

| Campo | Exemplo | Obrigatório |
|---|---|---|
| `card_name` | `JOAO DA SILVA` | Sim |
| `card_number` | `1234 5678 9012 3456` | Sim |
| `bank_name` | `BANCO EXEMPLO S.A.` | Não |
| `expiry_date` | `12/28` | Não |

A validação considera o cartão **válido** quando `card_name` e `card_number` estão presentes.

## Fluxo da Aplicação

```
Upload da imagem
       ↓
Validação local (tipo e tamanho)
       ↓
Upload para Azure Blob Storage
       ↓
Análise com Document Intelligence
       ↓
Exibição dos campos extraídos no Streamlit
```

## Screenshots

**Etapa 1 — Upload da imagem**

![Upload](images/Captura%20de%20tela%202026-02-09%20081630.png)

**Etapa 2 — Resultado da análise**

![Resultados](images/Captura%20de%20tela%202026-02-09%20081745.png)

## Como Contribuir

1. Faça um *fork* do repositório
2. Crie uma branch para sua feature: `git checkout -b feature/minha-feature`
3. Faça commit das alterações: `git commit -m "feat: adiciona minha feature"`
4. Envie para o seu fork: `git push origin feature/minha-feature`
5. Abra um *pull request*

## Licença

Distribuído sob a licença **MIT**. Veja [LICENSE](LICENSE) para detalhes.

---

Desenvolvido por [Allan Giaretta](https://github.com/AllanGiaretta26).

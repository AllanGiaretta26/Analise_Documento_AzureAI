# 📄 Azure Fake Docs — Validação de Cartões com Document Intelligence

> App Streamlit que utiliza **Azure Document Intelligence** e **Azure Blob Storage** para validar e extrair dados de cartões de crédito a partir de imagens.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)
![Azure](https://img.shields.io/badge/Azure-Document%20Intelligence-0078D4.svg)

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Como Executar](#-como-executar)
- [Fluxo da Aplicação](#-fluxo-da-aplicação)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Campos Extraídos](#-campos-extraídos)
- [Boas Práticas](#-boas-práticas)
- [Screenshots](#-screenshots)
- [Autor](#-autor)

---

## 🎯 Sobre o Projeto

O **Azure Fake Docs** é uma aplicação web construída com Streamlit que demonstra a integração com serviços cognitivos da Azure para extração automática de dados de cartões de crédito. O usuário envia uma imagem do cartão e o sistema realiza:

1. **Upload** para o Azure Blob Storage
2. **Análise** com o modelo pré-construído `prebuilt-creditCard` do Document Intelligence
3. **Exibição** dos campos extraídos com indicadores de validação

Este projeto é ideal para desenvolvedores que desejam aprender a integrar serviços cognitivos da Azure em aplicações Python.

---

## ✨ Funcionalidades

- ✅ Upload de imagens (`.png`, `.jpg`, `.jpeg`) com limite de **8 MB**
- ☁️ Upload automático para o **Azure Blob Storage**
- 🧠 Extração inteligente com o modelo **`prebuilt-creditCard`** do Document Intelligence
- 📊 Exibição de progresso e taxa de preenchimento dos campos
- 🎨 Interface moderna com tema escuro e design responsivo
- 🔍 Validação automática dos campos essenciais (nome e número do cartão)
- 📋 Detalhes técnicos expansíveis, incluindo URL do blob e resposta JSON

---

## 🛠 Tecnologias Utilizadas

| Tecnologia | Descrição |
|------------|-----------|
| **Python 3.8+** | Linguagem principal |
| **Streamlit** | Framework para apps web interativos |
| **Azure Blob Storage** | Armazenamento de arquivos na nuvem |
| **Azure Document Intelligence** | Serviço de OCR e análise de documentos |
| **python-dotenv** | Gerenciamento de variáveis de ambiente |

---

## 📦 Pré-requisitos

Antes de começar, certifique-se de ter:

- [Python 3.8+](https://www.python.org/downloads/) instalado
- Uma conta **Azure** ativa ([crie gratuitamente aqui](https://azure.microsoft.com/free/))
- Recurso **Azure Document Intelligence** criado no portal Azure
- Recurso **Azure Storage Account** criado no portal Azure

---

## 🔧 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/azure-fake-docs.git
cd azure-fake-docs
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
# Azure Document Intelligence
ENDPOINT="https://<seu-endpoint>.cognitiveservices.azure.com/"
SUBSCRIPTION_KEY="<sua-chave-de-assinatura>"

# Azure Blob Storage
AZURE_STORAGE_CONNECTION_STRING="<sua-connection-string>"
CONTAINER_NAME="cartoes"
```

> **⚠️ Importante:** Nunca versione o arquivo `.env` com credenciais reais. Ele já está listado no `.gitignore`.

### 📍 Como obter as credenciais no Portal Azure

1. **Document Intelligence**: Acesse o recurso > **Keys and Endpoint** > copie o endpoint e uma das chaves
2. **Storage Account**: Acesse o recurso > **Access keys** > copie a connection string

---

## 🚀 Como Executar

Após configurar o ambiente, inicie o app:

```bash
streamlit run src/app.py
```

A aplicação será aberta automaticamente no navegador em `http://localhost:8501`.

---

## 📁 Estrutura do Projeto

```
DOCS/
├── src/
│   ├── app.py                          # App principal (Streamlit UI)
│   ├── services/
│   │   ├── blob_service.py             # Serviço de upload para Blob Storage
│   │   └── credit_card_service.py      # Serviço de análise com Document Intelligence
│   └── utils/
│       └── Config.py                   # Gerenciamento de variáveis de ambiente
├── images/                             # Screenshots da aplicação
├── requirements.txt                    # Dependências Python
├── .gitignore                          # Arquivos ignorados pelo Git
└── README.md                           # Esta documentação
```

### Descrição dos módulos

| Arquivo | Responsabilidade |
|---------|------------------|
| `app.py` | Interface do usuário, validação de arquivos e orquestração do fluxo |
| `services/blob_service.py` | Conexão e upload para o Azure Blob Storage |
| `services/credit_card_service.py` | Chamada ao Document Intelligence e extração de campos |
| `utils/Config.py` | Leitura e validação de variáveis de ambiente |

---

## 💳 Campos Extraídos

O modelo `prebuilt-creditCard` extrai os seguintes campos:

| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| **card_name** | Nome do titular do cartão | `JOAO DA SILVA` |
| **card_number** | Número do cartão | `1234 5678 9012 3456` |
| **bank_name** | Banco/Instituição emissora | `BANCO EXEMPLO S.A.` |
| **expiry_date** | Data de validade | `12/28` |

> A validação do cartão considera os campos `card_name` e `card_number` como essenciais.

---

## 📸 Screenshots

### Etapa 1: Upload e validação inicial
![Tela do app - upload](images/Captura%20de%20tela%202026-02-09%20081630.png)

### Etapa 2: Resultados da análise
![Tela do app - resultado](images/Captura%20de%20tela%202026-02-09%20081745.png)

---

## 🛡️ Boas Práticas

- 🔒 **Segurança**: Nunca compartilhe ou versione arquivos com credenciais
- 📷 **Qualidade da imagem**: Use fotos nítidas, bem iluminadas e sem reflexos
- 📏 **Tamanho do arquivo**: Mantenha as imagens abaixo de 8 MB para melhor performance
- 🧪 **Testes**: Verifique as variáveis de ambiente com o indicator na sidebar antes de usar

---

## 🧑‍💻 Autor
Desenvolvido por Allan Giaretta

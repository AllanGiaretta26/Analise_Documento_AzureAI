# 📄 Análise de Documento com Azure AI

> Validação automática de cartões de crédito com OCR e inteligência artificial.

![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)
![Azure](https://img.shields.io/badge/Azure-Document%20Intelligence-0078D4.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📋 Sumário

- [Descrição](#-descrição)
- [O que este projeto resolve](#-o-que-este-projeto-resolve)
- [Principais funcionalidades](#-principais-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Como começar](#-como-começar)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
  - [Configuração](#configuração)
  - [Executar](#executar)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Campos de dados extraídos](#-campos-de-dados-extraídos)
- [Fluxo de funcionamento](#-fluxo-de-funcionamento)
- [Guia de uso](#-guia-de-uso)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

---

## 📖 Descrição

O **Análise de Documento com Azure AI** é uma aplicação web moderna construída com **Streamlit** que integra serviços cognitivos da **Microsoft Azure** para extrair e validar dados de cartões de crédito através de análise de imagens.

A aplicação demonstra como usar:
- **Azure Document Intelligence** — Modelo pré-treinado `prebuilt-creditCard` para OCR e extração de dados estruturados
- **Azure Blob Storage** — Armazenamento seguro de imagens na nuvem
- **Python + Streamlit** — Interface web interativa e responsiva

---

## 🎯 O que este projeto resolve

Empresas e desenvolvedores frequentemente precisam validar e extrair dados de documentos (cartões, RG, comprovantes) de forma automática. Este projeto demonstra:

✅ **Integração prática** com Azure Cognitive Services  
✅ **Processamento de imagens** sem dependências locais complexas  
✅ **Validação em tempo real** com feedback visual  
✅ **Arquitetura modular** fácil de estender

Ideal para **portfólio**, **aprendizado** ou **prototipagem rápida** de soluções document-heavy.

---

## ✨ Principais funcionalidades

| Funcionalidade | Descrição |
|---|---|
| **Upload seguro** | Aceita `.png`, `.jpg`, `.jpeg` com limite de 8 MB |
| **Análise instantânea** | Extrai dados em segundos com modelo pré-treinado |
| **Armazenamento em nuvem** | Salva imagens automaticamente no Azure Blob Storage |
| **Validação inteligente** | Identifica campos preenchidos e essenciais automaticamente |
| **Interface responsiva** | Design moderno com tema escuro e feedback visual |
| **Detalhes técnicos** | Expande informações como URL do blob e resposta JSON bruta |

---

## 🛠 Tecnologias

| Tecnologia | Versão | Função |
|---|---|---|
| **Python** | 3.8+ | Linguagem principal |
| **Streamlit** | 1.28+ | Framework web |
| **Azure Document Intelligence** | Latest | OCR e extração de dados |
| **Azure Storage Blob** | Latest | Armazenamento em nuvem |
| **python-dotenv** | Latest | Gerenciar variáveis de ambiente |

---

## 🚀 Como começar

### Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/)
- Conta ativa no [Azure](https://azure.microsoft.com/free/) (gratuita)
- Recurso **Azure Document Intelligence** criado
- Recurso **Azure Storage Account** criado

### Instalação

1. **Clone o repositório**

```bash
git clone https://github.com/AllanGiaretta26/Analise_Documento_AzureAI.git
cd Analise_Documento_AzureAI
```

2. **Instale as dependências**

```bash
pip install -r requirements.txt
```

### Configuração

1. **Crie um arquivo `.env`** na raiz do projeto:

```env
# Azure Document Intelligence
ENDPOINT="https://<seu-recurso>.cognitiveservices.azure.com/"
SUBSCRIPTION_KEY="<sua-chave-primária>"

# Azure Storage Account
AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=<seu-account>;..."
CONTAINER_NAME="cartoes"
```

2. **Obtenha as credenciais**:

| Serviço | Onde encontrar |
|---|---|
| Document Intelligence | Portal Azure > Seu recurso > Keys and Endpoint |
| Storage Account | Portal Azure > Seu recurso > Access keys > Connection string |

> ⚠️ **Importante**: O `.env` está no `.gitignore`. Nunca versione credenciais reais.

### Executar

```bash
streamlit run src/app.py
```

A aplicação abrirá automaticamente em `http://localhost:8501`.

---

## 📁 Estrutura do projeto

```
Analise_Documento_AzureAI/
├── src/
│   ├── app.py                          # Aplicação Streamlit (UI + orquestração)
│   ├── services/
│   │   ├── blob_service.py             # Upload para Azure Blob Storage
│   │   └── credit_card_service.py      # Análise com Document Intelligence
│   └── utils/
│       └── Config.py                   # Carregamento de variáveis de ambiente
├── images/                             # Screenshots
├── requirements.txt                    # Dependências Python
├── .gitignore                          # Arquivo padrão
└── README.md                           # Esta documentação
```

### Responsabilidades dos módulos

| Módulo | O que faz |
|---|---|
| **app.py** | Interface do usuário, validação de arquivo, orquestração do pipeline |
| **blob_service.py** | Conexão e upload de imagens para Azure Blob Storage |
| **credit_card_service.py** | Chamada ao Document Intelligence, parsing de resposta |
| **Config.py** | Leitura segura de variáveis de ambiente com validação |

---

## 💳 Campos de dados extraídos

O modelo pré-treinado `prebuilt-creditCard` extrai automaticamente:

| Campo | Exemplo | Status |
|---|---|---|
| **card_name** | `JOAO DA SILVA` | Obrigatório ✓ |
| **card_number** | `1234 5678 9012 3456` | Obrigatório ✓ |
| **bank_name** | `BANCO EXEMPLO S.A.` | Opcional |
| **expiry_date** | `12/28` | Opcional |

---

## 🔄 Fluxo de funcionamento

```
Usuário upload imagem
        ↓
Validação local (tipo, tamanho)
        ↓
Upload para Azure Blob Storage
        ↓
Análise com Document Intelligence
        ↓
Extração de campos estruturados
        ↓
Exibição e validação no Streamlit
```

1. Usuário seleciona e envia imagem do cartão
2. Sistema valida formato e tamanho localmente
3. Imagem é armazenada no Azure Blob Storage
4. Document Intelligence analisa e extrai campos
5. Campos são exibidos com indicadores visuais

---

## 📸 Guia de uso

### Etapa 1: Upload da imagem

![Upload](images/Captura%20de%20tela%202026-02-09%20081630.png)

- Selecione uma imagem clara do cartão de crédito
- Certifique-se que todos os dados visíveis estão bem nítidos
- Tamanho máximo: 8 MB

### Etapa 2: Resultados da análise

![Resultados](images/Captura%20de%20tela%202026-02-09%20081745.png)

- Campos são exibidos conforme extraídos
- Verde = campo validado
- Vermelho = campo ausente ou inválido
- Expanda "Detalhes técnicos" para ver resposta JSON bruta

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja [LICENSE](LICENSE) para detalhes.

---

Desenvolvido por Allan Giaretta.

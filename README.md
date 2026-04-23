# Automação em Python 

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Coverage](https://img.shields.io/badge/coverage-pytest--cov-informational)](https://pytest-cov.readthedocs.io/)


## Visão Geral
Repositório **completo** com **exemplos práticos de automação** usando Python: escritório, web, APIs, IA/ML, monitoramento e dashboards.



## Instalação 

```bash
git clone [repo-url]
cd automacao-em-py
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Configure suas chaves
```

## Estrutura 

```
automacao-em-python/
├── automacao_escritorio/     # Relatórios, emails, PDFs
├── automacao_tarefas/        # Web scraping, download
├── integracao_apis/          # Bots, posts sociais
├── ia_aplicada/              # ML/NLP (sentimentos, imagens)
├── monitoramento_alertas/    # Monitoramento sites
├── projetos_exemplo/         # Dashboards, pipelines
├── utils/                    # Funções auxiliares
├── tests/                    # Testes unitários
├── requirements.txt          # Dependências
├── .env                      # Template chaves

```


## Exemplos Rápidos (Copy-Paste)
Veja mais exemplos em [examples/](examples/)

### 1. **Renomear 100+ arquivos** (segundos)
```bash
python automacao_tarefas/renomear_arquivos.py ./pasta --padrao "relatorio_%Y%m%d_%03d"
```

### 2. **Web Scraping** (preços/notícias)
```bash
python automacao_tarefas/web_scraping.py --url "amazon.com" --seletor ".price"
```

### 3. **Bot Telegram** (automação)
```bash
python integracao_apis/telegram_bot.py
```

### 4. **Análise Sentimentos** (reviews)
```bash
python ia_aplicada/analise_sentimentos.py --texto "Amei o produto, entrega rápida!"
```

### 5. **Relatório Excel** (vendas)
```bash
python automacao_escritorio/gerar_relatorios.py dados.csv
```

### 6. **Dashboard Interativo**
```bash
streamlit run projetos_exemplo/dashboard_dados.py
```

### 7. **Monitor Site** (alertas)
```bash
python monitoramento_alertas/monitor_sites.py exemplo.com
```

## Configuração (.env)

```env
# Email
GMAIL_USER=seu_email@gmail.com
GMAIL_APP_PASSWORD=xxxx

# APIs
OPENAI_API_KEY=sk-...
TELEGRAM_BOT_TOKEN=xxx

# Banco
DB_HOST=localhost
DB_USER=root
DB_PASS=senha
```

## Dependências Principais
```
requests pandas openpyxl selenium beautifulsoup4
transformers torch pytest python-dotenv streamlit
python-telegram-bot tweepy openai
```

##  Testes
```bash
pytest tests/ -v
```


## Contribuindo
Veja [CONTRIBUTING.md](CONTRIBUTING.md) para regras e dicas de contribuição.

---
Este projeto segue boas práticas de código, testes automatizados, integração contínua (CI) e documentação. Para dúvidas, sugestões ou bugs, abra uma issue ou envie um PR!

---

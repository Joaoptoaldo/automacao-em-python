# CHANGELOG

Todas as mudanças notáveis deste projeto serão documentadas aqui.

## [1.0.0] - 2026-04-19
### Adicionado
- Estrutura inicial do projeto 
- requirements.txt com dependências principais.
- Testes básicos em tests/.

### Alterado
- --

### Removido
- --

## [1.1.0] - 2026-07-16

### Alterado
- **`requirements.txt`**: Versões fixas (`==`) alteradas para (`>=`) para melhor compatibilidade de instalação (especialmente do `pandas` e `torch`).
- **`automacao_escritorio/enviar_emails.py`**: Refatorado para criar o corpo do e-mail antes da verificação de credenciais. Substituído o log de modo simulado (que escondia bugs) por `raise ValueError`.
- **`automacao_escritorio/gerar_relatorios.py`**: Adicionado inclusão no `sys.path` para suportar importação de pacotes internos (utils) ao rodar localmente.
- **`ia_aplicada/chatbot_nlp.py`**: Corrigido *deprecation warning* do `transformers` (uso de `max_new_tokens` no lugar de `max_length`).
- **`ia_aplicada/classificar_imagens.py`**: Corrigido *deprecation warning* do `torchvision` (`pretrained=True` substituído por `weights='DEFAULT'`).
- **`integracao_apis/postagens_sociais.py` e `telegram_bot.py`**: Removido early return que ocultava falhas de token, substituído por exceções explícitas (`raise ValueError`).
- **`projetos_exemplo/pipeline_ia.py`**: Corrigida integração do módulo de PDF, habilitando de fato a chamada da função `gerar_pdf()`.

### Adicionado
- **Testes Unitários**: Criados scripts `tests/test_enviar_emails.py` e `tests/test_integracoes.py` (usando `unittest.mock`) para testar integrações e garantir que dependências externas possuam cobertura de testes mesmo sem credenciais válidas.

### Removido
- --

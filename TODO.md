# TODO - Correção CI: pandas incompatível com Python 3.8

## Plano
- [x] Entender o erro: pandas==2.2.2 requer Python >=3.9, mas CI usa 3.8
- [x] Escolher estratégia: Opção B (manter Python 3.8, downgrade pandas)
- [x] Editar `requirements.txt`: `pandas==2.2.2` → `pandas==2.0.3`
- [x] Validar e ajustar `python-telegram-bot==21.5` → `python-telegram-bot==20.8` (também requer Python >= 3.9)
- [ ] Commitar alterações


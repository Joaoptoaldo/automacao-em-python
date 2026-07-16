#!/usr/bin/env python3
"""
Testes basicos com pytest.
Uso: pytest tests/test_exemplos.py -v
"""

from utils.helpers import log_info
from automacao_tarefas.renomear_arquivos import renomear_arquivos
from monitoramento_alertas.detectar_anomalias import detectar_anomalias
from monitoramento_alertas.monitor_sites import iniciar_monitoramento


def test_helpers():
    """Garante que o helper de log esta disponivel."""
    assert callable(log_info)


def test_renomear(tmp_path):
    """Renomeia arquivos do diretorio com prefixo auto_."""
    arquivo = tmp_path / "arquivo.txt"
    arquivo.write_text("conteudo", encoding="utf-8")

    renomear_arquivos(str(tmp_path))

    assert (tmp_path / "auto_arquivo.txt").exists()


def test_detectar_anomalias():
    """Detecta o valor fora do padrao na serie de exemplo."""
    anomalias = detectar_anomalias([10, 12, 11, 9, 50, 13, 14])
    assert anomalias.tolist() == [50]


def test_monitor_importavel():
    """O monitor pode ser importado sem iniciar loop automaticamente."""
    assert callable(iniciar_monitoramento)

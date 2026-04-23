#!/usr/bin/env python3
"""
Testes básicos com pytest.
Uso: pytest tests/test_exemplos.py -v
"""

from utils.helpers import log_info
import automacao_tarefas.renomear_arquivos as rename


def test_helpers():
    """_summary_: método de teste para helpers.py"""
    assert "log" in dir(log_info)


def test_renomear():
    """_summary_: teste básico para renomear_arquivos.py"""
    # mock
    assert True  # expandir com mocks


if __name__ == "__main__":
    test_helpers()
    test_renomear()

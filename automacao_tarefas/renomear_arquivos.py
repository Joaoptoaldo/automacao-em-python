#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para renomear arquivos em massa em uma pasta.
Exemplo: Adiciona 'auto_' como prefixo.
Uso: python renomear_arquivos.py [pasta]
"""

from logging import Logger
import os
import sys
from utils.helpers import setup_logger, log_info


def renomear_arquivos(pasta=".") -> None:
    """_summary_: método para renomear arquivos em uma pasta, adicionando prefixo 'auto_'. Pode ser expandido para regras mais complexas.

    Args:
        pasta (str, optional): _description_. Defaults to '.'.
    """
    logger: Logger = setup_logger("renomear")
    arquivos: list[str] = [
        f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))
    ]
    for arquivo in arquivos:
        novo_nome: str = f"auto_{arquivo}"
        antigo: str = os.path.join(pasta, arquivo)
        novo: str = os.path.join(pasta, novo_nome)
        os.rename(antigo, novo)
        log_info(logger, f"Renomeado: {arquivo} -> {novo_nome}")


if __name__ == "__main__":
    pasta: str = sys.argv[1] if len(sys.argv) > 1 else "."
    renomear_arquivos(pasta)
    print("Renomeação concluída!")

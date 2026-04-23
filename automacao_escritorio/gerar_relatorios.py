#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera relatório Excel e PDF simples.
Uso: python gerar_relatorios.py
"""

from logging import Logger

import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from utils.helpers import setup_logger, log_info


def gerar_excel() -> None:
    """_summary_: gera um relatório Excel simples com pandas"""
    data = {"Vendas": [100, 200, 150], "Produtos": ["A", "B", "C"]}
    df = pd.DataFrame(data)
    df.to_excel("relatorio_vendas.xlsx", index=False)
    log_info(logger, "Excel gerado: relatorio_vendas.xlsx")


def gerar_pdf() -> None:
    """_summary_: gera um relatório PDF simples com reportlab"""
    c = canvas.Canvas("relatorio_vendas.pdf", pagesize=letter)
    c.drawString(100, 750, "Relatório de Vendas Automatizado")
    c.drawString(100, 700, "Vendas: 100, 200, 150")
    c.save()
    log_info(logger, "PDF gerado: relatorio_vendas.pdf")


logger: Logger = setup_logger("relatorios")

if __name__ == "__main__":
    gerar_excel()
    gerar_pdf()
    print("Relatórios gerados!")

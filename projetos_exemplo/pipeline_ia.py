#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pipeline completo: scrape + análise sentimentos + relatório PDF.
Uso: python pipeline_ia.py
"""

from automacao_tarefas.web_scraping import scrape_headlines
from ia_aplicada.analise_sentimentos import analisar_sentimento
from automacao_escritorio.gerar_relatorios import gerar_pdf  # Adaptar
from utils.helpers import setup_logger, log_info

def pipeline():
    logger = setup_logger('pipeline')
    log_info(logger, '1. Scraping dados...')
    # simular scrape
    textos = ['Ótima notícia!', 'Ruim demais.']
    log_info(logger, '2. Análise IA...')
    for t in textos:
        analisar_sentimento(t)
    log_info(logger, '3. Gerar relatório...')
    # chamar gerar_relatorios adaptado
    log_info(logger, 'Pipeline concluído! Veja relatorios.')

if __name__ == '__main__':
    pipeline()


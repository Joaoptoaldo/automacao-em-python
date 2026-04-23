#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise de sentimentos com Transformers.
Uso: python analise_sentimentos.py
"""

from transformers import pipeline
from utils.helpers import setup_logger, log_info

def analisar_sentimento(texto):
    """_summary_: método para analisar o sentimento de um texto usando Transformers.

    Args:
        texto (_type_): _description_
    """
    logger = setup_logger('sentimentos')
    classifier = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')
    resultado = classifier(texto)
    log_info(logger, f'Texto: {texto}')
    log_info(logger, f'Sentimento: {resultado[0]["label"]} ({resultado[0]["score"]:.2f})')

if __name__ == '__main__':
    textos = [
        'Amo programar em python!',
        'Que dia horrível...',
        'Produto ok'
    ]
    for t in textos:
        analisar_sentimento(t)


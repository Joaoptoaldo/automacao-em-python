#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Postagem simulada no Twitter/X com Tweepy.
Uso: python postagens_sociais.py "Mensagem teste"
Requer chaves Twitter no .env (TWITTER_API_KEY, etc.)
"""

import tweepy
import sys
from utils.helpers import load_env, setup_logger, log_info
import os

load_env()
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_SECRET")


def post_tweet(texto):
    """_summary_: método para postar um tweet usando a API do Twitter via Tweepy. Se as chaves de API não estiverem configuradas, o método simula a postagem e loga a mensagem.

    Args:
        texto (_type_): _description_: texto da mensagem a ser postada no Twitter
    """
    logger = setup_logger("twitter")
    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        log_info(logger, "Configure chaves no .env. Modo simulado.")
        log_info(logger, f"SIMULADO: Tweet: {texto}")
        return
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    # A API do Twitter mudou e agora usa o método create_tweet para postar. O código foi atualizado para refletir isso.
    try:
        response = client.create_tweet(text=texto)
        log_info(logger, f'Tweet postado: {response.data["id"]}')
    except Exception as e:
        log_info(logger, f"Erro: {e}")


if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "Automação py teste! #automacao"
    post_tweet(msg)

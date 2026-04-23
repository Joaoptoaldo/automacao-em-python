#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Previsão do tempo via OpenWeatherMap.
Uso: python api_previsao.py sao_paulo
Requer OPENWEATHER_KEY no .env
"""

import requests
import sys
from utils.helpers import load_env, setup_logger, log_info
import os

load_env()
API_KEY = os.getenv("OPENWEATHER_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_previsao(cidade):
    """_summary_: método para obter a previsão do tempo de uma cidade usando a API do OpenWeatherMap. A resposta é processada e as informações relevantes (temperatura e descrição) são logadas.

    Args:
        cidade (_type_): _description_: nome da cidade para a qual obter a previsão do tempo
    """
    logger = setup_logger("previsao")
    params = {"q": cidade, "appid": API_KEY, "units": "metric", "lang": "pt_br"}
    resp = requests.get(BASE_URL, params=params)
    data = resp.json()
    if resp.status_code == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        log_info(logger, f"{cidade}: {temp}°C - {desc}")
    else:
        log_info(logger, f"Erro: {data}")


if __name__ == "__main__":
    cidade = sys.argv[1] if len(sys.argv) > 1 else "Sao Paulo"
    get_previsao(cidade)

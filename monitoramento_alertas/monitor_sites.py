#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monitora site e alerta se down.
Uso: python monitor_sites.py
"""

from logging import Logger

import requests
import schedule
import time
from utils.helpers import setup_logger, log_info


def checar_site(url) -> None:
    """_summary_: função para checar se um site está online. Faz uma requisição GET e verifica o status code. Se o site estiver down ou ocorrer um erro, um alerta é logado.

    Args:
        url (_type_): _description_: URL do site a ser monitorado
    """
    logger: Logger = setup_logger("monitor")
    try:
        resp: requests.Response = requests.get(url, timeout=5)
        if resp.status_code == 200:
            log_info(logger, f"{url} OK")
        else:
            log_info(logger, f"ALERTA: {url} status {resp.status_code}")
    except Exception as e:
        log_info(logger, f"ALERTA: {url} down - {e}")


schedule.every(10).seconds.do(checar_site, "https://www.google.com")

while True:
    schedule.run_pending()
    time.sleep(1)

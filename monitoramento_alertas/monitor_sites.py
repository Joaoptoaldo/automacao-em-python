#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monitora site e alerta se down.
Uso: python monitor_sites.py
"""

import time
from logging import Logger

import requests
import schedule

from utils.helpers import setup_logger, log_info


def checar_site(url) -> None:
    """Checa se um site esta online."""
    logger: Logger = setup_logger("monitor")
    try:
        resp: requests.Response = requests.get(url, timeout=5)
        if resp.status_code == 200:
            log_info(logger, f"{url} OK")
        else:
            log_info(logger, f"ALERTA: {url} status {resp.status_code}")
    except Exception as e:
        log_info(logger, f"ALERTA: {url} down - {e}")


def iniciar_monitoramento(
    url: str = "https://www.google.com", intervalo_segundos: int = 10
) -> None:
    """Agenda verificacoes periodicas sem executar no import do modulo."""
    schedule.every(intervalo_segundos).seconds.do(checar_site, url)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    iniciar_monitoramento()

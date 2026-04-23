#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Preenchimento automático de form com Selenium (exemplo Google).
Uso: python preencher_formularios.py
Requer chromedriver no PATH.
"""

from logging import Logger

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.helpers import setup_logger, log_info
import time


def preencher_form() -> None:
    """
    Preenche automaticamente o campo de busca do Google usando Selenium.

    - Abre o navegador Chrome.
    - Acessa https://www.google.com.
    - Preenche o campo de busca com 'Automação Python' e envia.
    - Aguarda 2 segundos e registra o log.
    - Encerra o navegador.
    """
    logger: Logger = setup_logger("form")
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    # Exemplo busca
    campo = driver.find_element(By.NAME, "q")
    campo.send_keys("Automação Python")
    campo.submit()
    time.sleep(2)
    log_info(logger, "Form preenchido e enviado!")
    driver.quit()


if __name__ == "__main__":
    preencher_form()

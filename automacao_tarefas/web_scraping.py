#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web scraping simples com BeautifulSoup.
Exemplo: Headlines do G1.
"""

from logging import Logger

import requests
from bs4 import BeautifulSoup
from utils.helpers import setup_logger, log_info


def scrape_headlines(url="https://g1.globo.com/") -> None:
    """_summary_: método para fazer web scraping de um site de notícias e extrair as principais manchetes. Pode ser adaptado para outros sites e tipos de dados.

    Args:
        url (str, optional): _description_. Defaults to 'https://g1.globo.com/'.
    """
    logger: Logger = setup_logger("scraping")
    resp: requests.Response = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    titulos = soup.find_all("h2")[:5]
    for i, t in enumerate(titulos, 1):
        log_info(logger, f"{i}. {t.get_text().strip()}")


if __name__ == "__main__":
    scrape_headlines()

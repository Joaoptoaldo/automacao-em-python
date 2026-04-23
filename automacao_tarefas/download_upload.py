#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download de URL e upload simulado (ex: salvar local).
Uso: python download_upload.py https://exemplo.com/file.txt
"""

import requests
import os
from utils.helpers import setup_logger, log_info


def download_file(url, destino="downloads"):
    """_summary_: método simples para baixar um arquivo de uma URL e salvar localmente. Pode ser expandido para upload real

    Args:
        url (_type_): _description_: URL do arquivo a ser baixado
        destino (str, optional): _description_. Defaults to 'downloads'.
    """
    logger = setup_logger("download")
    os.makedirs(destino, exist_ok=True)
    nome_arq = url.split("/")[-1]
    resp = requests.get(url)
    path = os.path.join(destino, nome_arq)
    with open(path, "wb") as f:
        f.write(resp.content)
    log_info(logger, f"Downloaded: {path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python download_upload.py <url>")
        sys.exit(1)
    download_file(sys.argv[1])

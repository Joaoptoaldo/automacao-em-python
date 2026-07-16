#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Envio de email automatizado com smtplib.
Uso: python enviar_emails.py
Requer GMAIL_USER, GMAIL_APP_PASSWORD no .env
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils.helpers import load_env, setup_logger, log_info

load_env()
USER = os.getenv("GMAIL_USER")
PASS = os.getenv("GMAIL_APP_PASSWORD") or os.getenv("GMAIL_PASS")


def enviar_email(destino, assunto, corpo):
    """Envia email usando SMTP. Exige configuracao valida."""
    logger = setup_logger("email")

    msg = MIMEMultipart()
    msg["From"] = USER if USER else "mock@email.com"
    msg["To"] = destino
    msg["Subject"] = assunto
    msg.attach(MIMEText(corpo, "plain"))

    if not USER or not PASS:
        log_info(logger, "Configure .env. Nao é possível autenticar no SMTP sem credenciais.")
        raise ValueError("Credenciais de email não encontradas no .env")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(USER, PASS)
    server.sendmail(USER, destino, msg.as_string())
    server.quit()
    log_info(logger, f"Email enviado para {destino}")


if __name__ == "__main__":
    try:
        enviar_email("exemplo@email.com", "Relatorio Automatico", "Veja os dados anexos.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Envio de email automatizado com smtplib.
Uso: python enviar_emails.py
Requer GMAIL_USER, GMAIL_PASS no .env
"""

import smtplib
from email.mime.text import MimeText
from email.mime.multipart import MIMEMultipart
from utils.helpers import load_env, setup_logger, log_info
import os

load_env()
USER = os.getenv('GMAIL_USER')
PASS = os.getenv('GMAIL_PASS')

def enviar_email(destino, assunto, corpo):
    """_summary_: envia email usando SMTP. Se chaves não configuradas, simula o envio.

    Args:
        destino (_type_): _description_: email do destinatário
        assunto (_type_): _description_: assunto do email
        corpo (_type_): _description_: corpo do email
    """
    logger = setup_logger('email')
    if not USER or not PASS:
        log_info(logger, 'Configure .env. Modo simulado.')
        log_info(logger, f'SIMULADO para {destino}: {assunto}')
        return
    msg = MIMEMultipart()
    msg['From'] = USER
    msg['To'] = destino
    msg['Subject'] = assunto
    msg.attach(MimeText(corpo, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(USER, PASS)
    text = msg.as_string()
    server.sendmail(USER, destino, text)
    server.quit()
    log_info(logger, f'Email enviado para {destino}')

if __name__ == '__main__':
    enviar_email('exemplo@email.com', 'Relatório Automático', 'Veja os dados anexos.')


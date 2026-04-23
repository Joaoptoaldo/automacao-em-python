#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bot Telegram simples (eco).
Uso: python telegram_bot.py
Requer TELEGRAM_TOKEN no .env
"""

import logging
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from utils.helpers import load_env, setup_logger, log_info

load_env()
TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Envie uma mensagem.")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


def main():
    logger = setup_logger("telegram_bot")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    log_info(logger, "Bot iniciado...")
    app.run_polling()


if __name__ == "__main__":
    main()

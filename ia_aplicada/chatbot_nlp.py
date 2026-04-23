#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chatbot simples com pipeline Transformers.
Uso: python chatbot_nlp.py
Digite 'sair' para parar.
"""

from transformers import pipeline
from utils.helpers import setup_logger, log_info

generator = pipeline('text-generation', model='gpt2')

def chatbot():
    """_summary_: função principal do chatbot, que recebe input do usuário e gera respostas usando o modelo GPT-2. O loop continua até o usuário digitar 'sair'.
     As interações são logadas usando o logger configurado.
    """
    logger = setup_logger('chatbot')
    print('Chatbot: Olá! Fale algo (sair para parar).')
    while True:
        user_input = input('Você: ')
        if user_input.lower() == 'sair':
            break
        resposta = generator(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
        log_info(logger, f'Bot: {resposta}')
        print(f'Bot: {resposta}')

if __name__ == '__main__':
    chatbot()


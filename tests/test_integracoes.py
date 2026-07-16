import pytest
from unittest.mock import patch, MagicMock
from integracao_apis.api_previsao import get_previsao
from integracao_apis.postagens_sociais import post_tweet
from integracao_apis.telegram_bot import main as telegram_main

@patch('integracao_apis.api_previsao.requests.get')
def test_get_previsao_sucesso(mock_get):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "main": {"temp": 25.5},
        "weather": [{"description": "céu limpo"}]
    }
    mock_get.return_value = mock_resp

    with patch('integracao_apis.api_previsao.API_KEY', 'fake_key'):
        get_previsao("Sao Paulo")
        mock_get.assert_called_once()

@patch('integracao_apis.postagens_sociais.tweepy.Client')
def test_post_tweet_sucesso(mock_client):
    mock_instance = MagicMock()
    mock_instance.create_tweet.return_value = MagicMock(data={"id": "12345"})
    mock_client.return_value = mock_instance

    with patch('integracao_apis.postagens_sociais.consumer_key', 'fake'), \
         patch('integracao_apis.postagens_sociais.consumer_secret', 'fake'), \
         patch('integracao_apis.postagens_sociais.access_token', 'fake'), \
         patch('integracao_apis.postagens_sociais.access_token_secret', 'fake'):
        
        post_tweet("Teste de tweet")
        mock_instance.create_tweet.assert_called_once_with(text="Teste de tweet")

@patch('integracao_apis.telegram_bot.Application')
def test_telegram_bot_main(mock_app):
    mock_builder = MagicMock()
    mock_app.builder.return_value = mock_builder
    mock_builder.token.return_value = mock_builder
    mock_instance = MagicMock()
    mock_builder.build.return_value = mock_instance

    with patch('integracao_apis.telegram_bot.TOKEN', 'fake_token'):
        telegram_main()
        mock_instance.add_handler.assert_called()
        mock_instance.run_polling.assert_called_once()

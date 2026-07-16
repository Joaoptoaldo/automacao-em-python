import pytest
from unittest.mock import patch, MagicMock
from automacao_escritorio.enviar_emails import enviar_email
import automacao_escritorio.enviar_emails as email_module


def test_enviar_email_com_credenciais_mocks():
    """Testa o envio de e-mail usando mock para smtplib.SMTP"""
    with patch.object(email_module, "USER", "test@test.com"), patch.object(
        email_module, "PASS", "secret"
    ), patch("automacao_escritorio.enviar_emails.smtplib.SMTP") as mock_smtp:

        mock_server = MagicMock()
        mock_smtp.return_value = mock_server

        enviar_email("destino@test.com", "Assunto", "Corpo")

        mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once_with("test@test.com", "secret")
        mock_server.sendmail.assert_called_once()
        mock_server.quit.assert_called_once()

def test_enviar_email_sem_credenciais():
    """Testa comportamento quando não há credenciais, deve lançar exceção."""
    with patch.object(email_module, "USER", None), patch.object(
        email_module, "PASS", None
    ):

        with pytest.raises(ValueError, match="Credenciais de email não encontradas"):
            enviar_email("destino@test.com", "Assunto", "Corpo")

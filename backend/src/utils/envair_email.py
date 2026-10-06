import smtplib
import secrets
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def disparar_email(email_destino: str, token: str):
    remetente = "seu_email_de_teste@gmail.com"
    senha_app = "sua_senha_de_aplicativo_aqui" # Esconda isso no arquivo .env
    
    # Monta a estrutura da mensagem
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = email_destino
    mensagem['Subject'] = "Ative sua conta em nosso sistema! Arena Society"
    
    link_confirmacao = f"https://sua-api.com/email/confirmar?token={token}" # rota pendente
    
    # O visual da mensagem em HTML
    corpo_html = f"""
    <html>
        <body style="font-family: Arial, sans-serif; text-align: center; padding: 20px;">
            <h2>Bem-vindo!</h2>
            <p>Falta apenas um passo. Confirme que este e-mail é seu clicando no botão abaixo:</p>
            <br>
            <a href="{link_confirmacao}" style="background-color: #28a745; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold;">
                Confirmar Meu E-mail
            </a>
        </body>
    </html>
    """
    mensagem.attach(MIMEText(corpo_html, 'html'))
    
    # Conecta no servidor do Gmail e envia
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls() # Criptografa a conexão
        servidor.login(remetente, senha_app)
        servidor.send_message(mensagem)
        servidor.quit()
        print(f"📩 E-mail de confirmação enviado para {email_destino}")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")
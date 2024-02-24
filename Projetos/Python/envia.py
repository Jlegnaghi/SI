import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email():
    # Configurações do servidor SMTP
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'jeffersonlegnaghi07@gmail.com'
    smtp_password = 'dveicdejxlhufrzh'

    # Configurações do email
    sender_email = 'jeffersonlegnaghi07@gmail.com'
    receiver_email = 'jefferson@udc.edu.br'
    subject = 'ATENÇÂO'
    message = 'Olá, Estou ligado!'

    # Criando o objeto MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Adicionando o corpo da mensagem como texto
    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    # Inicializando o servidor SMTP
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Enviando o email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Encerrando a conexão com o servidor SMTP
    server.quit()

enviar_email()

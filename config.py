import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Configuración del servidor de correo
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', '')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')
    
    # Destinatario fijo
    RECIPIENT_EMAIL = 'gbricenor@ucentral.edu.co'
    
    TEAM_MEMBERS = ['Lizeth Eliana Acevedo', 'Harold Nicolas Neisa']
    
    EMAIL_SUBJECT = 'Presentación del Equipo Sistemas Distribuidos Grupo 1'
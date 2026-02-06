from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config
import os

# Obtener ruta absoluta
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

print("=" * 60)
print("🚀 SISTEMAS DISTRIBUIDOS - Envío de Correo")
print(f"📁 Plantillas en: {TEMPLATES_DIR}")
print("=" * 60)

app = Flask(__name__, template_folder=TEMPLATES_DIR)
app.config.from_object(Config)
app.secret_key = 'clave_secreta_para_flask'

def create_email_body(members):
    body = "Estimado Ing Giovany,\n\n"
    body += "Nos complace presentarnos como equipo:\n\n"
    
    for i, member in enumerate(members, 1):
        body += f"{i}. {member}\n"
    
    body += "\n Repositorio Git:https://github.com/NicolasNeisa21/Presentacion_Correo- Saludos cordiales,\n"
    body += f"{', '.join(members)}"
    
    return body

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        return True, "Correo enviado exitosamente"
        
    except Exception as e:
        return False, f"Error al enviar el correo: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sender_email = request.form.get('sender_email')
        sender_password = request.form.get('sender_password')
        
        if not sender_email or not sender_password:
            flash('Por favor, ingresa tu correo y contraseña', 'error')
            return redirect(url_for('index'))
        
        member1 = request.form.get('member1', app.config['TEAM_MEMBERS'][0])
        member2 = request.form.get('member2', app.config['TEAM_MEMBERS'][1])
        
        members = [member1, member2]
        email_body = create_email_body(members)
        
        success, message = send_email(
            sender_email,
            sender_password,
            app.config['RECIPIENT_EMAIL'],
            app.config['EMAIL_SUBJECT'],
            email_body
        )
        
        if success:
            flash(message, 'success')
        else:
            flash(message, 'error')
        
        return redirect(url_for('index'))
    
    return render_template('index.html', 
                         members=app.config['TEAM_MEMBERS'],
                         recipient=app.config['RECIPIENT_EMAIL'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)

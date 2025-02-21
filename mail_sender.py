import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Mailgun SMTP Ayarları
SMTP_SERVER = "smtp.mailgun.org"
SMTP_PORT = 587  # TLS kullanacağız
SMTP_USERNAME = "postmaster@sandbox865255d8b1554bdd988abd65b7815004.mailgun.org"  # Buraya Mailgun kullanıcı adını gir
SMTP_PASSWORD = "f055c8dc10e676d4b8f3b347f017c3a2-ac3d5f74-582717b9"  # Buraya Mailgun API Key'i gir

SENDER_EMAIL = "program.dev.eng@gmail.com"  # Mailgun’da doğrulanan bir e-posta olmalı

def send_mail(recipient, subject, body):
    """Mailgun SMTP kullanarak mail gönderir."""
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # TLS bağlantısını başlat
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient, msg.as_string())
        print(f"E-posta başarıyla gönderildi: {recipient}")
    except Exception as e:
        print(f"E-posta gönderme hatası: {e}")

# ✅ TEST KISMI: Mail gönderme işlemini burada test edelim
if __name__ == "__main__":
    test_recipient = "program.dev.eng@gmail.com"  # Buraya test için bir e-posta adresi gir
    test_subject = "Mailgun ile Test Maili"
    test_body = "Bu e-posta, Mailgun SMTP ile gönderildi."

    print("Test e-postası gönderiliyor...")
    send_mail(test_recipient, test_subject, test_body)

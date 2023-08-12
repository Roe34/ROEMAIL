import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os

def send_email():
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("figlet ROEMAİL")
    time.sleep(2) 

    sender_email = input("E-posta adresinizi girin: ")
    smtp_username = sender_email
    smtp_password = input("E-posta şifrenizi girin: ")
    receiver_email = input("Alıcı e-posta adresini girin: ")
    subject = input("E-posta konusunu girin: ")
    message = input("E-posta içeriğini girin: ")

    smtp_server = "smtp.example.com"
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print("E-posta gönderilirken bir hata oluştu:", e)

# Ana program
if __name__ == "__main__":
    send_email()

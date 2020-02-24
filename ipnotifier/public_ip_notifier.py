from requests import get
from send_email import send_email
from config_helper import read_setting, write_setting
import logging

logging.basicConfig(filename='ipnotifier.log',level=logging.DEBUG)
ip = get('https://api.ipify.org').text
last_public_ip = read_setting('ip', 'public_ip')

# get public ip
if last_public_ip != ip:
    send_email('IPApp message', 'Hello Linh: this is your number today: ' + ip)
    write_setting('ip', 'public_ip', ip)
else:
    logging.info('No email is sent')
    print('No email is sent')

import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv
import os


def send_to_me(title, body):
    load_dotenv()
    username = os.environ.get('NAVER_ID')
    password = os.environ.get('NAVER_PW')
    sender = f'{username}@naver.com'
    receiver = sender  # 내게쓰기

    with smtplib.SMTP('smtp.naver.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, password)

        msg = MIMEText(body)
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = title
        smtp.sendmail(sender, receiver, msg.as_string())

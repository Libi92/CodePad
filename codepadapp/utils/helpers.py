from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib

__author__ = 'cyberprism'

build = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def generateRandomPassword(length = 8):
    password = ""
    for i in range(length):
        password += build[random.randint(0, len(build)-1)]
    return password


def sendEmail(to, subject, message):
    fromaddr = "virtuallab44@gmail.com"
    toaddr = to
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "1517414244")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


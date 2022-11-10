import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version

from random import randint


def send_new(email, code):
    try:
        server = 'smtp.mail.ru'
        user = 'kuslytuna@mail.ru'
        password = 't7RdZd0vrQaLRSXfMWr3'

        to_email = email
        recipients = [to_email]
        sender = 'kuslytuna@mail.ru'
        subject = 'Код для привязки почты'
        text = f'<h3>Ваш код для привязки почты {to_email}</h3><b><br><h1>Код -> {code}</h1>'
        html = '<html>' \
               '<head >' \
               '</style>' \
               '</head>' \
               '<body>' \
               '<p>' + text + '</p>' \
               '</body>' \
               '</html>'

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = 'CODE <' + sender + '>'
        msg['To'] = ', '.join(recipients)
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg['X-Mailer'] = 'Python/' + (python_version())

        part_text = MIMEText(text, 'plain')
        part_html = MIMEText(html, 'html')

        msg.attach(part_text)
        msg.attach(part_html)

        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()
        return True
    except Exception as e:
        return False


def send_forgot(email, code):
    try:
        server = 'smtp.mail.ru'
        user = 'kuslytuna@mail.ru'
        password = 't7RdZd0vrQaLRSXfMWr3'

        to_email = email
        recipients = [to_email]
        sender = 'kuslytuna@mail.ru'
        subject = 'Код для восстановления пароля'
        text = f'<h3>Ваш код для востановления пароля</h3><b><br><h1>Код -> {code}</h1>'
        html = '<html>' \
               '<head >' \
               '</style>' \
               '</head>' \
               '<body>' \
               '<p>' + text + '</p>' \
                              '</body>' \
                              '</html>'

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = 'CODE <' + sender + '>'
        msg['To'] = ', '.join(recipients)
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg['X-Mailer'] = 'Python/' + (python_version())

        part_text = MIMEText(text, 'plain')
        part_html = MIMEText(html, 'html')

        msg.attach(part_text)
        msg.attach(part_html)

        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()
        print('2')
        return True

    except Exception as e:
        return False
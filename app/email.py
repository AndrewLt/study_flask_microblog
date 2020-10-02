from threading import Thread
from flask import render_template
#from flask_mail import Message
from flask import current_app
import requests

"""Test module. The module send jwt token to my Telegram account"""


def send_async_email(app, msg):
    with app.app_context():
        #mail.send(msg)
        pass


def send_email(subject, sender, recipients, text_body, html_body):
    msg = f'<b>{subject}</b>\nFrom: {sender}\n' \
          f'To: {recipients}\n\n{text_body}\n{html_body}'
    token = current_app.config['TELEGRAM_TOKEN']
    admin_chat_id = current_app.config['TELEGRAM_ADMIN_CHAT_ID']
    requests.get(f'https://api.telegram.org/bot{token}/'
                 f'sendMessage?chat_id={admin_chat_id}&text={msg}&parse_mode=HTML')
    #Thread(target=send_async_email, args=(app, msg)).start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))

"""
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))
"""
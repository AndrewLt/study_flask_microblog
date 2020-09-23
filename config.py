import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 21
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    TELEGRAM_ADMIN_CHAT_ID = os.environ.get('TELEGRAM_ADMIN_CHAT_ID')
    MAIL_SERVER = 'localhost'  # 'smtp.googlemail.com' os.environ.get('MAIL_SERVER')
    MAIL_PORT = 8025  # int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = 1  # os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = 'andrii'  # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = '212'  # os.environ.get('MAIL_PASSWORD')
    ADMINS = ['admin-andrew@example.com']

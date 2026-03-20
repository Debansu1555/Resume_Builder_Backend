import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/resume_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'your_email@gmail.com'
    MAIL_PASSWORD = 'your_app_password'
    MAIL_USE_TLS = True

    SECRET_KEY = "secret"
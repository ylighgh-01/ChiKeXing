# 数据库的配置变量
import os

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'chikexing'
USERNAME = 'root'
PASSWORD = 'wl991224'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

SECRET_KEY = 'sdfsdfsdf123'

# 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = 'xxxxx1@qq.com'
MAIL_PASSWORD = 'xxxxxx'
MAIL_DEFAULT_SENDER = 'xxxxx@qq.com'

# 文件上传
BASE_DIR = os.path.dirname(__name__)
UPLOAD_DIR = os.path.join(BASE_DIR, 'static/images/upload/')

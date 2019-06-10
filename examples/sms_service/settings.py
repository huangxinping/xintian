import os

APP_ID = 'kx_service'
APP_VERSION = '0.0.1'

HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
PORT = os.environ.get('SERVER_PORT', 8001)

MYSQL_CONFIG = {
    'host': os.environ.get('MYSQL_HOST', '192.168.0.210'),
    'port': int(os.environ.get('MYSQL_PORT', 3306)),
    'user': os.environ.get('MYSQL_USER', 'root'),
    'password': os.environ.get('MYSQL_PASSWORD', '123456'),
    'db': os.environ.get('MYSQL_DB', APP_ID)
}

REDIS_CONFIG = {
    'host': os.environ.get('REDIS_HOST', '192.168.0.210'),
    'port': int(os.environ.get('REDIS_PORT', 6379)),
    'password': os.environ.get('REDIS_PASSWORD', None),
    'db': int(os.environ.get('REDIS_DB', 1)),
    'pool_size': int(os.getenv('REDIS_POOL_SIZE', 10)),
    'namespace': APP_ID
}

MONGO_CONFIG = {
    "host": os.getenv('MONGO_HOST', "192.168.0.210"),
    "port": int(os.getenv('MONGO_PORT', 27017)),
    "db": os.getenv('MONGO_DB', APP_ID)
}

API_VERSION = '0.0.1'
API_TITLE = 'Short message micro service.'
API_DESCRIPTION = 'Platform User API by huangxinping'
API_TERMS_OF_SERVICE = 'Nanjing Reliant Data Services(NanJing) Co., Ltd.'
API_PRODUCES_CONTENT_TYPES = ['application/json']
API_CONTACT_EMAIL = 'o0402@outlook.com'

SENTRY_DSN = 'https://b407a597bd2946a5a660a36bad6f3411:2aecfd0ef1c2493abb2673ebacd21d50@error.jiankanghao.net/32'

USE_PROMETHUS_FOR_JAEGER = False
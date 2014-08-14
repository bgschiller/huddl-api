import logging
import logging.handlers
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from json_app import make_json_app

logger = logging.getLogger('') #root logger
logger.setLevel(logging.DEBUG)
fh = logging.handlers.TimedRotatingFileHandler('huddl_api.log',when='W0')

formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.info('initializing app...')

app = make_json_app(Flask(__name__))

app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///huddl.sqlite'
app.debug = True

logger.info('initializing db...')

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

logger.info('importing views...')

import huddl.views

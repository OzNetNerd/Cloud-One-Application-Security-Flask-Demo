import trend_app_protect.start
import logging
from flask import Flask

gunicorn_error_logger = logging.getLogger('gunicorn.error')

app = Flask(__name__)
app.secret_key = 'SECRET'
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)

from app import views
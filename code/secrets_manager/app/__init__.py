import os
import boto3
import json
from botocore.exceptions import ClientError


def get_secrets():
    secret_name = "TrendMicro/ApplicationSecurity"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=session.region_name,
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )

    except ClientError as e:
        error_message = e.response['Error']['Message']
        print(f'Error: {error_message}')
        raise

    secret_string = json.loads(get_secret_value_response['SecretString'])
    trend_ap_key = secret_string['TREND_AP_KEY']
    trend_ap_secret = secret_string['TREND_AP_SECRET']

    os.environ["TREND_AP_KEY"] = trend_ap_key
    os.environ["TREND_AP_SECRET"] = trend_ap_secret


get_secrets()

import trend_app_protect.start
import logging
from flask import Flask

gunicorn_error_logger = logging.getLogger('gunicorn.error')

app = Flask(__name__)
app.secret_key = 'SECRET'
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)

from app import views
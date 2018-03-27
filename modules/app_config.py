# -*- coding: utf-8 -*-
import os
import logging
from gluon.contrib.appconfig import AppConfig

conf = AppConfig(reload=False)
env = os.getenv('AMBIENTE', default='prod')

logger = logging.getLogger("web2py.app.web2canvas")
if conf[env]['app']['log_level'] == 'info':
    logger.setLevel(logging.INFO)
elif conf[env]['app']['log_level'] == 'warning':
    logger.setLevel(logging.WARNING)
elif conf[env]['app']['log_level'] == 'error':
    logger.setLevel(logging.ERROR)
elif conf[env]['app']['log_level'] == 'critical':
    logger.setLevel(logging.CRITICAL)
else:
    logger.setLevel(logging.DEBUG)

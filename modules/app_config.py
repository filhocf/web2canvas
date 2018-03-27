# -*- coding: utf-8 -*-
import os
from gluon.contrib.appconfig import AppConfig

conf = AppConfig(reload=False)
env = os.getenv('AMBIENTE', default='prod')

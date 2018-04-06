#!/bin/bash

if [ ! -f /usr/local/web2py/wsgihandler.py ]; then
  cp /usr/local/web2py/handlers/wsgihandler.py /usr/local/web2py
fi

. /configure

nginx

uwsgi --ini /etc/uwsgi/web2py.ini

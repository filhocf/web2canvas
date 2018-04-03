#!/bin/bash

. /configure

exec nginx

exec gunicorn web2py.wsgi:application \
    --name web2canvas \
    --bind 0.0.0.0:8000 \
    --workers 5 \
    --log-level=${LOG_LEVEL}

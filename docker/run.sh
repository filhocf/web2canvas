#!/bin/bash

. /configure

exec nginx

exec uwsgi --ini /etc/uwsgi/web2py.ini

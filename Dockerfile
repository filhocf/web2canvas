FROM python:2

MAINTAINER Claudio Ferreira <filhocf@gmail.com>

ARG PKG_PROXY

# Update all mirrors
RUN \
    # Set a package proxy in next line
    echo ${PKG_PROXY} > /etc/apt/apt.conf; \
    apt-get update

# Install a tool set
RUN apt-get install -y nginx-full libldap2-dev libsasl2-dev vim; \
    pip install uwsgi python-ldap psycopg2-binary

RUN cd /usr/local; \
    echo 'Installing Web2py'; \
    mkdir /usr/local/web2py; \
    curl -L https://github.com/web2py/web2py/archive/master.tar.gz | \
    tar xz --strip-components=1 -C web2py; \
    echo 'Installing PyDAL'; \
    cd /usr/local/web2py/gluon/packages/dal; \
    mkdir /tmp/pydal; \
    curl -L https://github.com/web2py/pydal/archive/d4d7e48c1f82a0b2a27b7475f18ee9f92e3cb0fe.tar.gz | \
    tar xz --strip-components=1 -C /tmp/pydal; \
    mv /tmp/pydal/pydal . ; \
    echo 'Installing Web2Canvas'; \
    cd /usr/local/web2py/applications; \
    mkdir web2canvas; \
    curl -L https://github.com/filhocf/web2canvas/archive/master.tar.gz | \
    tar xz --strip-components=1 -C web2canvas; \
    chown www-data.www-data /usr/local/web2py -R

COPY docker/default.conf /etc/nginx/sites-available/default
COPY docker/web2py.ini /etc/uwsgi/web2py.ini
COPY docker/routes.py /usr/local/web2py/routes.py
COPY docker/configure /configure
COPY docker/run.sh /run.sh

CMD ["/run.sh"]

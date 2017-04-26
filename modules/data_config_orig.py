# -*- coding: utf-8 -*-

## Autenticação para envio de email

EMAIL_SERVER = '<smtp_server>:<smtp_port>'
CLIENT_EMAIL = '<email>'
CLIENT_LOGIN = '<usuario>:<senha>'

## Configuracao do LDAP
LDAP_CONFIG = {
    'mode': 'custom',
    'server': '<ldap_server>',
    'base_dn': '<base_dn>',
    'username_attrib': 'uid',
    'manage_user': True,
    'manage_groups': False,
    'custom_scope': 'subtree',
    'self_signed_certificate': True
}

# Configuracao do PostgreSQL
PG_CONFIG = 'postgres://<dbuser>:<dbpass>@<hostname>/web2canvas_prod'
PG_CONFIG_DEV = 'postgres://<dbuser>:<dbpass>@<hostname>/web2canvas_dev'

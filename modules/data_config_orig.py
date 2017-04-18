# -*- coding: utf-8 -*-

## Autenticação para envio de email

EMAIL_SERVER = '<smtp_server>:<smtp_port>'
CLIENT_EMAIL = '<email>'
CLIENT_LOGIN = '<usuario>:<senha>'

## Configuracao do LDAP
LDAP_CONFIG = {
    'mode': 'custom',
    'server': 'ldap.dataprev.gov.br',
    'base_dn': 'dc=gov,dc=br',
    'username_attrib': 'uid',
    'manage_user': True,
    'manage_groups': False,
    'custom_scope': 'subtree',
    'self_signed_certificate': True
}

# Configuracao do PostgreSQL
PG_CONFIG = 'postgres://<dbname>:<dbpass>@<hostname>/web2canvas_prod'
PG_CONFIG_DEV = 'postgres://<dbname>:<dbpass>@<hostname>/web2canvas_dev'

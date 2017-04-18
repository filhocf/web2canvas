# -*- coding: utf-8 -*-

## Autenticação para envio de email

EMAIL_SERVER = 'smtp.gmail.com:587'
CLIENT_EMAIL = 'you@gmail.com'
CLIENT_LOGIN = 'username:password'

## Configuracao do LDAP
LDAP_CONFIG = {
    "mode": 'custom',
    "server": 'ldap.dataprev.gov.br',
    "base_dn": 'dc=gov,dc=br',
    "username_attrib": 'uid',
    "manage_user": True,
    "manage_groups": False,
    "custom_scope": 'subtree',
    "self_signed_certificate": True
}

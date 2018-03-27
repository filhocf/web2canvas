# -*- coding: utf-8 -*-

#########################################################################
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
#########################################################################

# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# request.requires_https()

# Variaveis importadas
from app_config import conf
from app_config import env
from app_config import logger

try:
    if request.env.web2py_runtime_gae:
        # connect to Google BigTable (optional 'google:datastore://namespace')
        db = DAL('google:datastore')
        # store sessions and tickets there
        session.connect(request, response, db=db)
        # or store session in Memcache, Redis, etc.
        # from gluon.contrib.memdb import MEMDB
        # from google.appengine.api.memcache import Client
        # session.connect(request, response, db = MEMDB(Client()))
    elif conf[env]['database']['uri']:
        # Conecta ao PostgreSQL
        db = DAL(conf[env]['database']['uri'], check_reserved=['all'])
    else:
        # Connect to sqlite
        db = DAL('sqlite://db.sqlite')

    # by default give a view/generic.extension to all actions from localhost
    # none otherwise. a pattern can be 'controller/function.extension'
    response.generic_patterns = ['*'] if request.is_local else []
    # (optional) optimize handling of static files
    # response.optimize_css = 'concat,minify,inline'
    # response.optimize_js = 'concat,minify,inline'

    #########################################################################
    # Here is sample code if you need for
    # - email capabilities
    # - authentication (registration, login, logout, ... )
    # - authorization (role based authorization)
    # - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
    # - old style crud actions
    # (more options discussed in gluon/tools.py)
    #########################################################################

    from gluon.tools import Auth
    from gluon.tools import Crud
    from gluon.tools import Service
    from gluon.tools import PluginManager
    from gluon.tools import prettydate
    from gluon.tools import Mail
    auth = Auth(db)
    crud, service, plugins = Crud(db), Service(), PluginManager()

    # create all tables needed by auth if not custom tables
    if "auth_user" not in db.tables:
        auth.settings.extra_fields['auth_user'] = [
                Field("primeira_vez", "boolean", default=True),
            ]

    # creates all needed tables
    auth.define_tables(username=True, signature=False)

    if "auth_user" not in db.tables:
        db.define_table("auth_user",
            Field("primeira_vez", "boolean", default=True),
            migrate="auth_user.table")

    if "projeto" not in db.tables:
        Projeto = db.define_table("projeto",
            Field("nome", "string", length=200, default=None),
            Field("criado_por", db.auth_user, default=None),
            Field("criado_em", "datetime", default=None),
            Field("parcerias_principais", "text", default=None),
            Field("atividades_principais", "text", default=None),
            Field("recursos_principais", "text", default=None),
            Field("proposta_valor", "text", default=None),
            Field("relacionamento_clientes", "text", default=None),
            Field("canais", "text", default=None),
            Field("segmento_clientes", "text", default=None),
            Field("estrutura_custos", "text", default=None),
            Field("receitas", "text", default=None),
            Field("thumbnail", "upload", default=None),
            format='%(nome)s',
            migrate="projeto.table")

    if "compartilhamento" not in db.tables:
        Compartilhamento = db.define_table("compartilhamento",
            Field("user_id", db.auth_user, default=None),
            Field("projeto_id", db.projeto, default=None),
            migrate="compartilhamento.table")

    try:
        """ Relations between tables (remove fields you don't need from requires) """
        db.projeto.criado_por.requires = IS_IN_DB(
                                    db,
                                    'auth_user.id',
                                    db.auth_user._format
        )
        db.compartilhamento.user_id.requires = IS_IN_DB(
                                    db,
                                    'auth_user.id',
                                    db.auth_user._format
        )
        db.compartilhamento.projeto_id.requires = IS_IN_DB(
                                    db,
                                    'projeto.id',
                                    db.projeto._format
        )
        db.auth_user.full_name = Field.Virtual(
            'full_name',
            lambda row: "%s %s" % (row.auth_user.first_name, row.auth_user.last_name)
        )
    except Exception as e:
        logger.debug(str(e))
        pass

    # configure email
    mail = Mail()
    mail.settings.server = conf[env]['email']['servidor']
    mail.settings.sender = conf[env]['email']['caixa']
    mail.settings.login = conf[env]['email']['credenciais']
    auth.settings.mailer = mail

    try:
        # Allow login with ldap
        from gluon.contrib.login_methods.ldap_auth import ldap_auth
        # all we need is login
        auth.settings.actions_disabled = [
                                        'register',
                                        'change_password',
                                        'request_reset_password',
                                        'retrieve_username'
        ]

        # you don't have to remember me
        auth.settings.remember_me_form = False
        # Configura aplicacao para autenticar via LDAP
        auth.settings.login_methods.append(
            ldap_auth(db=db, **conf[env]['ldap'])
        )
        # redireciona depois do login
        auth.settings.login_next = URL('projetos')
    except Exception as e:
        logger.error(str(e))

    # import Gravatar
    try:
        from gravatar import Gravatar
    except ImportError:
        from gluon.contrib.gravatar import Gravatar

    # multiples languages
    if 'siteLanguage' in request.cookies and not (request.cookies['siteLanguage'] is None):
        T.force(request.cookies['siteLanguage'].value)

except Exception as e:
    logger.debug(str(e))

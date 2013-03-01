# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
    """Home page
    """
    return dict()


def modelo_canvas():
    """Pagina sobre o canvas
    """
    return dict()


@auth.requires_login()
def projetos():
    """Pagina com opcao de criar projetos
    """
    from datetime import datetime
    pessoa = db((Pessoa.usuario1==auth.user.id) | (Pessoa.usuario2==auth.user.id)).select().first()
    meus_projetos = db(Projeto.criado_por==pessoa.id).select()
    projetos_colaborador = ''
    #projetos_colaborador = db(Compartilhamento.usuario_id==auth.user).select()

    form = SQLFORM(Projeto, fields=['nome'], submit_button="Criar")

    if form.process().accepted:
        db(Projeto.id==form.vars.id).update(criado_por=pessoa.id, criado_em=datetime.now())
        redirect(URL('projetos'))

    return dict(form=form, meus_projetos=meus_projetos, projetos_colaborador=projetos_colaborador)


@auth.requires_login()
def projeto_canvas():
    """Pagina com o Canvas do projeto, onde os dados serao editados
    """
    import json
    projeto_id = request.args(0) or redirect(URL('index'))
    session.projeto_id = projeto_id
    usuarios_autorizados =  [i.criado_por for i in db(Projeto.id==projeto_id).select()]

    for i in db(Compartilhamento.projeto_id==projeto_id).select():
        if not i.usuario_id in usuarios_autorizados:
            usuarios_autorizados.append(i.usuario_id)

    if auth.user.id in usuarios_autorizados:
        projeto = db(Projeto.id==projeto_id).select().first()
        time_compartilhamento = db(Compartilhamento.projeto_id==projeto_id).select()
        id_time = [i.usuario_id for i in time_compartilhamento]
        id_time.append(projeto.criado_por)

        usuarios_para_adicionar = {'%s %s' % (i.first_name, i.last_name):i.id for i in db(db.auth_user).select() if not i.id in id_time}

        return dict(projeto=projeto,
                    time_compartilhamento=time_compartilhamento,
                    usuarios_para_adicionar=usuarios_para_adicionar)
    else:
        redirect(URL('index'))


def editar_dados():
    """Funcao que atualiza dados do projeto
    """
    import json

    if request.vars:
        valor = request.vars.value
        pk = request.vars.pk
        campo = request.vars.name

        dados_banco = db(Projeto.id==session.projeto_id).select().first()

        if dados_banco[campo]:
            dicionario_dados = json.loads(dados_banco[campo])
        else:
            dicionario_dados = {}

        dicionario_dados[pk] = valor
        dados = json.dumps(dicionario_dados)

        Projeto[session.projeto_id]= {campo:dados}

        return dict(success="success",msg="gravado com sucesso!")
    else:
        return dict(error="error",msg="erro ao gravar!")


def remove_item():
    """Funcao que atualiza dados do projeto
    """
    import json

    if request.vars:
        pk = request.vars.pk
        campo = request.vars.name

        dados_banco = db(Projeto.id==session.projeto_id).select().first()

        if dados_banco[campo]:
            dicionario_dados = json.loads(dados_banco[campo])
        else:
            dicionario_dados = {}

        if pk in dicionario_dados:
            del dicionario_dados[pk]
            dados = json.dumps(dicionario_dados)
            Projeto[session.projeto_id]= {campo:dados}

        return True
    else:
        return False


def atualiza_itens():
    """Funcao que atualiza dados do projeto
    """
    import json

    if request.vars:
        campo = request.vars.name
        todas_variaveis = request.vars

        valores =  {}
        for v in todas_variaveis:
            if not v == "name":
                valores[v] = todas_variaveis[v]

        dados_banco = db(Projeto.id==session.projeto_id).select().first()
        dados = json.dumps(valores)

        Projeto[session.projeto_id]= {campo:dados}

        return True
    else:
        return False


@auth.requires_login()
def adicionar_usuario():
    """Funcao que adiciona usuario a um projeto
    """
    projeto_id = request.vars['projeto_id'] or redirect(URL('index'))
    usuario_id = int(request.vars['usuario_id']) or redirect(URL('index'))

    projeto = db(Projeto.id==projeto_id).select().first()

    if projeto.criado_por == auth.user.id:
        Compartilhamento.insert(usuario_id=usuario_id,
            projeto_id=projeto_id)
    redirect(URL(c='default', f='projeto_canvas', args=[projeto_id]))


def login():
    if request.vars:
        if request.vars['rede'] == 'facebook':
            session.auth_with = 'facebook'

    redirect(URL('_cadastrar_pessoa'))


@auth.requires_login()
def _cadastrar_pessoa():
    nome = '%s %s' % (session.auth.user.first_name, session.auth.user.last_name)
    count = db((Pessoa.usuario1==session.auth.user.id) | (Pessoa.usuario2==session.auth.user.id)).count()
    if count == 0:
        pessoa_id = Pessoa.insert(
                        nome=nome.strip(),
                        usuario1=session.auth.user.id,
                        )

    redirect(URL('projetos'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    if request.args(0) == 'register':
        import random
        form = auth.register()
        form.element(_name='username')['_value'] = "%s" %random.random()

        return dict(form=form)        

    elif request.args(0) == 'logout':
        session.clear()

    return dict(form = auth())




def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

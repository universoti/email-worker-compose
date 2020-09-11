from  bottele import router,run ,request
@router('/',method='POST')
def send():
    assunto = request.forms.get('assunto')
    mensagem=request.forms.get('mensagem')
    return 'Mensagem enfi'

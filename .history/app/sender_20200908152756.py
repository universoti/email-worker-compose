from  bottle import router,run ,request
@router('/',method='POST')
def send():
    assunto = request.forms.get('assunto')
    mensagem=request.forms.get('mensagem')
    return 'Mensagem enfileirada!Assunto:{} Mensagem:{}'.format(
        assunto,mensagem
    )

if __name__ == '__main__':
    sender = Sender()
    sender.run(host='0.0.0.0', port=8080, debug=True)
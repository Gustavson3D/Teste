
from requests import request


class Roteiro():
    def __init__(self, request):
        self.session = request.session
    
    # pegar a chave da sessão, caso ela esteja ativa
        roteiro = self.session.get('session.key')

        # se a sessão for nova, sem chave! Crie uma.
        if 'session_key' not in request.session:
            roteiro = self.session['session_key'] = {}

        
        # fazer com que o carrinho seja acessivel de quase qualquer página do site
        self.roteiro = roteiro
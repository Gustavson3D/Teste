from .roteiros import Roteiro

# criando o context processor para que o carrinho seja acessado em qualquer página

def roteiro(request):
    #retornando o default
    return {'roteiro': Roteiro(request)}
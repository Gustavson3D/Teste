from.cart import Cart

# criando um processasdor de contexto para o  carrinho de compras funcionar em qualquer lugar do projeto
def cart(request):
    # retornar os dados padrão do Cart
    return {'cart': Cart(request)}
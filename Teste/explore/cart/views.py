import json
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from smarttravel.models import Local
from django.http import JsonResponse
from django.http import HttpResponse


def cart_summary(request):
    return render(request, 'cart_summary.html', {})


def cart_add(request):
    # puxar o carrinho

    print(f"metodo {request.POST.get('local_id')}")
    cart = Cart(request)
    #Testar para postar
    if request.POST.get('action') == 'post':
        #return('O que veio no POST:')
        product_id = int(request.POST.get('local_id'))  # Alteração aqui
        # procurar o produto na database
        product = get_object_or_404(Local, id=product_id)

        # Salvar na sessão
        #cart.add(product=product)

        response = JsonResponse({'Local Nome': product.nome_local})  # Use 'nome_local' em vez de 'name'
        return response
    
    #return  HttpResponse("Not a valid request")

def cart_delete(request):
    pass


def cart_update(request):
    pass
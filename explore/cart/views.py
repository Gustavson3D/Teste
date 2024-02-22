import json
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from smarttravel.models import Local
from django.http import JsonResponse
from django.http import HttpResponse


def cart_summary(request):
    return render(request, 'cart_summary.html', {})


# def cart_add(request):
#     # puxar o carrinho
#     cart = Cart(request)
#     #Testar para postar
#     if request.POST.get('action') == 'post':
#         #return('O que veio no POST:')
#         product_id = request.POST.get('product_id') # Alteração aqui
#         # procurar o produto na database
#         product = get_object_or_404(Local, id=product_id)

#         # Salvar na sessão
#         cart.add(product=product)

#         response = JsonResponse({'Local Nome': product.nome_local})  # Use 'nome_local' em vez de 'name'
#         return response
    
#     #return  HttpResponse("Not a valid request")

def cart_add(request):
    # puxar o carrinho
    cart = Cart(request)
    
    # Testar para postar
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')  # Alteração aqui
        print(product_id)
        # procurar o produto na database
        product = get_object_or_404(Local, id=product_id)
        # Salvar na sessão
        cart.add(product=product)

        cart_quantity = cart.__len__()

        response = JsonResponse({'Local Nome': product.nome_local})
        response = JsonResponse({'Quantidade': cart_quantity})  
        return response
    
    # Retorne uma resposta de erro se não for uma solicitação POST válida
    return HttpResponse("Not a valid request")

def cart_delete(request):
    pass


def cart_update(request):
    pass
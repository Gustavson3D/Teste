import json
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from smarttravel.models import Local
from django.http import JsonResponse
from django.http import HttpResponse


def cart_summary(request):
    # puxar o cart
    cart = Cart(request)
    cart_products = cart.get_product
    return render(request, 'cart_summary.html', {"cart_products": cart_products})



def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Local, id=product_id)
        
        cart.add(product=product)

        cart_quantity = cart.__len__()
        response = JsonResponse({'Local Nome': product.nome_local, 'qty': cart_quantity})
        return response

    return HttpResponse("Not a valid request")



def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        print("Tentativa de excluir o produto:", product_id)

        # Chamar a função delete no Carrinho
        cart.delete(product=product_id)
        response = JsonResponse({'product': product_id})  
        return response

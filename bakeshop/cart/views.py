from django.shortcuts import render, get_object_or_404
from .cart import Cart 
from shop.models import Product
from django.http import JsonResponse

def cart_summary(request): 
    #get the cart 
    # cart = Cart(request)
    # cart_products = cart.get.prods
    return render(request, "cart_summary.html", {})


def cart_add(request): 
    #get the cart 
    cart = Cart(request)
    #test the POST
    if request.POST.get('action') == 'post':
        #get stuff 
        product_id = int(request.POST.get('product_id'))
        #lookup product in database 
        product = get_object_or_404(Product, id=product_id)

        #Save to Session 
        cart.add(product=product)

        #Get Cart Quantity
        cart_quantity = cart.__len__()

        #return response
        response = JsonResponse ({'qty ': cart_quantity })
        return response

def cart_delete(request): 
    pass


def cart_update(request):
    pass
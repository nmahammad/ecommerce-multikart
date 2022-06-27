from ast import Or
from django.shortcuts import render
from .models import Product, ProductVersion, Cart, CartItem, Order
import json
from multiprocessing import context
from pyexpat import model
import re
from django.utils import timezone
from django.shortcuts import render, redirect
from requests import request
from order.forms import OrderForm 
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



# Create your views here.
def order_success(request):
    return render(request, 'order-success.html')

def wish_list(request):
    return render(request, 'wishlist.html')


class CreateOrderView(CreateView, LoginRequiredMixin):
    form_class = OrderForm
    template_name = 'checkout.html'
    success_url = reverse_lazy('order-success')
    #context_object_name = 'order_form'  ???? 

    def form_valid(self, form):
        return super().form_valid(form)


def cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(owner = user,  completed=False)
        cartitems = cart.cart_items.all()
        
    context = {
        "cartitems" : cartitems ,
        'cart' : cart,
       
    }
    return render(request, 'cart.html', context)


def cart_quantity(request):
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(owner = user,  completed=False)
        cartitems = cart.cart_items.all()
        
    context = {
        "cartitems" : cartitems ,
        'cart' : cart,
       
    }
    print
    return render(request, 'base.html', context)


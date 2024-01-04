from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .forms import CategoryForm


def edit_category(request):
    category = Category.objects.get(pk=id)
    return render(request, 'edit_category.html', {'category': category})


def add_category(request):
    submitted = False 

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_category?submitted=True')
    else: 
        form = CategoryForm 
    
    if 'submitted' in request.GET: 
        submitted =True

    return render(request, 'add_category.html', {'form': form, 'submitted': submitted})

def category(request, pk):
    
    category = Category.objects.all()
    category_name = Category.objects.filter(id=pk).first()
    category_id = Category.objects.get(id=pk)
    products = Product.objects.filter(category=category_id)

    category_paginated = Paginator(Category.objects.all(), 3)
    page_number = request.GET.get('page')
    page = category_paginated.get_page(page_number)
    nums = "a" * page.paginator.num_pages

    return render(request, 'category.html', {'category':category, 'category_name':category_name, 'products':products, 'page': page , 'nums': nums})


def product(request, pk):
	category = Category.objects.all()
	product = Product.objects.get(id=pk)
	return render(request, 'product.html', {'category':category, 'product':product})

def home(request): 
    category = Category.objects.all()
    products = Product.objects.all()

    products_paginated = Paginator(Product.objects.all(), 3)
    page_number = request.GET.get('page')
    page = products_paginated.get_page(page_number)
    nums = "a" * page.paginator.num_pages

    return render(request, 'home.html', {'products': products, 'category':category, 'page': page, 'nums': nums})


def about(request):
    category = Category.objects.all()

    about_paginated = Paginator(Category.objects.all(), 5)
    page_number = request.GET.get('page')
    page = about_paginated.get_page(page_number)
    nums = "a" * page.paginator.num_pages

    return render(request, 'about.html', {'category':category, 'nums': nums})


def login_user(request): 
    if request.method == "POST": 
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request, ("You have been Logged in"))
            return redirect('home')

        else: 
            messages.success(request, ("There was an error, please try again"))
            return redirect('login')
    
    else:
     return render(request, 'login.html', {})
    

def logout_user(request): 
     logout(request)
     messages.success(request, ("You have been logged out"))
     return redirect('home')

def register_user(request): 
    form =SignUpForm()
    if request.method == "POST": 
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, ("You Have Registered Successfully..."))
            return redirect('home')
        
        else: 
            messages.success(request, ("There was a problem Registering, please try again..."))
            return  redirect('register')
        
    else:
        
     return render(request, 'register.html', {'form': form})

def order(request):
    pass
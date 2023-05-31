from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as dj_login
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from .models import *
from .forms import RegisterUserForm

import random as rd
import os

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'feedback'},
        {'title': "Добавить продукт", 'url_name': 'add_page'}
        ]


def home(request):
    products = list(Product.objects.all())
    count_of_items = 4
    items = []
    for i in range(count_of_items):
        items += [products[i]]
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'items': items,
        'request': request
    }
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html', {'menu': menu,
                                          'title': 'О сайте',
                                          'request': request})


def addpage(request):
    return render(request, 'addpage.html', {'menu': menu,
                                            'title': 'Добавить продук',
                                            'request': request})


# def register(request):
#     return render(request, 'register.html', {'menu': menu,
#                                             'request': request})

def feedback(request):
    return render(request, 'feedback.html', {'menu': menu,
                                             'title': 'Обратная связь',
                                             'request': request})


def post(request):
    posts = Product.objects.all()
    return render(request, 'post.html', {'menu': menu,
                                         'posts': posts,
                                         'request': request})


def show_post(request, post_id):
    post = get_object_or_404(Product, pk=post_id)
    context = {
        'menu': menu,
        'post': post,
        'title': post.title,
        'request': request}
    return render(request, 'post.html', context=context)


def user_page(request):
    return render(request, 'user_page.html', {'menu': menu,
                                              'request': request})


def login(request):
    return render(request, 'registration/login.html', {'menu': menu,
                                          'title': 'Войти',
                                          'request': request})


class Register_user(View):
    form_class = RegisterUserForm()
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form_class = RegisterUserForm(request.POST)

        if form_class.is_valid():
            form_class.save()
            username = form_class.cleaned_data('username')
            password1 = form_class.cleaned_data('password1')
            password2 = form_class.cleaned_data('password2')
            user = authenticate(username=username, password=password1)
            dj_login(request, user)
            return redirect('login')
        else:
            print(form_class)

        context = {
            'form': form_class
        }
        return render(request, self.template_name, context)

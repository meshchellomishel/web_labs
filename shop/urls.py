from django.urls import path, re_path, include
import django.contrib.auth.urls

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('feedback/', feedback, name='feedback'),
    path('login/', include('django.contrib.auth.urls'), name='login'),
    path('register/', Register_user.as_view(), name='register'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('user_page/', user_page, name='user_page'),
]

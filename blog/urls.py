from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import profile




urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login_page, name = 'login'),
    path('logout/', views.logout_request, name="logout"),
    path('profile/', views.profile, name='profile'),
   
]
    
 
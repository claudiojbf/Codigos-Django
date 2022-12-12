from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('loguin', views.loguin, name='loguin'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logout', views.logout, name = 'logout')
]
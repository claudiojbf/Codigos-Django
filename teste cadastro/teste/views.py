from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Nivel

def inicio(request):
    usuario = request.user.id
    nivel = Nivel.objects.filter(usuario_id = usuario)
    if nivel is not None:
        return render(request, 'index.html',{'nivel' : nivel})
    return render(request, 'index.html')

def loguin(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if User.objects.filter(email = email).exists():
            nome = User.objects.filter(email = email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username = nome, password = senha)
            if user is not None:
                auth.login(request, user)
                return redirect('inicio')
    return render(request, 'loguin.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome_usuario']
        email = request.POST['email']
        senha = request.POST['senha']
        tipo = request.POST['nivel']
        user = User.objects.create_user(username = nome, email = email, password = senha)
        user.save()
        user_id = User.objects.get(email = email)
        user_n = get_object_or_404(User, pk = user_id.id)
        nivel = Nivel.objects.create(usuario = user_n, status = tipo)
        nivel.save()
        return redirect('loguin')
    return render(request, 'cadastro.html')

def logout(request):
    auth.logout(request)
    return redirect('inicio')
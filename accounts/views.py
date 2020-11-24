from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout


def register_func(request):
    if request.method == 'POST':
        temp_username = request.POST['username']
        temp_password = request.POST['password']
        try:
            User.objects.get(username=temp_username)
            return render(request, 'accounts/register.html', {'error': 'このユーザーは登録されています'})
        except:
            User.objects.create_user(temp_username, '', temp_password)
            return render(request, 'accounts/register.html')
    else:
        return render(request, 'accounts/register.html')


def login_func(request):
    if request.method == 'POST':
        temp_username = request.POST['username']
        temp_password = request.POST['password']
        user = authenticate(request, username=temp_username, password=temp_password)
        if user is not None:
            login(request, user)
            return redirect('/accounts/register')
        else:
            return redirect('/accounts/login')
    else:
        return render(request, 'accounts/login.html')
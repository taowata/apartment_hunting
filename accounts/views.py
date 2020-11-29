from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
import uuid


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


def guest_login_func(request):
    temp_username = "guest_" + str(uuid.uuid4())
    temp_password = "guest"
    User.objects.create_user(temp_username, '', temp_password)
    user = authenticate(request, username=temp_username, password=temp_password)
    login(request, user)
    return redirect('/apartment/list')


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


def logout_func(request):
    logout(request)
    return render(request, 'accounts/logout.html')
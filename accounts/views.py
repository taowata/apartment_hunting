from django.shortcuts import render, redirect
from .models import User
from apartment.models import Apartment
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
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
            return redirect('/accounts/login')
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
            return redirect('/apartment/list')
        else:
            return redirect('/accounts/login')
    else:
        return render(request, 'accounts/login.html')


def logout_func(request):
    logout(request)
    return render(request, 'accounts/logout.html')


@csrf_exempt
def add_favorite_apartment_func(request):
    print("wellcom to api")
    response = HttpResponse()
    parameter = request.GET
    print(parameter)
    try:
        user = User.objects.get(id=request.GET.get('user_id'))
        apartment = Apartment.objects.get(id=request.GET.get('apartment_id'))
        user.favorite_apartment.add(apartment)
        print("succeeded")
    except:
        response.write("error: failed to remove favorite apartment")
        print("failed!")
        print("user-id: ")
        print(str(request.GET.get('user_id')))
        print("apartment-id: ")
        print(str(request.GET.get('apartment_id')))
    return response


def remove_favorite_apartment_func(request):
    print("wellcom to api")
    response = HttpResponse()
    try:
        user = User.objects.get(id=request.headers['user_id'])
        apartment = Apartment.objects.get(id=request.headers['apartment_id'])
        user.favorite_apartment.remove(apartment)
        print("succeeded")
    except:
        response.write("error: failed to remove favorite apartment")
        print("failed!")
        print("user-id: ")
        print(request.headers['user_id'])
        print("apartment-id: ")
        print(request.headers['apartment_id'])
    return response

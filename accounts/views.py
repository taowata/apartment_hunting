from django.shortcuts import render, redirect
from .models import User
from apartment.models import Apartment
from django.contrib.auth import authenticate, login, logout
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


def add_favorite_apartment_func(request):
    try:
        user = User.objects.get(id=request.GET.get('user_id'))
        apartment = Apartment.objects.get(id=request.GET.get('apartment_id'))
    except:
        print("error: failed to get user or apartment")
        return HttpResponse("error: failed to get user or apartment")
    try:
        user.favorite_apartment.add(apartment)
    except:
        print("error: failed to add favorite apartment")
        return HttpResponse("error: failed to add favorite apartment")
    try:
        apartment.goodNumber = apartment.user_set.all().count()
        apartment.save()
    except:
        print("error: failed to update Apartment.goodNumber")
        return HttpResponse("error: failed to update Apartment.goodNumber")
    print("succeeded")
    return HttpResponse("succeeded")


def remove_favorite_apartment_func(request):
    try:
        user = User.objects.get(id=request.GET.get('user_id'))
        apartment = Apartment.objects.get(id=request.GET.get('apartment_id'))
    except:
        print("error: failed to get user or apartment")
        return HttpResponse("error: failed to get user or apartment")
    try:
        user.favorite_apartment.remove(apartment)
    except:
        print("error: failed to remove favorite apartment")
        return HttpResponse("error: failed to remove favorite apartment")
    try:
        apartment.goodNumber = apartment.user_set.all().count()
        apartment.save()
    except:
        print("error: failed to update Apartment.goodNumber")
        return HttpResponse("error: failed to update Apartment.goodNumber")
    print("succeeded")
    return HttpResponse("succeeded")

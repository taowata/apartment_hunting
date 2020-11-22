from django.shortcuts import render
from .models import User


def registerfunc(request):
    if request.method == 'POST':
        temp_username = request.POST['username']
        temp_password = request.POST['password']
        try:
            User.objects.get(username=temp_username)
            return render(request, 'accounts/register.html', {'error': 'このユーザーは登録されています'})
        except:
            User.objects.create_user(temp_username, '', temp_password)
            return render(request, 'accounts/register.html', {'some': 100})
    else:
        return render(request, 'accounts/register.html', {'some': 100})

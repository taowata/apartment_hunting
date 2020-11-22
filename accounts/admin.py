from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('favorite_apartment',)}),)
    list_display = ['username', 'email']


admin.site.register(User, CustomUserAdmin)

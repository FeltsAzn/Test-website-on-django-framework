from django.shortcuts import render
from django.views import View

from .models import User


# Create your views here.


class UsersView(View):
    """Список посетителей сайта"""
    def get(self, request):
        user = User.objects.all()
        return render(request, 'users/users_list.html', {"users_list": user})

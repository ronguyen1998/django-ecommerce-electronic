import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from core.models import CustomUser
# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')
    def post(self, request):
        email = request.POST.get('email')
        username = CustomUser.objects.get(email=email.lower()).username
        password = request.POST.get('password')
        next_url = request.POST.get('next_url')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_lock:
            context = {
                'username':username,
                'message':'Tài khoản của bạn tạm thời bị khóa, vui lòng liên hệ Admin'
            }
            return render(request, 'auth/login.html', context)
        login(request, user)
        if next_url:
            return HttpResponseRedirect(next_url)
        elif request.user.is_superuser:
            return HttpResponseRedirect('/admin')

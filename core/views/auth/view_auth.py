import re
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from core.models import CustomUser
# Create your views here.

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'auth/login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next_url','')
        user = authenticate(request, username=username, password=password)
        if (user is not None):
            if (user.is_lock):
                context = {
                    'old_user':username,
                    'message':'Tài khoản của bạn tạm thời bị khóa, vui lòng liên hệ Admin'
                }
                return render(request, 'auth/login.html', context)
            login(request, user)
            if next_url:
                return HttpResponseRedirect(next_url)
            elif request.user.is_superuser:
                return HttpResponseRedirect('/admin')
        else:
            context = {
                'username':username,
                'message':'Tài khoản hoặc mật khẩu không đúng'
            }
            return render(request, 'auth/login.html', context)
        

def Logout(request):
    logout(request)
    return redirect('home')
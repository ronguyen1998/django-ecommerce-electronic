from multiprocessing import context
import re
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from core.models import CustomUser
from core.forms import NewUserForm
# Create your views here.

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'auth/login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if (user is not None):
            if (user.is_lock):
                context = {
                    'old_user':username,
                    'message':'Tài khoản của bạn tạm thời bị khóa, vui lòng liên hệ Admin'
                }
                return render(request, 'auth/login.html', context)
            login(request, user)
            if request.user.is_superuser:
                return HttpResponseRedirect('/admin')
            else:
                return redirect('home')
        else:
            context = {
                'username':username,
                'message':'Tài khoản hoặc mật khẩu không đúng'
            }
            return render(request, 'auth/login.html', context)
        

def Logout(request):
    logout(request)
    return redirect('home')


class SigupView(View):
    def get(self,request):
        form = NewUserForm()
        context = {
            'form':form,
        }
        return render(request, 'auth/sigup.html',context)
    def post(self, request):
        forms = NewUserForm(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password1 = forms.cleaned_data['password1']
            password2 = forms.cleaned_data['password2']
            if password1 == password2 :
                if CustomUser.objects.filter(email=email).exists():
                    context = {
                        'form':forms,
                        'message':'Email đã tồn tại'
                    }
                    return render(request, 'auth/sigup.html', context)
                elif CustomUser.objects.filter(username=username).exists():
                    context = {
                        'form':forms,
                        'message':'Username đã tồn tại'
                    }
                    return render(request, 'auth/sigup.html', context)
                else:
                    newuser = forms.save()
                    login(request,newuser)
                    return redirect('home')
            else:
                context = {
                        'form':forms,
                        'message':'Mật khẩu không trùng khớp'
                    }
                return render(request, 'auth/sigup.html', context)
        else:
            
            context = {
                'message':"Đăng ký không thành công. Thông tin không hợp lệ."
            }
            return render(request,'auth/sigup.html', context)
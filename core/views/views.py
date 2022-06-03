from django.http import JsonResponse
from django.views import View
from django.shortcuts import render

from core.forms import ContactForm
import json

class ContactView(View):
    def get(self,request):
        return render(request,'contact/index.html')
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save()
            data_contact = {
                'result':'success',
                'message':form.cleaned_data['name']
            }
            return JsonResponse(data_contact,status=200)
        data_contact = {
            'result':'error',
            'message':json.dumps(form.errors)
        }
        return JsonResponse(data_contact, status = 400)
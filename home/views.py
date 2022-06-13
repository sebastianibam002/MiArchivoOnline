from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django import forms
from .forms import FileForm
from .models import UploadedFile
from datetime import date
from .filesTools import generateUrl

# Create your views here.

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def index(request):
    form = FileForm(request.POST or None,  request.FILES or None)
    share_link = ""
    if is_ajax(request):
        print("Form Errors")
        print(form.errors)  
        if form.is_valid():
            print("form is valid")
            send_email = form.cleaned_data['user_email']
            dest_email =  form.cleaned_data['dest_email']
            generated_url = generateUrl()
            share_link = f"http://82.180.160.116/myfile/{generated_url}"
            # instance = UploadedFile(unique_link=generated_url, file=request.FILES['file'], date_sent=date.today())
            instance = UploadedFile(file=request.FILES['file'], user_email=send_email, dest_email=dest_email, unique_link=generated_url,  date_sent=date.today())
            instance.save()
            return JsonResponse({'link': share_link })
            
    return render(request, "home/home.html", {
        "form": FileForm,
        "link": share_link
    })

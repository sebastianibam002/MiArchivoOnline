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
   
    if is_ajax(request):
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'worked'})

    return render(request, "home/home.html", {
        "form": FileForm,
    })

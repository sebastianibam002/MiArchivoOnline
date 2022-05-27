from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import FileForm
from .models import UploadedFile
from datetime import date
from .filesTools import generateUrl

# Create your views here.

def index(request):
    if request.method == "POST":
         # Take in the data the user submitted and save it as form
        form = FileForm(request.POST, request.FILES)
        # Check if form data is valid (server-side)
        if form.is_valid():
            # Isolate the task from the 'cleaned' version of form data
            user_email = form.cleaned_data["user_email"]
            send_email = form.cleaned_data["send_email"]
            note = form.cleaned_data['note']
            # Create an url to access the file later that is different from the previous ones
            generated_url = generateUrl()
            instance = UploadedFile(origin_email=user_email, destination_email=send_email, generated_url=generated_url, file=request.FILES['file'], date_sent=date.today())
            instance.save()
        else:
             # If the form is invalid, re-render the page with existing information.
            return render(request, "home/home.html", {
                "form": form
            })

    return render(request, "home/home.html", {
        "form": FileForm()
    })

def handle_uploaded_file(f):
    with open(f'home/files/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
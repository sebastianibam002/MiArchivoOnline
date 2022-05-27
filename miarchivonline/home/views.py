from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms

class FileForm(forms.Form):
    user_email = forms.EmailField(label="user")
    send_email = forms.EmailField(label="receiver")
    file = forms.FileField()


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
            handle_uploaded_file(request.FILES['file'])
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
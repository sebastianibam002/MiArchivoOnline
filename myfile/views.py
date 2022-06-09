from django.shortcuts import render
from home.models import UploadedFile
# Create your views here.


def index(request, name):
    return render(request, "myfile/myfile.html", {
        "source": getFileLink(name)
    })


"""
Returns the real name of the file
"""
def getFileLink(code: str) -> str:
    name = UploadedFile.objects.filter(generated_url= code)
    if name.exists():
        return name[0].file

from django.urls import path
from . import views


app_name = "myfile"
urlpatterns = [
     #path("", views.index, name="index")
     path("<str:name>", views.index, name="index")

 ]
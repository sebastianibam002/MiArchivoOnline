from operator import mod
from django.db import models

# Create your models here.

"""
This model is in charge of connecting the file with the person who send it
and the person who is going to receive the email with the file
"""
class UploadedFile(models.Model):
    origin_email = models.EmailField()
    destination_email = models.EmailField()
    generated_url = models.CharField(max_length=50)
    # date which is sent
    date_sent = models.DateField()
    file = models.FileField()

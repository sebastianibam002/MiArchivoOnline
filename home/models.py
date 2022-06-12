from operator import mod
from statistics import mode
from django.db import models

# Create your models here.

"""
This model is in charge of connecting the file with the person who send it
and the person who is going to receive the email with the file
"""
class UploadedFile(models.Model):
    user_email = models.EmailField()
    dest_email = models.EmailField()
    file = models.FileField()
    unique_link = models.CharField(max_length=50)
    date_sent = models.DateField()
    def __str__(self):
        return str(self.pk)
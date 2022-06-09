from operator import mod
from django.db import models

# Create your models here.

"""
This model is in charge of connecting the file with the person who send it
and the person who is going to receive the email with the file
"""
class UploadedFile(models.Model):
    file = models.FileField()
    def __str__(self):
        return str(self.pk)
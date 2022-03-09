from unicodedata import name
from django.db import models

# Create your models here.
class store(models.Model):

    name=models.TextField(max_length=20)
    lname=models.TextField(max_length=20)
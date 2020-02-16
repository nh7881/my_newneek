from django.db import models

# Create your models here.

class User(models.Model) :
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    major = models.CharField(max_length = 50)
    create_date = models.DateTimeField('date published')
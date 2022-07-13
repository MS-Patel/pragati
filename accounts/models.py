from django.db import models
from django.contrib.auth.models import AbstractUser

class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username =  models.CharField(max_length=100)
    password =  models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    email =  models.EmailField(max_length=256)

    def __str__(self):
        return self.username
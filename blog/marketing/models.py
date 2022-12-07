from django.db import models

# Create your models here.
class Signup(models.Model):
    email = models.EmailField()
    datetime = models.DateTimeField(auto_now=True)
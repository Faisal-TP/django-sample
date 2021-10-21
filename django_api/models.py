from django.db import models

# Create your models here.
class Register_api(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    gender=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
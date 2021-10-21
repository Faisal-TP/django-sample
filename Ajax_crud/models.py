from django.db import models

# Create your models here.
class Registerajax(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    gender=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class AjaxFileUpd(models.Model):
    name = models.CharField(max_length=30)
    file=models.CharField(max_length=100)

from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    gender=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Profile(models.Model):
	user_id = models.ForeignKey(Register,on_delete=models.CASCADE)
	image = models.CharField(max_length=100)
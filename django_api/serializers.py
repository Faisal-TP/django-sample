from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Register_api
		# fields=('name','address','contact','gender','email')
		fields='__all__'

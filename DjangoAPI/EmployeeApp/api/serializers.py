from dataclasses import fields
from rest_framework import serializers
from EmployeeApp.models import Activity,Product,Profile

from django.contrib.auth.models import User 
from  rest_framework.authtoken.models import Token


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model= User
        # fields= ['id', 'username', 'password']
        fields= '__all__'
        # extra_kwargs={'password': {'write_only': True, 'required':True}}
    def create(self, validated_data):
        user= User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class Departmentserializer(serializers.ModelSerializer):
    class Meta:
        model=Activity
        fields=('DepartmentName')
class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('user','value','contact','gender','blood','profession','address')
class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('PId','PName','Description','Price','DateOfJoining','ClosingDate')
        # read_only_fields = ['PId']
    
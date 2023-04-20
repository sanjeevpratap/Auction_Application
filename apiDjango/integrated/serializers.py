from rest_framework import serializers
from integrated.models import Departments


class Departmentserializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId','DepartmentName')
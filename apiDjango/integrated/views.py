from django.shortcuts import render

# Create your views here.
from integrated.models import Departments
from integrated.serializers import Departmentserializer
# Create your views here.

from rest_framework.generics import ListAPIView,RetrieveAPIView

class DempartmentsListview(ListAPIView):
    queryset=Departments.objects.all()
    serializer_class=Departmentserializer
class DempartmentsDetailview(RetrieveAPIView):
    queryset=Departments.objects.all()
    serializer_class=Departmentserializer
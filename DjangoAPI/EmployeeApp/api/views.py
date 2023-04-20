# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse

from EmployeeApp.models import Product
from EmployeeApp.models import Activity,Profile
from .serializers import Departmentserializer,Productserializer,Userserializer,Profileserializer
# Create your views here.

from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})
class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = Userserializer
class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset= Activity.objects.all()
    serializer_class = Departmentserializer
    authentication_classes=[TokenAuthentication, ]
    permission_classes=[IsAuthenticated, ]

class ProfileListview(ListAPIView):
    queryset=Profile.objects.all()
    serializer_class=Profileserializer

class ProfileCreateview(CreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=Profileserializer
class ProfileUpdateview(UpdateAPIView ):
    queryset=Profile.objects.all()
    serializer_class=Profileserializer
class DempartmentsListview(ListAPIView):
    queryset=Activity.objects.all()
    serializer_class=Departmentserializer
class DempartmentsDetailview(RetrieveAPIView):
    queryset=Activity.objects.all()
    serializer_class=Departmentserializer
class DempartmentsCreateview(CreateAPIView):
    queryset=Activity.objects.all()
    serializer_class=Departmentserializer
    authentication_classes=[TokenAuthentication, ]
    permission_classes=[IsAuthenticated, ]
class DempartmentsUpdateview(UpdateAPIView ):
    queryset=Activity.objects.all()
    serializer_class=Departmentserializer

class ProductListview(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer
class ProductCreateview(CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer
class ProductUpdateview(UpdateAPIView ):
    queryset=Product.objects.all()
    serializer_class=Productserializer


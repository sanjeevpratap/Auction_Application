"""DjangoAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from EmployeeApp.api.views import DempartmentsDetailview,DempartmentsListview,ProductListview,ProductUpdateview,ProductCreateview,DempartmentsCreateview,DempartmentsUpdateview
from EmployeeApp.api.views import ProfileCreateview,ProfileListview,ProfileUpdateview
from EmployeeApp.api.views import UserViewSet,DepartmentsViewSet,CustomObtainAuthToken
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register('users', UserViewSet)
# router.register('Activity', DepartmentsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    # path('auth/', obtain_auth_token),
    path('auth/', CustomObtainAuthToken.as_view()),
    path('Dept', DempartmentsListview.as_view()),
    path('<pk>Det', DempartmentsDetailview.as_view()),
    path('create/', DempartmentsCreateview.as_view()),
    path('<pk>/update/', DempartmentsUpdateview.as_view()),

    path('PList/', ProductListview.as_view()),
    
    path('PCreate/', ProductCreateview.as_view()),
    path('PUpdate/', ProductUpdateview.as_view()),

    path('api-auth/', include('rest_framework.urls')),
    
    path('Profile/', ProfileListview.as_view()),
    path('<pk>/profill/', ProfileUpdateview.as_view()),
    path('ProfileCreate/', ProfileCreateview.as_view()),

    #  path('/',include(EmployeeApp.urls))
]

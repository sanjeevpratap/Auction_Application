from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
# from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    # user = models.OneToOneField(User,  on_delete=models.CASCADE)
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    # DepartmentName = models.CharField(max_length=500,)
    # avatar = models.ImageField(default="7.jpg")
    # bio = models.TextField()
    value = models.CharField(max_length=500 ,default='bio..')
    gender = models.CharField(max_length=10,default='XYZ')
    blood = models.CharField(max_length=5,default='x+')
    profession = models.CharField(max_length=20,default='others')
    address = models.CharField(max_length=200,default='Mars')
    contact=models.IntegerField(unique=True,default=123)
    # cart_products = models.ArrayField(
    #     models.IntegerField(blank=True),
    #     default = list
    # )
   
    # value=models.IntegerField(unique=True,default=99)
    

    def __str__(self):
        return self.user.username
    # class Meta:
    #     # managed = False
    #     db_table = 'Profile'
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
        

class Activity(models.Model):
    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    DepartmentId = models.IntegerField(default=0)
    # DepartmentName = models.CharField(max_length=500)
    # bio = models.TextField()
     # BuyId = models.IntegerField(unique=True, default=0)
    # SellId= models.ImageField(unique=True ,default=0)
    # WatchListId = models.IntegerField(unique=True, default=0)
    # def __str__(self):
    #     return self.DepartmentName
    # class Meta:
    #     db_table='Department_Description'


class Product(models.Model):
    PId = models.AutoField(primary_key=True)
    PName = models.CharField(max_length=500 , default="name")
    Description = models.CharField(max_length=500,default="hello")
    DateOfJoining = models.CharField(max_length=50,default='')
    PhotoFileName = models.CharField(max_length=500,default="photoname") 
    Price= models.IntegerField(default=0)
    ClosingDate=models.CharField(max_length=50,default='')
    def __str__(self):
        return self.PName
   




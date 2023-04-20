from django.contrib import admin

# Register your models here.

 
# Register your models here.
from .models import Activity,Product,Profile
 
admin.site.register(Activity)

admin.site.register(Product)
admin.site.register(Profile)
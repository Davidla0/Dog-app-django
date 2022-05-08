from django.contrib import admin
from .models import Category, Photo

# Register your models here.

admin.site.register(Category)  
admin.site.register(Photo)   


Photo.objects.all().delete()
Category.objects.all().delete()
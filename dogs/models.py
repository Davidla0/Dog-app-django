import json
from pyexpat import model
from tkinter import image_names
from django.db import models
from matplotlib import image
from numpy import blackman
import requests
from sqlalchemy import null

# Create your models here.


class Category(models.Model):
    name = models.CharField( max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null= False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description

    


    


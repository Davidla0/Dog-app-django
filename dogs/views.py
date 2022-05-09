import itertools
from random import random, randrange
from tkinter import image_names
from turtle import update
from django.shortcuts import render
from matplotlib import image
from matplotlib.style import context
import pkg_resources
import requests, json

import dogs

from .models import Category, Photo
from dogs import models
# Create your views here.




def MainView(request):
    categories = Category.objects.all()
    photo = Photo.objects.all()
    context = {
        'categories': categories,
        'photo': photo
        }
    return render(request, 'gallery.html', context)


def ViewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {'photo': photo})


def addPhoto(request):
    categories = Category.objects.all()
    photo = Photo.objects.all()
    print(len(photo))
    if (len(photo) < 172):

        response = requests.get('https://api.thedogapi.com/v1/breeds')
        response_json = (json.loads(response.text))
        images_list = [d['image']['url'] for d in response_json]
        name_list = [d['name'] for d in response_json]

        category = Category.objects.get(name='Dogs')
        for i in range(len(images_list)):
            Photo.objects.filter(id=i).create(image=images_list[i - 1], description=name_list[i - 1], category=category)

    context={'categories': categories, 'photo': photo}
    return render(request, 'Dogs.html', context)


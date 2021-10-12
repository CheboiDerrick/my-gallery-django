from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.

def all_images(request):
    
    categories= Category.objects.all()
    locations= Location.objects.all()
    images=Image.objects.all()
    return render(request, 'gallery/home.html', {'images':images, 'categories':categories,'locations':locations})

def category_images(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/category.html',{"message":message,"images": images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/category.html',{"message":message})

def views_images(request, category):
    categories= Category.objects.all()
    locations= Location.objects.all()
    images = Image.objects.filter(category__name=category)
    return render(request, 'gallery/category.html',{"category":category,"images": images,'categories':categories,'locations':locations})

def views_location(request, location):
    categories= Category.objects.all()
    locations= Location.objects.all()
    images = Image.objects.filter(location__name=location)
    return render(request, 'gallery/location.html',{"category":location,"images": images,'categories':categories, 'locations':locations, 'location':location})



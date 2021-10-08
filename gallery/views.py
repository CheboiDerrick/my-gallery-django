from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Image

# Create your views here.

def all_images(request):
    images=Image.objects.all()
    return render(request, 'gallery/home.html', {'images':images})

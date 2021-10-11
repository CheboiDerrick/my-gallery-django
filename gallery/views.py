from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Image

# Create your views here.

def all_images(request):
    images=Image.objects.all()
    return render(request, 'gallery/home.html', {'images':images})

def category_images(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/category.html',{"message":message,"images": images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/category.html',{"message":message})

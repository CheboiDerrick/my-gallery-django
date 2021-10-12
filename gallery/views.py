from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Image

# Create your views here.

def all_images(request):
    
    categories= Image.objects.distinct().values_list('category__name', flat=True)
    # categories = [r for (r,) in categories]

    images=Image.objects.all()
    return render(request, 'gallery/home.html', {'images':images, 'categories':categories})

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
    categories= Image.objects.distinct().values_list('category__name', flat=True)
    images = Image.objects.filter(category__name=category)
    return render(request, 'gallery/category.html',{"category":category,"images": images,'categories':categories})



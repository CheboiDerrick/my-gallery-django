from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()


    def delete_locations(self):
        self.delete()


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = CloudinaryField ('photo_gallery')
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, default=None)
    category = models.ManyToManyField(Category)
    post_time= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-post_time']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location=location)
        return images

    @classmethod
    def view_by_category(cls, category):
        images=cls.objects.filter

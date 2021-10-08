from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='photo_gallery/', default=None)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, default=None)
    category = models.ManyToManyField(Category)

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
        images = cls.objects.filter(category=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location=location)
        return images

from distutils.command.upload import upload
from unicodedata import category
from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'category/{filename}'.format(filename=filename)

class Category(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Person(models.Model):
    category = models.ForeignKey(Category, null=False, default=1, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Subcategory, null=False, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=125, blank=False, null=False)
    number = models.CharField(max_length=16, blank=False, null=False)
    rank = models.CharField(max_length=75, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    
from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.db.models.fields import SlugField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    desc = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product_id = ForeignKey(Product, on_delete=CASCADE)
    def __str__(self):
        return self.product_id.title + " image " +str(self.pk)

class Header(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50, blank=True)
    text = models.CharField(max_length=400, blank=True)
    image = models.ImageField(upload_to='images/header')

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu',on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    name        = models.CharField(max_length=100)
    category    = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'


class Allergen(models.Model):
    name        = models.CharField(max_length=20)

    class Meta:
        db_table = 'allergens'

class Image_URL(models.Model):
    image_url   = models.CharField(max_length=400)
    drink       = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'image_urls'

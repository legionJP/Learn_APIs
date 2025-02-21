from django.db import models

# Create your models here.

class Category(models.Model):
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=255)


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price =models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1) # on_delete=models.PROTECT means that if a category is deleted, all the menu items in that category will be protected from deletion.
    created_at = models.DateTimeField(auto_now_add=True)




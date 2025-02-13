from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(primary_key=True,max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=3)
    inventory = models.CharField(max_length=255, default='Book')

    class Meta:
        indexes = [models.Index(fields=['price'])]


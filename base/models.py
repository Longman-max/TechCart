from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField(null=True, blank=True, default=0)
    description = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=2083, null=True, blank=True)


    def __str__(self):
        return self.name
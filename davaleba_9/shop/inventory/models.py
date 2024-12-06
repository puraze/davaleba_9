from django.db import models

class category(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField()
    stock_quanity = models.IntegerField()
    rating = models.DecimalField()
    category = models.ForeignKey(category, related_name='products', on_delete=models.CASCADE)
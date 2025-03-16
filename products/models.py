from django.db import models
 
class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=245)
    base_price = models.DecimalField(decimal_places=2, max_digits=12)
    sort_order = models.IntegerField()

class Image(models.Model):
    file = models.CharField(max_length=145)
    tooltip = models.CharField(max_length=45)
    sort_order = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    
class Parameter(models.Model):
    name = models.CharField(max_length=45)
    value = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    sort_order = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
from django.db import models

# Create your models here.
class ProductDB(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Size = models.CharField(max_length=100, null=True, blank=True)
    Color = models.CharField(max_length=100, null=True, blank=True)
    Status = models.CharField(max_length=100, null=True, blank=True)


class OrderDB(models.Model):
    ProductId = models.ForeignKey(ProductDB, on_delete=models.CASCADE)
    Quantity = models.IntegerField(null=True, blank=True)

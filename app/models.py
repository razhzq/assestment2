from django.db import models
from django.db.models.fields import FloatField

class Order(models.Model):
    item_name = models.IntegerField()
    item_vendor = models.CharField(max_length=200)
    total_amount = models.FloatField()
    total_price = models.FloatField()

    def __str__(self):
        return self.total_amount

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.DecimalField(decimal_places=2, max_digits=8)
    item_vendor = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name



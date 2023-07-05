from django.db import models
from demo_app.models import *
from tkinter import CASCADE
from django.contrib.auth.models import User


# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    PAYMENT=(
        ('Cash on Delivery','Cash on Delivery'),
        ('esewa','esewa')
            
         )

    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    total_price = models.IntegerField()
    status = models.CharField(default='Pending',max_length=100,null=True)
    payment_method = models.CharField(max_length=100,choices=PAYMENT)
    payment_status = models.BooleanField(default=False, null=True)
    contact_no = models.CharField(max_length=14)
    address = models.CharField(max_length=100)
    Order_date = models.DateTimeField(auto_now=True)


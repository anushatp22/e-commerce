from django.db import models

class register_seller_tb(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Dob=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Phone=models.CharField(max_length=20)
    Country=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    Image=models.FileField()
    Status=models.CharField(max_length=20, default='pending')
class product_tb(models.Model):
    product=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.FileField()
    details=models.CharField(max_length=20)
    stock=models.CharField(max_length=20)
    category=models.ForeignKey('siteadmin.Category_tb', on_delete=models.CASCADE)
    seller=models.ForeignKey(register_seller_tb, on_delete=models.CASCADE)
class tracking_tb(models.Model):
    orderid=models.ForeignKey('buyer.order_tb', on_delete=models.CASCADE)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    details=models.CharField(max_length=20)


    

# Create your models here.

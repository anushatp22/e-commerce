from django.db import models

class register_tb(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Dob=models.CharField(max_length=20)
    Phone=models.CharField(max_length=20)
    Country=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
class cart_tb(models.Model):
    Name=models.CharField(max_length=20)
    Shipping_address=models.CharField(max_length=20)
    Phone=models.IntegerField()
    Quantity=models.IntegerField()
    Total_price=models.IntegerField()
    Productid=models.ForeignKey('seller.product_tb', on_delete=models.CASCADE)
    Buyerid=models.ForeignKey(register_tb, on_delete=models.CASCADE)
class order_tb(models.Model):
    shippingaddress=models.CharField(max_length=20)
    quantity=models.IntegerField()
    phone=models.IntegerField()
    stock=models.CharField(max_length=20)
    totalprice=models.IntegerField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    Status=models.CharField(max_length=20, default='pending')
    buyerid=models.ForeignKey(register_tb, on_delete=models.CASCADE)
    productid=models.ForeignKey('seller.product_tb', on_delete=models.CASCADE)
    sellerid=models.ForeignKey('seller.register_seller_tb', on_delete=models.CASCADE)
    

    

# Create your models here.

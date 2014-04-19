from django.db import models
from Users.models import Customer
from product.models import Product

class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True, max_length=10)
    PaymentType = models.CharField(max_length=50)
    Allowed = models.BooleanField()

class Shipper(models.Model):
    ShipperID = models.AutoField(primary_key=True, max_length=10)
    ShipperName = models.CharField(max_length=100)
    Phone = models.IntegerField(max_length=12)

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True, max_length=10)
    CustomerID = models.ForeignKey(Customer)
    OrderNumber = models.CharField(max_length=10)
    PaymentID = models.ForeignKey(Payment)
    OrderDate = models.DateField()
    ShipDate = models.DateField()
    RequiredDate = models.DateField()
    ShipperID = models.ForeignKey(Shipper)
    Freight = models.FloatField(max_length=10)
    Sales_tax= models.FloatField(max_length=5)
    Timestamp = models.CharField(max_length=50)
    TransactStatus = models.CharField(max_length=100)
    ErrLoc = models.CharField(max_length=100)
    Errmsg = models.CharField(max_length=200)
    Fullfilled = models.BooleanField()
    Deleted = models.BooleanField()
    Paid = models.FloatField(max_length=10)
    PaymentDate = models.DateField()
    
class OrderDetail(models.Model):
    OrderDetailID = models.AutoField(primary_key=True, max_length=10)
    OrderId = models.ForeignKey(Order)
    ProductID = models.ForeignKey(Product)
    Price = models.FloatField(max_length=10)
    Quantity = models.IntegerField(max_length=2)
    Discount = models.FloatField(max_length=4)
    Total = models.FloatField(max_length=10)
    Size = models.IntegerField(max_length=2)
    Color = models.CharField(max_length=20)
    Fulfilled = models.BooleanField()
    BillDate = models.DateField()
    ShipDate = models.DateField()
    ShipperID = models.ForeignKey(Shipper)
    Freight = models.FloatField(max_length=10)
    SaleTax = models.FloatField(max_length=10)
    
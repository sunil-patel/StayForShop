from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True, max_length=10, null=False, blank=False, db_index=True)
    ID = models.ForeignKey(User)
    Address1 = models.CharField(max_length=200, null=True)
    Address2 = models.CharField(max_length=200, null=True)
    City = models.CharField(max_length=100, null=True)
    PostalCode = models.IntegerField(null=True)
    State = models.CharField(max_length=100, null=True)
    Country =  models.CharField(max_length=100, null=True)
    Phone = models.CharField(max_length=10, null=True)
    CreditCard = models.CharField(max_length=12, null=True)
    CreditCardTypeID = models.CharField(max_length=10, null=True)
    CardExpMo = models.IntegerField(null=True)
    CardExpYr = models.IntegerField(null=True)
    BillingAddress = models.CharField(max_length=400, null=True)
    BillingCity = models.CharField(max_length=100, null=True)
    BillingRegion = models.CharField(max_length=100, null=True)
    BillingPostalCode = models.IntegerField(null=True)
    BillingCountry = models.CharField(max_length=100, null=True)
    ShipAdress = models.CharField(max_length=400, null=True)
    ShipCity = models.CharField(max_length=100, null=True)
    ShipRegion = models.CharField(max_length=100, null=True)
    ShipPostalCode = models.IntegerField(null=True)
    ShipCountry = models.CharField(max_length=100, null=True)
    DateEntered = models.DateField()
    
    
    

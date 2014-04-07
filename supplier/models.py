from django.db import models
from django.utils.translation import ugettext as _

class Supplier(models.Model):
    SupplierID = models.AutoField(primary_key=True, max_length=10, null=False, blank=False, db_index=True)
    CompanyName = models.CharField(max_length=50)
    ContactFName = models.CharField(max_length=50)
    ContactLName = models.CharField(max_length=50)
    ContactTitle = models.CharField(max_length=10)
    Address1 = models.CharField(max_length=50)
    Address2 = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    PostalCode = models.CharField(max_length=15)
    Country = models.CharField(max_length=25)
    Phone = models.CharField(max_length=15)
    Fax = models.CharField(max_length=15)
    Email = models.CharField(max_length=50)
    URL = models.CharField(max_length=100)
    PaymentMethod = models.CharField(max_length=100)
    DiscountType = models.CharField(max_length=100)
    TypeGoods = models.CharField(max_length=255)
    DiscountAvailable = models.BooleanField(default=False)
    CurrentOrder = models.BooleanField(default=True)
    CustomerID = models.CharField(max_length=50)
    SizeURL = models.CharField(max_length=100)
    #LOGO = models.CharField(max_length=100)
    LOGO = models.ImageField(upload_to="Images/shoes")
    Ranking = models.IntegerField(max_length=10)
    Note = models.CharField(max_length=255)    
    
    def __unicode__(self):
        return  self.CompanyName
    
    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Supplier")
        
        
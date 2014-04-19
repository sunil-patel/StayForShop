from django.db import models
from supplier.models import Supplier
# Create your models here.


class MainCategory(models.Model):
    MainCatID = models.AutoField(primary_key=True, max_length=10)
    CategoryName = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.CategoryName

class SubCategory(models.Model):
    SubCatID = models.AutoField(primary_key=True, max_length=10)
    MainCatID = models.ForeignKey(MainCategory)
    CategoryName = models.CharField(max_length=50)
    
    def __unicode__(self):
        return "%s %s" % (self.MainCatID.CategoryName, self.CategoryName)

class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True, max_length=10)
    MainCatID = models.ForeignKey(MainCategory)
    SubCatID = models.ForeignKey(SubCategory)
    CategoryName = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    Picture = models.ImageField(upload_to="Images/category")
    Active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.CategoryName

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True, max_length=10)
    SKU = models.CharField(max_length=50)
    PupplierProductID = models.CharField(max_length=50)
    ProductName = models.CharField(max_length=60)
    ProductDescription = models.CharField(max_length=255)
    SupplierID = models.ForeignKey(Supplier)
    CategoryID = models.ForeignKey(Category)
    QuantityPerUnit = models.IntegerField(max_length=10)
    UnitSize = models.CharField(max_length=20)
    UnitPrice = models.FloatField(max_length=10)
    MSRP = models.FloatField(max_length=10)
    AvailableSize = models.CharField(max_length=50)
    AvailableColors = models.CharField(max_length=100)
    SizeID = models.IntegerField(max_length=10)
    ColorID = models.IntegerField(max_length=10)
    Discount = models.FloatField(max_length=10)
    UnitWeight = models.FloatField(max_length=10)
    UnitsInStock = models.SmallIntegerField(max_length=5)
    UnitsOnOrder = models.SmallIntegerField(max_length=5)
    ReorderLevel = models.SmallIntegerField(max_length=5)
    ProductAvailable = models.BooleanField(default=True)
    DiscountAvailable = models.BooleanField(default=False)
    CurrentOrder = models.BooleanField(default=True)
    Picture = models.ImageField(upload_to="Images/product")
    Ranking = models.IntegerField(max_length=10)
    Note = models.CharField(max_length=255)
    
    
class ProductDetail(models.Model):
    ProductDetailID = models.AutoField(primary_key=True, max_length=10)
    ProductID = models.ForeignKey(Product)
    Color = models.CharField(max_length=20)
    Size = models.IntegerField(max_length=5)
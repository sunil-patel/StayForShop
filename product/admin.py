from django.contrib import admin
from product.models import Products, Categories

    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("CategoryID",
                     "CategoryName",
                     "Description",
                     "Picture",
                     "Active")

admin.site.register(Categories, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    
    list_display = ["ProductID",
                    "SKU",
                    "PupplierProductID",
                    "ProductName",
                    "ProductDescription",
                    "SupplierID",
                    "CategoryID",
                    "QuantityPerUnit",
                    "UnitSize",
                    "UnitPrice",
                    "MSRP",
                    "AvailableSize",
                    "AvailableColors",
                    "SizeID",
                    "ColorID",
                    "Discount",
                    "UnitWeight",
                    "UnitsInStock",
                    "UnitsOnOrder",
                    "ReorderLevel",
                    "ProductAvailable",
                    "DiscountAvailable",
                    "CurrentOrder",
                    "Picture",
                    "Ranking",
                    "Note"]
   
    
admin.site.register(Products, ProductAdmin)
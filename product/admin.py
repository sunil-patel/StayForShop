from django.contrib import admin
from product.models import Product, Category, MainCategory, SubCategory

class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ("MainCatID", "CategoryName")
    
admin.site.register(MainCategory, MainCategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("SubCatID", "MainCatID", "CategoryName")
    
admin.site.register(SubCategory, SubCategoryAdmin)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("CategoryID",
                     "CategoryName",
                     "Description",
                     "Picture",
                     "Active")

admin.site.register(Category, CategoryAdmin)


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
   
    
admin.site.register(Product, ProductAdmin)
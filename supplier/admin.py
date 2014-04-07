from django.contrib import admin
from supplier.models import Supplier

class SupplierAdmin(admin.ModelAdmin):
    list_display = ("SupplierID",
                    "CompanyName",
                    "ContactFName",
                    "ContactLName",
                    "ContactTitle",
                    "Address1",
                    "Address2",
                    "City",
                    "State",
                    "PostalCode",
                    "Country",
                    "Phone",
                    "Fax",
                    "Email",
                    "URL",
                    "PaymentMethod",
                    "DiscountType",
                    "TypeGoods",
                    "DiscountAvailable",
                    "CurrentOrder",
                    "CustomerID",
                    "SizeURL",
                    "LOGO",
                    "Ranking",
                    "Note")
                    
admin.site.register(Supplier, SupplierAdmin)
    
from django.contrib import admin
from Users.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    pass
    
    
admin.site.register(Customer)

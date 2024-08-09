from django.contrib import admin
from appnote1.models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Product)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'status', 'date_created']
admin.site.register(Order, OrderAdmin)
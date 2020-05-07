from django.contrib import admin
from .models import Product, Transaction, Company

# Register your models here.



class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'quantity']

class TransactionAdmin(admin.ModelAdmin):
	list_display = ['user','product', 'operation','timestamp','object_id', 'remarks']
	list_filter = ('product','timestamp',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Company)

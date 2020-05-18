from django.contrib import admin
from .models import Product, Transaction, Company, Customer, Damage_Product

# Register your models here.



class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'quantity']

class TransactionAdmin(admin.ModelAdmin):
	list_display = ['user','product', 'operation','timestamp','object_id', 'remarks']
	list_filter = ('product','timestamp',)


class DamageInline(admin.TabularInline):
	model = Damage_Product

class CustomerAdmin(admin.ModelAdmin):
	inlines = [DamageInline,]

admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Company)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Damage_Product)
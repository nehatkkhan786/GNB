from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name



class Product(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
	name = models.CharField(max_length=250)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	quantity = models.IntegerField(blank=True, null=True, default=0)

	def __str__(self):
		return self.name

	def decrement_quantity(self, count):
		self.quantity = self.quantity - count

	def increment_quantity(self, count):
		self.quantity = self.quantity + count

class Transaction(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	object_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	operation_choice = [
		('Added', 'Addition'),
		('Deleted', 'Deletion'),
	]
	operation = models.TextField(choices=operation_choice)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	in_stock = models.IntegerField(blank=True, null=True, default=0)
	remarks = models.CharField(max_length=1000, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now=True)


class Customer(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, editable=False)
	name = models.CharField(max_length=255, blank=True)
	firm_name = models.CharField(max_length=255, blank=True, null=True)
	phone = models.CharField(max_length=255, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	address = models.CharField(max_length=500, null=True, blank=True)
	created = models.DateTimeField(auto_now=True)
	remarks = models.CharField(max_length=500)


	def __str__(self):
		return self.name

class Damage_Product(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
	product = models.CharField(max_length=255)
	price = models.IntegerField(default=0)
	quantity = models.IntegerField(default=0)
	mfg = models.DateField()
	exp = models.DateField(blank=True, null=True)
	

	def __str__(self):
		return self.customer.name










































































	

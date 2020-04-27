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
	price = models.IntegerField()
	quantity = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.name

class Transaction(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	object_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	operation_choice = [
		(1, 'Addition'),
		(2, 'Deletion'),
	]
	operation = models.IntegerField(choices=operation_choice)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	remarks = models.CharField(max_length=1000, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now=True)

	
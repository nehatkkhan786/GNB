from django import forms
from .models import Product, Company

class AddProductForm(forms.ModelForm):
	class Meta:
		model= Product
		fields = ['company', 'name', 'price']

class AddCompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ['name']

		

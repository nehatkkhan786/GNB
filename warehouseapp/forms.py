from django import forms
from .models import Product, Company

class AddProductForm(forms.ModelForm):
	class Meta:
		model= Product
		fields = ['company', 'name', 'price']

	def __init__(self, user, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['company'].queryset = Company.objects.filter(user=user)

class AddCompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ['name']



		

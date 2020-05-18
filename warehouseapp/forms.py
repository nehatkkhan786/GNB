from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Product, Company, Customer, Damage_Product
from bootstrap_datepicker_plus import DatePickerInput





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

class AddCustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class DateInput(forms.DateInput):
	input_type = 'date'


class AddDamageForm(forms.ModelForm):
	class Meta:
		model = Damage_Product
		fields = '__all__'
		widgets = {'mfg':DateInput(), 'exp':DateInput()}



		

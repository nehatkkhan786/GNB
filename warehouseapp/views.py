from django.shortcuts import render, redirect
from .models import Product, Transaction
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddProductForm, AddCompanyForm
from django.contrib import messages


# Create your views here.

class Dashboard(View):
	def get(self, request, *args, **kwargs):
		products = Product.objects.filter(user=request.user)
		return render(request, 'home.html', {'products':products})


# @login_required()
# def homepage(request):
# 	products = Product.objects.filter(user=request.user)
# 	return render(request, 'home.html', {'products':products})



def add_quantity(request,pk):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=pk)
		quantity = request.POST.get('quantity')
		int_quantity = int(quantity)
		product.quantity += int_quantity
		product.save()
		updated_quantity = product.quantity

		new_transaction = Transaction.objects.create(
				#object_id = uuid.uuid4(),
				operation= 1, 
				product = product, 
				remarks = str(quantity) +' case has been added to the the stock by'

				
		)
		new_transaction.save()
		
		
		data = {
			'quantity':updated_quantity
		}
		
		return JsonResponse(data) 


def delete_quantity(request, pk):
	if request.method == 'POST':
		product = get_object_or_404(Product,pk=pk)
		quantity = request.POST.get('quantity')
		print (quantity)
		int_quantity = int(quantity)
		product.quantity -=int_quantity
		product.save()
		updated_quantity = product.quantity

		new_transaction = Transaction.objects.create(
			operation = 2,
			product = product,
			remarks = str(quantity) +' case has been deleted from the stock'
			)
		
		data = {
			'quantity':updated_quantity
		}
		return JsonResponse(data)



class AddProduct(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'add_product.html',{'form':AddProductForm,'form2':AddCompanyForm})

	def post(self, request, *args, **kwargs):
		form = AddProductForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			messages.success(request, 'Item Successfully Added')
			return redirect('warehouse:homepage')
		else:
			messages.error(request, 'Got some error')
			return redirect('warehouse:homepage')



class AddCompany(View):
	def post(self, request, *args, **kwargs):
		form = AddCompanyForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			messages.success(request, 'Comapany Successfully Added')
			return redirect('warehouse:add_product')
		else:
			messages.error(request,'Something went wrong')
			return redirect('warehouse:add_product')



def demo(request):
	return render(request, 'demo.html')





































































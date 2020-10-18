from django.shortcuts import render, redirect
from .models import Product, Transaction, Customer, Damage_Product
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from .forms import AddProductForm, AddCompanyForm, AddCustomerForm
from django.contrib import messages
from gnb.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.sessions.models import Session







# Create your views here.

class HomeView(View):
	def get(self, request, *args, **kwargs):
		if request.session.has_key('is_logedin'):
			return redirect('warehouse:dashboard')
		return render(request, 'home.html', {})


def Dashboard(request):
	products = Product.objects.filter(user=request.user)
	return render(request, 'dashboard.html', {'products':products})


class AddProduct(View):
	def get(self, request, *args, **kwargs):
		
		forms = AddProductForm(request.user)
		return render(request, 'add_product.html',{'form':forms,'form2':AddCompanyForm})

	def post(self, request, *args, **kwargs):
		frm = request.user
		form = AddProductForm(request.user, request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			messages.success(request, 'Item Successfully Added')
			return render(request, 'add_product.html',{'form':form,'form2':AddCompanyForm})
		else:
			messages.error(request, 'Got some error')
			return render(request, 'add_product.html',{'form':form,'form2':AddCompanyForm})



class AddCompany(View):
	def post(self, request, *args, **kwargs):
		form = AddCompanyForm(request.POST)
		forms = AddProductForm(request.user)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			messages.success(request, 'Comapany Successfully Added')
			return render(request, 'add_product.html',{'form':forms,'form2':AddCompanyForm})
		else:
			messages.error(request,'Something went wrong')
			return render(request, 'add_product.html',{'form':AddProductForm,'form2':AddCompanyForm})

class LoginView(View):
	def post(self, request, *args, **kwargs):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			request.session['is_logedin'] = True
			messages.success(request, 'Successfully Logged In')
			return redirect('warehouse:dashboard')
		else:
			messages.error(request, 'Something went wrong')
			return redirect('warehouse:home')

class LogoutView(View):
	def get(self, request, *args, **kwargs):
		logout(request)
		messages.info(request, 'Successfully Logout')
		return redirect('warehouse:home')
	
def AddQuantity(request, pk):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=pk)
		quantity= request.POST.get('quantity')
		int_quantity = int(quantity)
		product.quantity += int_quantity 
		product.save()
		product_quantity = product.quantity
		transaction = Transaction.objects.create(
			user=request.user,
			operation='Added',
			product=product,
			remarks= quantity + ' case added to stock',
			in_stock=product_quantity
			)
		messages.success(request, 'Quantity Updated Successfully')
		return redirect('warehouse:dashboard')

def DeleteQuantity( request, pk):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=pk)
		quantity = request.POST.get('quantity')
		int_quantity = int(quantity)
		if int_quantity > product.quantity:
			messages.error(request, 'You cant delete item in minus')
			return redirect('warehouse:dashboard')
		product.quantity -= int_quantity
		product.save()
		product_quantity = product.quantity
		transaction = Transaction.objects.create(
			user=request.user,
			operation='Deleted',
			product=product,
			remarks= quantity + ' case removed from stock',
			in_stock=product_quantity
			)
		messages.success(request, 'Quantity Updated Successfully')
		return redirect('warehouse:dashboard')


class UpdateProductView(UpdateView):
	model = Product
	fields = [ 'company','name', 'price', 'quantity']
	template_name = 'edit_product.html'
	context_object_name = 'products'
	success_url = reverse_lazy('warehouse:dashboard')

class DeleteProductView(DeleteView):
	model = Product
	template_name = 'product_confirm_delete.html'
	success_url=reverse_lazy('warehouse:dashboard')


class TransactionView(View):
	def get(self, request, *args, **kwargs):
		transactions = Transaction.objects.filter(user=request.user)
		return render(request, 'transaction.html', {'transactions':transactions})

class DamageView(View):
	def get(self, request, *args, **kwargs):
		form1 = AddCustomerForm
		return render(request, 'damages.html', {'form1':form1})

	def post(self, request, *args, **kwargs):
		form = AddCustomerForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = self.request.user
			obj.save()
		
			i = 1
			while(True):
				name = 'product_' + str(i)
				print('ok')
				if name in self.request.POST:
					product = self.request.POST.get(name)
					price = self.request.POST.get('price_' + str(i))
					quantity = self.request.POST.get('quantity_' + str(i))
					mfg = self.request.POST.get('mfg_' + str(i))
					exp = self.request.POST.get('exp_' + str(i))
					Damage_Product.objects.create(
						product=product,
						price=price,
						quantity=quantity,
						mfg=mfg,
						exp=exp,
						customer=obj)
					i = i + 1
				else:
					break
			return redirect('warehouse:dashboard')
		return render(request, 'damages.html', {'form1':form})




def demo(request):
	return render(request, 'demo.html')





































































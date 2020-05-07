from django.shortcuts import render, redirect
from .models import Product, Transaction
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from .forms import AddProductForm, AddCompanyForm
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




#class Dashboard(LoginRequiredMixin,View):
def Dashboard(request):
	products = Product.objects.filter(user=request.user)
	return render(request, 'dashboard.html', {'products':products})


# def add_quantity(request,pk):
# 	if request.method == 'POST':
# 		product = get_object_or_404(Product, pk=pk)
# 		quantity = request.POST.get('quantity')
# 		int_quantity = int(quantity)
# 		product.quantity += int_quantity
# 		product.save()
# 		updated_quantity = product.quantity

# 		new_transaction = Transaction.objects.create(
# 				#object_id = uuid.uuid4(),
# 				operation= 1, 
# 				product = product, 
# 				remarks = str(quantity) +' case has been added to the the stock by'

				
# 		)
# 		new_transaction.save()
		
		
# 		data = {
# 			'quantity':updated_quantity
# 		}
		
# 		return JsonResponse(data) 


# def delete_quantity(request, pk):
# 	if request.method == 'POST':
# 		product = get_object_or_404(Product,pk=pk)
# 		quantity = request.POST.get('quantity')
# 		print (quantity)
# 		int_quantity = int(quantity)
# 		product.quantity -=int_quantity
# 		product.save()
# 		updated_quantity = product.quantity

# 		new_transaction = Transaction.objects.create(
# 			operation = 2,
# 			product = product,
# 			remarks = str(quantity) +' case has been deleted from the stock'
# 			)
		
# 		data = {
# 			'quantity':updated_quantity
# 		}
# 		return JsonResponse(data)


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

# class AddQuantityView(View):
# 	def post(self, request, *args, **kwargs):
# 		product = get_object_or_404(Product, pk=pk)
# 		quantity = request.POST.get('quantity')
# 		print(str(quantity))
# 		add = product.increment_quantity(quantity)
# 		add.save()
# 		
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
			operation=1,
			product=product,
			remarks= quantity + ' case added from stock',
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
			operation=2,
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

def demo(request):
	return render(request, 'demo.html')





































































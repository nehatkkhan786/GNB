from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [

	path('', views.HomeView.as_view(), name = 'home'),
	path('dashboard/', views.Dashboard, name = 'dashboard'),
	path('<int:pk>/add/', views.AddQuantity, name = 'add_quantity'),
	path('<int:pk>/delete/', views.DeleteQuantity, name = 'delete_quantity'),
	path('edit_product/<int:pk>/', views.UpdateProductView.as_view(), name='update_product'),
	path('delete_product/<int:pk>/', views.DeleteProductView.as_view(), name = 'delete_product'),



	path('add_product/', views.AddProduct.as_view(), name = 'add_product'),
	path('add_company/', views.AddCompany.as_view(), name = 'add_company'),
	path('login/', views.LoginView.as_view(), name = 'login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('transaction/', views.TransactionView.as_view(), name='transaction'),
	path('damages/', views.DamageView.as_view(), name ='damages'),
	path('damages/add_damage_product/', views.Add_Damage_Product.as_view(), name = 'add_damage_product'),
	
	
	path('demo/', views.demo, name ='demo'),
	

]

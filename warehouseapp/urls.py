from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [

	path('', views.Dashboard.as_view(), name = 'homepage'),
	path('list/<int:pk>/add/', views.add_quantity, name = 'add_quantity'),
	path('list/<int:pk>/delete/', views.delete_quantity, name = 'delete_quantity'),
	path('add_product/', views.AddProduct.as_view(), name = 'add_product'),
	path('add_company/', views.AddCompany.as_view(), name = 'add_company'),
	path('demo/', views.demo, name ='demo'),
	

]

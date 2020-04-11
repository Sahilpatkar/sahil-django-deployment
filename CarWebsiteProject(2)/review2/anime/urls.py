from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('sign/', views.sign, name='sign'),
	path('register/', views.register, name='register'),
	path('carinfo/', views.car, name='carinfo'),

]
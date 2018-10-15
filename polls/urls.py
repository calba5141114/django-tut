from django.urls import path 
# importing views from module
from . import views

urlpatterns = [
	path('', views.index, name='index'),
]

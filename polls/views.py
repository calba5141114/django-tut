from django.shortcuts import render
from django.http import HttpResponse as httpr

# Application Views
	
def index(request):
	return httpr("Hello world, you are at the polls app index")

from django.shortcuts import render, redirect

# Create your views here.

def home(request):
	return render(request,'appnote1/dashboard.html')

def customer(request):
	return render(request,'appnote1/customer.html')

def products(request):
	return render(request,'appnote1/products.html')

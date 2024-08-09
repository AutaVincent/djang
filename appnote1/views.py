from django.shortcuts import render,redirect
from .forms import CreateUserForm, PurchaseForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *


def home(request):
	x = CustomUser.objects.get(id=request.user.id)
	return render(request,'appnote1/dashboard.html', {'x': x})

def customer(request):
	return render(request,'appnote1/customer.html')

def products(request):
	return render(request,'appnote1/products.html')

def registerpage(request):
        if request.user.is_authenticated:
            messages.info(request, "you're already logged in")
            return redirect('home')
        else:

            form=CreateUserForm()
            if request.method =='POST':
            
                form=CreateUserForm(request.POST)
                if form.is_valid():
                        form.save() 
                        email=form.cleaned_data.get('email')

                        messages.success(request,'account was created for ' +email)
                        return redirect('login')
                else:
                    form=CreateUserForm()
                    messages.warning(request,'Something wentwrong')
                    context={'form':form}
                    return render(request,"appnote1/register.html",context)
            else:
                form=CreateUserForm()
                context={'form':form}
                return render(request,"appnote1/register.html",context)
        
        
def loginpage(request):
         if request.user.is_authenticated:
            return redirect('home')
         else:
    
            if request.method=='POST':
                email=request.POST['email']
                password= request.POST.get('password')
                user=authenticate(request,email=email,password=password)

                if user is not None:
                    login(request, user)
                    messages.info(request,'login successful')
                    return redirect('home')
                else:
                    messages.info(request,'Error invalid credential')
                    #mess="Error invalid credential"
                    #context={'messages':mess}
                    return render(request,"appnote1/login.html")

            else:  
                #mess="Error invalid credential"
                #context={'messages':mess}
                return render(request,"appnote1/login.html")        
            

def signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def buy(request):
	if request.method == "POST":
		form = PurchaseForm(request.POST)
		if form.is_valid():
			x = form.cleaned_data.get('product')
			print(x.price)
			Order.objects.create(
				customer = request.user,
                product	= x,
                # status = 'Pending'
			)

	else:
		form = PurchaseForm()
	return render(request, "appnote1/buynow.html", {'form':form})
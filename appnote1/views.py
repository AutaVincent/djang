from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .decorator import *



def home(request):


    orders=Order.objects.all()
    customers=CustomUser.objects.all()
    total_orders=orders.count()
    total_customers=customers.count()
    delivered=orders.filter(status='Delivered').count()
    out=orders.filter(status='Out for delivery').count()
    pending=orders.filter(status='Pending').count()


    context={'orders':orders,'customers':customers,'out':out, 'delivered':delivered,'pending':pending,'total_orders':total_orders,
             'total_customers':total_customers}
    
    return render(request,'appnote1/dashboard.html',context)


def customer(request,pk):
    customer=CustomUser.objects.get(id=pk)
    orders=customer.order_set.all()
    order_count=orders.count()
    context={'customers':customer,'orders':orders,'orders_count':order_count}
    return render(request,'appnote1/customer.html',context)


def products(request):
    products=Product.objects.all()
    return render(request,'appnote1/products.html',{'products':products})


def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
       form=OrderForm(request.POST, instance=order)
       if form.is_valid:
           form.save() 
           return redirect('home')
    context={'form':form}


    return render(request,"appnote1/update_order.html",context)


def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect("home")


    context={'item':order}


    return render(request,'appnote1/delete.html',context)


@login_required(login_url='login')
def purchasePage(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            selection = form.cleaned_data['product']
            print(selection)
    else:
        form = PurchaseForm()
    return render(request,'appnote1/buynow.html', {'form':form})


@unauthenticated_user
def registerpage(request):
        if request.user.is_authenticated:
            messages.warning(request, 'you are already logged in')
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
                    messages.success(request,'Something wentwrong')
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
                email=request.POST.get('email')
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

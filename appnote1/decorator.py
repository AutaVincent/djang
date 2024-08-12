from django.shortcuts import render,redirect
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
         if request.user.is_authenticated:
            messages.warning(request, 'you are already logged in')
            return redirect('/appnote1/home')
         else:
           return view_func(request,*args,**kwargs)
    
    return wrapper_func

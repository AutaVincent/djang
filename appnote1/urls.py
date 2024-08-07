from django.urls import path
from . import views

urlpatterns=[
    path("",views.home ,name="home"),
    path("customer/",views.customer ,name="customer"),
    path("products/",views.products,name="products"),
    path("register/",views.registerpage,name="register"),
    path("login/",views.loginpage ,name="login"),
    path("logout/",views.signout,name="logout"),
]


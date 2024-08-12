from django.urls import path
from . import views


urlpatterns=[
    path("",views.home ,name="home"),
    path("customer/",views.customer ,name="customer"),
    path("customer/<str:pk>/",views.customer,name="customer"),
    path("update_order/<str:pk>/",views.updateOrder,name="update_order"),
    path("delete_order/<str:pk>/",views.deleteOrder,name="delete_order"),


    path("products/",views.products,name="products"),
    path("register/",views.registerpage,name="register"),
    path("login/",views.loginpage ,name="login"),
    path("logout/",views.signout,name="logout"),
    path("buy/",views.purchasePage,name="buy"),
]

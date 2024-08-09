from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=False, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone=models.CharField(max_length=200,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
class Product(models.Model):
      CATEGORY=(
            ('Indoor','Indoor'),
            ('Outdoor','Outdoor'),
      )
      name=models.CharField(max_length=200,null=True)
      price=models.DecimalField(max_digits=10, null=True, decimal_places=0)
      category=models.CharField(max_length=200,null=True,choices=CATEGORY)
      description=models.CharField(max_length=200,null=True,blank=True)
      date_created=models.DateTimeField(auto_now_add=True,null=True)   

     
      def __str__(self) -> str:
            return f"{self.name} - {self.price} - {self.category}"
      
      
  

class Order(models.Model):  
      STATUS=(
            ('Pending','Pending'),
            ('Out for delivery','Out for delivery'),
            ('Delivered','Delivered') 
            )
      customer=models.ForeignKey(CustomUser,null=True,on_delete=models.SET_NULL)
      product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
      date_created=models.DateTimeField(auto_now_add=True,null=True)
      status=models.CharField(max_length=200,null=True,choices=STATUS)

      def __str__(self) -> str:
            return self.product.name 


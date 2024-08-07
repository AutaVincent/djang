from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CreateUserForm(UserCreationForm):
      class Meta:
        model = CustomUser
        fields = ['username','email','password1','password2']

class PurchaseForm(forms.Form): 
    product = forms.ModelChoiceField(
        queryset = Product.objects.all(),
        label = 'Select a Product',
        widget = forms.Select(attrs={'class': 'form-select border-2 border-success bg-body-secondary'}),
        required = True,
    )

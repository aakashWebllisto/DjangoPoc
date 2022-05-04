from django.contrib.auth.models import User
from django import forms
from .models import Listing2,Query2
class ListCarForm(forms.ModelForm):
    class Meta:
        model = Listing2
        fields = ["make","model_name","year","asking_price","condition","seller_name","seller_mobile"]
    

class QueryListCarForm(forms.ModelForm):
    class Meta:
        model = Query2
        fields = ["name","mobile","query_id"]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
                'username', 
                'password', 
                'email', 
                'first_name', 
                'last_name'
        ]
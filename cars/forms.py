from django import forms
from .models import Listing2,Query
class ListCarForm(forms.ModelForm):
    class Meta:
        model = Listing2
        fields = ["make","model_name","year","asking_price","condition","seller_name","seller_mobile"]
    

class QueryListCarForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ["name","mobile","query_id"]
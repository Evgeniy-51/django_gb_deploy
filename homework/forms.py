from datetime import datetime

from django import forms


class ChangeProduct(forms.Form):
    prod_id = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Product ID'}))
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Product description'}))
    price = forms.FloatField(min_value=1, step_size=0.01, widget=forms.NumberInput(attrs={'placeholder': 'Price'}))
    amount = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Amount'}))
    create_date = forms.DateField(initial=datetime.today(), widget=forms.DateInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False)
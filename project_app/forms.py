from django import forms
from .models import Travel


class CreateTravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ('name','category','price','image')




class UpdateTravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ('name','category','price','image')
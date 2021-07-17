from django import forms
from django.db.models import fields
from .models import Advert,Location,Category



class AdvertForm(forms.ModelForm):

    
    
    class Meta:
        model=Advert
        fields=("title","category","location","description","condition",
        "image","price")
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter Title'}),
            'location': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please Enter Location'}),

            'location': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please Enter Location'}),
            'condition': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please Enter condition'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'placeholder': 'Please Enter description'}),
          
        
           
           

        }
class LocationForm(forms.ModelForm):
    model=Location
    fields=('name',)


class CategoryForm(forms.ModelForm):
    model = Category
    fields = ('name',)

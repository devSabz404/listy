from django.utils.datastructures import CaseInsensitiveMapping
import django_filters
from .models import Advert, Category, Location

class AdsFilter(django_filters.FilterSet):

    class Meta:
        model =Advert
        fields={
            'title':['icontains'],
            'category': ['exact'],
            'location': ['exact'],
           
            
            
            
            }


# class LocFilter(django_filters.FilterSet):

#     class Meta:
#         model = Advert
#         fields = ('location',)


# class CatFilter(django_filters.FilterSet):

#      class Meta:
#        model = Category
#        fields = ('name', )





       

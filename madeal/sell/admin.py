
from django.contrib import admin
from .models import Advert,Location,Category





class LocationAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Location, LocationAdmin)


class CategoryAdmin(admin.ModelAdmin):


    list_display = ('name','get_advert', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category,CategoryAdmin)



class AdvertAdmin(admin.ModelAdmin):


    list_display = ('title', 'slug', 'price','location',
                    'available', 'created', )
    list_filter = ('available', 'created','location','category')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Advert, AdvertAdmin)




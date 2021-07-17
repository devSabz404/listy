from django.db.models.lookups import PostgresOperatorLookup
from django.shortcuts import render,get_object_or_404
from .forms import AdvertForm, LocationForm
from .models import Advert, Location,Profile,Category
from django.contrib import messages
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .filters import AdsFilter


def AdvertView(request):

    img = Advert.objects.all()
   
    return render(request,"sell/advert_list.html",{"img":img})


@login_required
def AdvertPost(request):
    if request.method == "POST":
        form = AdvertForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
           

    else:
        form = AdvertForm()
    return render(request, "sell/upload.html", {"form": form})


class AdvertDetailView(generic.DetailView):
    model = Advert


class ProfileDetailView(generic.DetailView):
    model = Profile
    
    
    


class AdvertListView(generic.ListView):

    model = Advert
    context_object_name = 'img'
    #queryset = Advert.objects.all().order_by("-created")
    template_name = 'sell/advert_list.html'
    ordering = ['-created']
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['filter']=AdsFilter(self.request.GET, self.get_queryset())
        return context
    
  

class CategoryListView(generic.ListView):
    model = Category
    template_name="sell/category_view.html"
    context_object_name='cat'


# class CategoryDetailView(generic.DeleteView):
#     model= Category
#     template_name="sell/category_detail.html"
#     context_object_name="catd"

def CategoryDetailView(request, id):


    cat = get_object_or_404(Category, id=id)
    context = {
        "category": cat.advert.all()
    }
    return render(request, 'sell/category_detail.html', context)
        



    


    




  




# def is_valid_queryparam(param):
#     return param != '' and param is not None

# def search_view(request):
#     qs=Advert.objects.all()
 
#     query_search =request.GET.get('search')
#     query_category = request.GET.get('category')
#     query_location = request.GET.get('location')

#     if is_valid_queryparam(query_search):
#         qs = qs.filter(title__icontains=query_search)
    
#     if is_valid_queryparam(query_category) and query_category != 'Choose...':
#         qs = qs.filter(category__name=query_category)

#     if is_valid_queryparam(query_location) and query_location != 'Choose...':
#         qs = qs.filter(location__name=query_location)

#     return render(request,'sell/search_form.html',{qs:'qs'})

                 

   


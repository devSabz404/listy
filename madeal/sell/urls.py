from django.urls import path
from .import views

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),

    path('post/', views.AdvertPost, name='post'),

    path('home', views.AdvertListView.as_view(), name='home1'),
    path('', views.advert_list, name='home'),
    path('category', views.CategoryListView.as_view(), name='category'),
    path('category_detail/<int:pk>',
         views.AdvertcatListView.as_view(), name='cat_detail'),
    path('advert/<int:pk>', views.AdvertDetailView.as_view(), name='advert_detail'),
  
  
]

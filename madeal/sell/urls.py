from django.urls import path
from .import views

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),

    path('post/', views.AdvertPost, name='post'),

    path('', views.AdvertListView.as_view(), name='home'),
    path('category', views.CategoryListView.as_view(), name='category'),
    path('category_detail/<int:pk>', views.CategoryDetailView, name='category-detail'),
    path('advert/<int:pk>', views.AdvertDetailView.as_view(), name='advert-detail'),
  
  
]

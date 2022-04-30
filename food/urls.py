from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
        path('', views.index, name='index'),
        path('food_detail/<int:id>/', views.food_detail, name= 'food_detail'),
        path('food_list/', views.food_list, name= 'food_list'),
        path('search/', views.search, name= 'search'),
        ]
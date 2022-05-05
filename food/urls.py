from django.urls import path, include
import django.contrib.auth.urls
from . import views

app_name = 'food'


urlpatterns = [
        path('', views.common.index, name='index'),
        path('food_detail/<int:id>/', views.food.food_detail, name= 'food_detail'),
        path('food_list/', views.food.food_list, name= 'food_list'),
        path('search/', views.common.search, name= 'search'),
        path('register/', views.user.register, name='register'),
        path('login/', views.user_login, name='login'),
        ]
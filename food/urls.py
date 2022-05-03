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
        path('register_handle/', views.user.register_handle, name='register_handle'),
        path('register_exist/', views.user.register_exist, name='register_exist'),
        path('login/', views.user.login, name='login'),
        path('login_handle/', views.user.login_handle, name='login_handle'),
        path('logout/', views.user.logout, name='logout'),
        path('user_cart/', views.cart.user_cart, name='user_cart'),
        path('add/', views.cart.add, name='add'),
        path('edit/<int:oid>/', views.cart.edit, name='edit'),
        path('delete/<int:oid>/', views.cart.delete, name='delete'),
        ]
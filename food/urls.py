from django.urls import path, include
import django.contrib.auth.urls
from . import views

app_name = 'food'


urlpatterns = [
        path('', views.common.index, name='index'),
        path('food_detail/<int:id>/', views.food.food_detail, name= 'food_detail'),
        path('food_list/', views.food.food_list, name= 'food_list'),
        path('search/', views.common.search, name= 'search'),
        path('register/', views.user.user_register, name='register'),
        path('login/', views.user.user_login, name='login'),
        path('success/<int:id>', views.food.success, name='success'),
        path('cart/', views.cart.Cart1, name='cart'),
        path('logout/', views.user.logout, name='logout'),
        path('admin_page/', views.cart.admin_orders, name='admin_page'),
        path('delete/<int:id>', views.cart.delete, name='delete'),
        path('staff_delete/<int:id>', views.cart.staff_delete, name='staff_delete'),
        ]
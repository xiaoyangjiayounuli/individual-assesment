from django.template import Template, Context
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from food.models import Food_list,Food_detail, Cart
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def Cart1(request):
    username = request.user.username
    orders = Cart.objects.filter(username=username)
    return render(request, 'cart.html', {'orders' : orders})

@staff_member_required
def admin_orders(request):
    orders = Cart.objects.all()
    return render(request, 'admin_page.html', {'orders' : orders})

@login_required
def delete(request, id):
    Cart.objects.filter(id=id).delete()
    return redirect('food:cart')


@login_required
def staff_delete(request, id):
    Cart.objects.filter(id=id).delete()
    return redirect('food:admin_page')



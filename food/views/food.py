from django.shortcuts import render, get_object_or_404
from food.models import Food_list,Food_detail

def food_list(request):
    foods = Food_list.objects.all()
    return render(request, 'food_list.html', {'foods' : foods})

def food_detail(request, id):
    foods = Food_detail.objects.filter(id=id)
    return render(request, 'food_detail.html', {'foods' : foods})
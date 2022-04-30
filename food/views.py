# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Food_list,Food_detail

def food_list(request):
    foods = Food_list.objects.all()
    return render(request, 'food/food_list.html', {'foods' : foods})

def food_detail(request, id):
    foods = Food_detail.objects.filter(id=id)
    return render(request, 'food/food_detail.html', {'foods' : foods})

def index(request):
    return render(request, 'food/index.html')

def search(request):
    Result = Food_detail.objects.all()
    if request.method=="POST":
        foodname = str(request.POST.get('foodname',''))
        category = str(request.POST.get('category',''))
        Result = Food_detail.objects.filter(foodname__icontains=foodname, category__icontains=category)
    return render(request, 'food/search.html', {'foods' : Result})
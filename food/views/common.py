from django.shortcuts import render, get_object_or_404
from food.models import Food_list,Food_detail

def index(request):
    return render(request, 'index.html')

def search(request):
    Result = Food_detail.objects.all()
    if request.method=="POST":
        foodname = str(request.POST.get('foodname',''))
        category = str(request.POST.get('category',''))
        Result = Food_detail.objects.filter(foodname__icontains=foodname, category__icontains=category)
    return render(request, 'search.html', {'foods' : Result})
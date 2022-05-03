from django.shortcuts import render, get_object_or_404
from .models import Food_list,Food_detail
def index(request):
    return render(request, 'templates/index.html')

def search(request):
    Result = Food_detail.objects.all()
    if request.method=="POST":
        foodname = str(request.POST.get('foodname',''))
        category = str(request.POST.get('category',''))
        Result = Food_detail.objects.filter(foodname__icontains=foodname, category__icontains=category)
    return render(request, 'templates/search.html', {'foods' : Result})
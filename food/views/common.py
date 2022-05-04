from django.shortcuts import render, get_object_or_404
from food.models import Food_list,Food_detail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'index.html')

def search(request):
    Result = Food_detail.objects.all()
    if request.method=="POST":
        foodname = str(request.POST.get('foodname',''))
        category = str(request.POST.get('category',''))
        Result = Food_detail.objects.filter(foodname__icontains=foodname, category__icontains=category)
    return render(request, 'search.html', {'foods' : Result})


def page_list(request):
    post_list = Food_list.objects.all() 
    paginator = Paginator(post_list, 10) 
    page = request.GET.get('page') 

    try:
        post_list = paginator.page(page) 
    except PageNotAnInteger:
        post_list = paginator.page(1) 
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages) 

    return render(request, 'blog/index.html', context={'post_list': post_list})


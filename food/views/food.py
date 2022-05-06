from django.shortcuts import render, get_object_or_404
from food.models import Food_list,Food_detail, Cart

def food_list(request):
    foods = Food_list.objects.all()
    return render(request, 'food_list.html', {'foods' : foods})

def food_detail(request, id):
    list = Food_list.objects.get(id=id)
    price = list.price
    food = Food_detail.objects.get(id=id)
    return render(request, 'food_detail.html', {'food' : food, 'price' : price})

def success(request, id):
    food = Food_list.objects.get(id=id)
    username = request.user.username
    judge = Cart.objects.filter(username=username, foodname=food.foodname)
    if judge:
        judge = Cart.objects.get(username=username, foodname=food.foodname)
        amount = judge.count + 1
        total_price = judge.total_price + food.price
        Cart.objects.filter(username=username, foodname=food.foodname).update(count=amount, total_price=total_price)
    else:
        Cart.objects.create(username=username, foodname=food.foodname, count=1, total_price=food.price).save()
    return render(request, 'success.html')
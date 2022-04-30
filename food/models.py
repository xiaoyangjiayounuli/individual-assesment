from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
 

class Food_list(models.Model):
    foodname = models.TextField()
    price = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

#We join all of the attributes into a string so that data can be shared by models 
#in foreign keys, and to ensure the relevant parts can be displayed.

    def __str__(self):
        return f'{self.foodname},{self.price},{self.created_date}'

class Food_detail(models.Model):
    foodname = models.TextField()
    measure = models.TextField()
    grams = models.TextField()
    calories = models.TextField()
    protein = models.TextField()
    fat = models.TextField()
    fiber = models.TextField()
    carbs = models.TextField()
    category = models.TextField()


    def __str__(self):
        return f'{self.foodname},{self.measure},{self.grams},{self.calories},{self.protein},{self.fat},{self.fiber},{self.carbs},{self.category}'




class Customer(models.Model):
    username = models.TextField()
    email = models.TextField()
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username, self.email, self.balance, self.created_date

class Basket(models.Model):
    username = models.TextField()
    basketname = models.TextField()
    foodname = models.TextField(default='')
    address = models.TextField(default='')
    status = models.TextField(default='unpaid')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username, self.basketname, self.name, self.address, self.status, self.created_date

class Basket_Detail(models.Model):
    foodname = models.TextField()
    username = models.TextField()
    basketname = models.TextField()
    address = models.TextField()
    item = models.TextField()
    item_id = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name, self.username, self.basketname, self.address, 
        self.item, self.item_id, self.price, self.total_price, self.amount, self.created_date
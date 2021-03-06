from django.db import models
from django.utils import timezone

 

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


class Cart(models.Model):

    username = models.TextField()
    foodname = models.TextField(default='')
    total_price = models.DecimalField(max_digits=12, decimal_places=2) 
    count = models.IntegerField(verbose_name="", default=0)  # 记录用户买个多少单位的商品


    def __str__(self):
        return f'{self.username},{self.foodname},{self.count}, {self.total_price}'
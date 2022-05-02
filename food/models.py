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



class User(models.Model):

    uname = models.CharField(max_length=20, verbose_name="username", unique=True)
    upwd = models.CharField(max_length=40, verbose_name="password", blank=False)
    uemail = models.EmailField(verbose_name="email_address", unique=True)

    def __str__(self):
        return f'{self.uname},{self.upwd},{self.uemail}'


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")
    foodname = models.TextField(default='')
    count = models.IntegerField(verbose_name="", default=0)  # 记录用户买个多少单位的商品


    def __str__(self):
        return f'{self.user},{self.foodname},{self.count}'

    


    

import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from food.models import Food_detail, Food_list

#We use the command tools so that we gain access to our models and database connections
#https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/ 




class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        # drop the data from the table so that if we rerun the file, we don't repeat values
        Food_list.objects.all().delete()
        Food_detail.objects.all().delete()
        
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        try:
            with open(str(base_dir) + '/food/food_nutr/nutrients_csvfile.csv', newline='') as f:
                reader = csv.reader(f, delimiter=",")
                next(reader) # skip the header line
                for row in reader:
                    print(row)
                    list = Food_list.objects.create(
                    foodname = row[0],
                    price =row [6]
                    )
                    list.save()

                    detail = Food_detail.objects.create(
                    foodname = row[0],
                    measure = row[1],
                    grams = row[2],
                    calories = row[3],
                    protein = row[4],
                    fat = row[5],
                    fiber = row[6],
                    carbs = row[7],
                    category = row[9],
                    )
                    detail.save()
                
            print("data parsed successfully")
        except  BaseException:
            print('somthing wrong')
# Generated by Django 3.2.13 on 2022-04-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.TextField()),
                ('measure', models.TextField()),
                ('grams', models.TextField()),
                ('calories', models.TextField()),
                ('protein', models.TextField()),
                ('fat', models.TextField()),
                ('fiber', models.TextField()),
                ('carbs', models.TextField()),
                ('category', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Food_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
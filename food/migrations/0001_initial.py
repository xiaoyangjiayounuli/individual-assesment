# Generated by Django 3.2.13 on 2022-05-02 20:52

from django.db import migrations, models
import django.db.models.deletion


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
                ('price', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20, unique=True, verbose_name='username')),
                ('upwd', models.CharField(max_length=40, verbose_name='password')),
                ('uemail', models.EmailField(max_length=254, unique=True, verbose_name='email_address')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('foodname', models.TextField(default='')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('oid', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Order Number')),
                ('count', models.IntegerField(default=0, verbose_name='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.user', verbose_name='user')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-14 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_food_order_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='food',
        ),
        migrations.CreateModel(
            name='FoodOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.food')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.order')),
            ],
        ),
    ]

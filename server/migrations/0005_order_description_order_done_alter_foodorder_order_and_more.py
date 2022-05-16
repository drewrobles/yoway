# Generated by Django 4.0.4 on 2022-05-15 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_remove_order_food_foodorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='foodorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_order', to='server.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='instructions',
            field=models.TextField(default=''),
        ),
    ]
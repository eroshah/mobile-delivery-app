# Generated by Django 4.1.7 on 2023-02-20 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_drinks_extra_ratings_toppings_remove_store_rate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toppings',
            name='store',
        ),
        migrations.AddField(
            model_name='toppings',
            name='food',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stores.food'),
            preserve_default=False,
        ),
    ]

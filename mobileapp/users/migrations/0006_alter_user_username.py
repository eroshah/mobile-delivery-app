# Generated by Django 4.1.7 on 2023-03-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=36, unique=True),
            preserve_default=False,
        ),
    ]

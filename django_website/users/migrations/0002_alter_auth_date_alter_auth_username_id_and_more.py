# Generated by Django 4.1.1 on 2022-10-08 13:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='date',
            field=models.DateTimeField(default=datetime.datetime, verbose_name='Дата генерации'),
        ),
        migrations.AlterField(
            model_name='auth',
            name='username_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='id', to='users.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime, verbose_name='Дата регистарции'),
        ),
    ]

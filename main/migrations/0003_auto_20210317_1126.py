# Generated by Django 3.1.5 on 2021-03-17 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_zakazmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
    ]

# Generated by Django 3.1.5 on 2021-03-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210317_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='miniopisanie',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Мини описание'),
        ),
    ]

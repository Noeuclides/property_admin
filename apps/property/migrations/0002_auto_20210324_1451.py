# Generated by Django 3.1.7 on 2021-03-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='img',
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Urbano'), (2, 'Rural')], verbose_name='tipo de predio'),
        ),
    ]

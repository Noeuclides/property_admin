# Generated by Django 3.1.7 on 2021-03-25 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20210325_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property.company'),
        ),
    ]
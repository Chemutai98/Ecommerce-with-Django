# Generated by Django 5.0.6 on 2024-06-16 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_commerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Availability',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 4.2.20 on 2025-03-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_parameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.CharField(max_length=145),
        ),
    ]

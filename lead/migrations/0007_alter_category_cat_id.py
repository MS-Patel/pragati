# Generated by Django 4.0.5 on 2022-07-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0006_category_cat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.CharField(max_length=100),
        ),
    ]

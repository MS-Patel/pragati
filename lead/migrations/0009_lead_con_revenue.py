# Generated by Django 4.0.6 on 2022-07-13 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0008_alter_revenue_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='con_revenue',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=15),
        ),
    ]

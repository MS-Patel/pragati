# Generated by Django 4.0.5 on 2022-07-05 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0005_lead_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_id',
            field=models.IntegerField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-14 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0013_lead_trx_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='trx_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

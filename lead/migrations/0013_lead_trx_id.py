# Generated by Django 4.0.6 on 2022-07-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0012_alter_lead_con_paybal_revenue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='trx_id',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

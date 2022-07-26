# Generated by Django 4.0.6 on 2022-07-14 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0010_rename_con_revenue_lead_con_paid_revenue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='con_paid_revenue',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='con_paybal_revenue',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='con_revenue_status',
            field=models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('PAID', 'PAID'), ('CANCELLED', 'CANCELLED')], default='PENDING', max_length=100, null=True),
        ),
    ]
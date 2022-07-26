# Generated by Django 4.0.5 on 2022-07-01 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0002_alter_lead_party_address_alter_lead_party_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_types',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='lead.category', verbose_name='category'),
        ),
    ]

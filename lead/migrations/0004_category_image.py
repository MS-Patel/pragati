# Generated by Django 4.0.5 on 2022-07-01 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_alter_service_types_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

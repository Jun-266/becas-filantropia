# Generated by Django 4.2.5 on 2023-11-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_becas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='typescholarship',
            name='units_available',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='typescholarship',
            name='units_type',
            field=models.CharField(default=1, max_length=20),
        ),
        migrations.AddField(
            model_name='typescholarship',
            name='weight_percentaje',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_becas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='calendar_id',
            field=models.UUIDField(default=11),
            preserve_default=False,
        ),
    ]

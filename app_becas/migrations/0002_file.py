# Generated by Django 4.2.6 on 2023-10-10 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_becas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_file', models.FileField(upload_to='archivos/')),
            ],
        ),
    ]

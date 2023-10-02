# Generated by Django 4.2.5 on 2023-10-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('calendar_type_id', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=30)),
                ('scholarship_id', models.CharField(max_length=20)),
                ('inscription_start_date', models.DateField()),
                ('inscription_deadline', models.DateField()),
                ('selection_start_date', models.DateField()),
                ('selection_deadline', models.DateField()),
                ('interview_start_date', models.DateField()),
                ('interview_deadline', models.DateField()),
                ('publish_elected_start_date', models.DateField()),
                ('publish_elected_deadline', models.DateField()),
            ],
        ),
    ]

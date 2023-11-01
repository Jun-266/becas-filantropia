# Generated by Django 4.2.5 on 2023-10-31 19:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('auto_id', models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False)),
                ('convocation_type_id', models.CharField(max_length=2)),
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
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('identification', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_file', models.FileField(upload_to='archivos/')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='My_user',
            fields=[
                ('user_id', models.CharField(max_length=255)),
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255)),
                ('rol', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=250)),
                ('amount', models.IntegerField()),
                ('type_scholarship', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeScholarship',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=30)),
                ('school', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('phone', models.CharField(max_length=10)),
                ('first_semester', models.CharField(max_length=8)),
                ('last_semester', models.CharField(max_length=8)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_becas.major')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('enterprise_name', models.CharField(max_length=20)),
                ('contacts', models.ManyToManyField(related_name='donors', to='app_becas.contact')),
                ('scholarships', models.ManyToManyField(related_name='donors', to='app_becas.scholarship')),
            ],
        ),
    ]

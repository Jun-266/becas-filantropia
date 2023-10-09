from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My_user',
            fields=[
                ('userId', models.CharField(max_length=255)),
                ('autoId', models.AutoField(primary_key=True, serialize=False)),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=250)),
                ('amount', models.IntegerField()),
                ('type_scholarship', models.CharField(max_length=50)),
            ],
        ),

        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('auto_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('calendar_type_id', models.CharField(max_length=2)),
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
            name='TypeScholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ]   
        ),

        migrations.CreateModel(
            name='Contact',
            fields=[
                ('auto_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identification', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('auto_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('enterprise_name', models.CharField(max_length=20)),
                ('contacts', models.ManyToManyField(related_name='donors', to='app_becas.contact')),
                ('scholarships', models.ManyToManyField(related_name='donors', to='app_becas.scholarship')),
            ],
        ),
    ]

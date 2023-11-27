# Generated by Django 4.2.7 on 2023-11-26 17:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('type', models.CharField(choices=[('Aprobada', 'Aprobada'), ('En proceso', 'En proceso'), ('Denegada', 'Denegada'), ('Concluida', 'Concluida')], max_length=20, primary_key=True, serialize=False)),
            ],
        ),
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
            name='ConditionEnum',
            fields=[
                ('name', models.CharField(editable=False, max_length=35, primary_key=True, serialize=False)),
                ('condition_type', models.CharField(max_length=40)),
                ('data_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ConditionParams',
            fields=[
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('scholarship_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50)),
                ('condition_name', models.CharField(editable=False, max_length=50)),
                ('value', models.CharField(editable=False, max_length=30)),
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
            name='MyUser',
            fields=[
                ('user_id', models.CharField(max_length=50)),
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('rol', models.CharField(choices=[('Director filantropía', 'Director filantropía'), ('Filantropía', 'Filantropía'), ('Apoyo financiero', 'Apoyo financiero')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('calendar_id', models.CharField(default=uuid.uuid4, max_length=50)),
                ('donor_id', models.CharField(default=uuid.uuid4, max_length=50)),
                ('name', models.CharField(max_length=40)),
                ('summary', models.CharField(max_length=250)),
                ('target_audiences', models.CharField(default='La Beca está dirigida a _, de estratos _, del departamento/municipio de _, con alto desempeño, potencial académico y limitaciones económicas manifiestas, interesados en cursar los programas de pregrado de _. Esta beca no aplica para _ ', max_length=400)),
                ('benefits', models.CharField(max_length=450)),
                ('recomendations', models.CharField(max_length=2200)),
                ('additional_info', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='ScholarshipParams',
            fields=[
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('type_name', models.CharField(default=uuid.uuid4, max_length=30)),
                ('scholarship_id', models.CharField(default=uuid.uuid4, max_length=30)),
                ('units', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('units_type', models.CharField(default=1, max_length=20)),
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
            name='ScholarshipApplication',
            fields=[
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('application_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_becas.applicationstatus')),
                ('scholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_becas.scholarship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_becas.student')),
            ],
            options={
                'verbose_name': 'Scholarship Application',
                'verbose_name_plural': 'Scholarship Applications',
            },
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('enterprise_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('pais', models.CharField(blank=True, max_length=30, null=True)),
                ('joined_date', models.DateField(blank=True, null=True)),
                ('scholarships', models.ManyToManyField(related_name='donors', to='app_becas.scholarship')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('auto_id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('identification', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Dueño', 'Dueño'), ('Empleado', 'Empleado')], max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('donor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='app_becas.donor')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('student_code', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('grade_point_average', models.DecimalField(decimal_places=2, max_digits=5)),
                ('application_date', models.DateField()),
                ('requested_scholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_becas.scholarship')),
            ],
        ),
    ]

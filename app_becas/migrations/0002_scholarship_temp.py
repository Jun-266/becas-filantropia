from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('app_becas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=250)),
                ('amount', models.IntegerField()),
                ('type_scholarship', models.CharField(
                    choices=[('Excelencia', 'Excelencia'), ('Logros y Representantes', 'Logros y Representantes'),
                             ('Colaboradores', 'Colaboradores'), ('Especial', 'Especial'),
                             ('Familiar y Minorías', 'Familiar y Minorías')], max_length=50)),
            ],
        ),
    ]

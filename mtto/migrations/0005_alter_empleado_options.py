# Generated by Django 4.0.3 on 2022-03-24 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtto', '0004_empleado_cedula'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['nombre', 'cedula', 'cargo', 'departamento', 'sueldo'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
    ]

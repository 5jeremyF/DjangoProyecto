# Generated by Django 4.0.6 on 2022-09-18 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtto', '0007_materia_creditos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empleado',
            new_name='Profesores',
        ),
        migrations.AlterModelOptions(
            name='profesores',
            options={'ordering': ['nombre'], 'verbose_name': 'Profesores', 'verbose_name_plural': 'Profesores'},
        ),
    ]

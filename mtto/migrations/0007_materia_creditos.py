# Generated by Django 4.0.6 on 2022-09-18 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtto', '0006_rename_cargo_materia_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='creditos',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

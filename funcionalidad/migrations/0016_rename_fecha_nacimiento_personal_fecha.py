# Generated by Django 5.0.7 on 2024-09-08 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionalidad', '0015_remove_personal_activo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal',
            old_name='fecha_nacimiento',
            new_name='fecha',
        ),
    ]

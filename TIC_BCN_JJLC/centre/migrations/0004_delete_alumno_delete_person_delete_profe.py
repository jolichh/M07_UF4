# Generated by Django 5.0.3 on 2024-03-18 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Profe',
        ),
    ]

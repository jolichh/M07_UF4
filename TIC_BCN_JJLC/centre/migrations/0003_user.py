# Generated by Django 5.0.3 on 2024-03-17 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0002_alumno_profe'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('curs', models.CharField(max_length=100)),
                ('rol', models.CharField(choices=[('a', 'Alumne'), ('p', 'Professor')], max_length=100)),
            ],
        ),
    ]

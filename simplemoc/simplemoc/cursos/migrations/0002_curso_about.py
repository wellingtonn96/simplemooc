# Generated by Django 2.0 on 2018-07-17 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='about',
            field=models.TextField(blank=True, verbose_name='Sobre o Curso'),
        ),
    ]

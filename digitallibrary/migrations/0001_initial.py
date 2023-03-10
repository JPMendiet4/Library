# Generated by Django 3.2 on 2023-01-07 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('nationality', models.CharField(max_length=3, verbose_name='Nacionalidad')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Título')),
                ('year', models.IntegerField(default=1900, verbose_name='Año')),
                ('language', models.CharField(help_text='ISO 639-1 Language code (2 chars)', max_length=2, verbose_name='Idioma')),
                ('cover_url', models.URLField(blank=True, help_text='Guarda el url de una imagen', null=True, verbose_name='Portada')),
                ('price', models.DecimalField(decimal_places=2, default='', max_digits=10, verbose_name='Precio')),
                ('sellable', models.BooleanField(default=True, help_text='True disponible, False no disponible', verbose_name='Disponible')),
                ('copies', models.IntegerField(default=1, verbose_name='Copias')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Descripción')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitallibrary.author')),
            ],
        ),
    ]

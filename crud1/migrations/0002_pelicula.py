# Generated by Django 5.0.2 on 2024-02-25 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('sinopsis', models.TextField()),
                ('duracion', models.IntegerField()),
                ('genero', models.CharField(max_length=255)),
                ('estado', models.CharField(choices=[('estreno', 'Estreno'), ('no_disponible', 'No disponible')], max_length=20)),
                ('imagen', models.ImageField(upload_to='peliculas/')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
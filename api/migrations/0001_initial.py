# Generated by Django 4.2.7 on 2023-12-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catalogo_palabras',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('palabra', models.CharField(max_length=25, unique=True)),
                ('caracteres', models.IntegerField()),
                ('raiz', models.CharField(max_length=25)),
                ('letra_inicial', models.CharField(max_length=1)),
            ],
        ),
    ]

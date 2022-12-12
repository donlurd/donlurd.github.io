# Generated by Django 4.1.1 on 2022-11-04 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_tienda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('alt_text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TiendaAtributo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.marca')),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.tienda')),
            ],
        ),
    ]
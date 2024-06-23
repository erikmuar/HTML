# Generated by Django 5.0.6 on 2024-06-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_alter_frasedb_options_alter_frasedb_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='MelonDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(verbose_name='Cantidad')),
                ('chicle_de_melon', models.CharField(max_length=10, verbose_name='¿Es un chicle de melón?')),
                ('maduro', models.CharField(max_length=50, verbose_name='¿Está maduro el melón?')),
            ],
            options={
                'verbose_name': 'Melon',
                'verbose_name_plural': 'Melones',
                'db_table': 'Melones',
            },
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-21 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(primary_key=True, serialize=False, unique=True, verbose_name='Número de Identificación'),
        ),
    ]

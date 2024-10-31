# Generated by Django 5.0.4 on 2024-10-31 04:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_court_has_active_promotion_court_sport_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('reservación', 'Reservación'), ('promoción', 'Promoción'), ('pago', 'Pago'), ('review', 'Review'), ('other', 'Other')], max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notificación',
                'verbose_name_plural': 'Notificaciones',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('promotion_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.court')),
            ],
            options={
                'verbose_name': 'Promoción',
                'verbose_name_plural': 'Promociones',
            },
        ),
        migrations.CreateModel(
            name='ReservationHistory',
            fields=[
                ('reservation_history_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('status', models.CharField(choices=[('Confirmado', 'Confirmado'), ('Cancelado', 'Cancelado'), ('Completado', 'Completado')], default='Confirmado', max_length=20)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.court')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Historial de Reserva',
                'verbose_name_plural': 'Historiales de Reserva',
            },
        ),
    ]
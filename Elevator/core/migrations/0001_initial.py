# Generated by Django 5.0.3 on 2024-03-08 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elevator_number', models.IntegerField()),
                ('current_floor', models.PositiveSmallIntegerField(default=0)),
                ('is_operational', models.BooleanField(default=True)),
                ('is_door_open', models.BooleanField(default=True)),
                ('running_status', models.IntegerField(choices=[(1, 'Going Up'), (0, 'Standing Still'), (-1, 'Going Down')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ElevatorSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=20)),
                ('max_floor', models.IntegerField()),
                ('number_of_elevators', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ElevatorRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_floor', models.PositiveSmallIntegerField()),
                ('destination_floor', models.PositiveSmallIntegerField()),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('elevator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.elevator')),
            ],
        ),
        migrations.AddField(
            model_name='elevator',
            name='elevator_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.elevatorsystem'),
        ),
    ]
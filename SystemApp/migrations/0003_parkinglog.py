# Generated by Django 3.2.9 on 2021-11-11 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SystemApp', '0002_auto_20211110_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parkinglog',
            fields=[
                ('ticket_id', models.UUIDField(db_column='TicketId', primary_key=True, serialize=False)),
                ('date', models.DateField(db_column='Date')),
                ('platenum', models.CharField(db_column='PlateNum', max_length=50)),
                ('entrygateid', models.CharField(db_column='EntryGateId', max_length=50)),
                ('checkintime', models.BigIntegerField(db_column='CheckinTime')),
                ('checkouttime', models.BigIntegerField(blank=True, db_column='CheckoutTime', null=True)),
                ('exitgateid', models.CharField(blank=True, db_column='ExitGateId', max_length=50, null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=50, null=True)),
                ('duration', models.FloatField(blank=True, db_column='Duration', null=True)),
                ('cash', models.FloatField(blank=True, db_column='Cash', null=True)),
                ('subcription_id', models.CharField(blank=True, db_column='SubcriptionId', max_length=50, null=True)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemApp.customers')),
            ],
        ),
    ]

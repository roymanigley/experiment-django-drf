# Generated by Django 4.2.7 on 2023-11-17 18:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('ACTIVE', 'Active'), ('PASSIVE', 'Passive'), ('EXPENSE', 'Expense'), ('REVENUE', 'Revenue')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('remark', models.TextField(null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('credit_account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='credit_booking', to='accounting.account')),
                ('debit_account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='debit_booking', to='accounting.account')),
            ],
        ),
    ]

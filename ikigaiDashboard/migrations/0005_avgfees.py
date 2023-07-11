# Generated by Django 4.2.2 on 2023-07-10 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikigaiDashboard', '0004_btctraders'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvgFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('avg_fee_per_transactions', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'db_table': 'avgfees',
            },
        ),
    ]
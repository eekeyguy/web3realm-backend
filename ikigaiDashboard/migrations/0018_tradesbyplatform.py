# Generated by Django 4.2.2 on 2023-07-11 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikigaiDashboard', '0017_rename_brc20_fee_bitcointransaction_brc20_fee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradesByPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('project', models.CharField(max_length=100)),
                ('trades', models.IntegerField()),
            ],
            options={
                'db_table': 'tradesbyplatform',
            },
        ),
    ]
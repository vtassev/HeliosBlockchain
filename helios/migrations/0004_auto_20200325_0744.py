# Generated by Django 2.2.10 on 2020-03-25 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helios', '0003_auto_20200325_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='contract_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='election',
            name='owner_address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
# Generated by Django 3.2.2 on 2021-05-29 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMIK', '0002_auto_20210530_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peminjam',
            name='no_pengenal',
            field=models.PositiveBigIntegerField(),
        ),
    ]

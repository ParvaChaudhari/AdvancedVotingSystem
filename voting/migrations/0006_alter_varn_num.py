# Generated by Django 3.2.5 on 2022-04-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_varn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varn',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.5 on 2022-04-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0007_time_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_num',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 4.0.1 on 2022-04-24 17:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0021_alter_result_pn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='Aadhar_no',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]

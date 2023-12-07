# Generated by Django 4.0.1 on 2022-04-25 13:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0023_alter_voter_aadhar_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='Aadhar_no',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')]),
        ),
    ]

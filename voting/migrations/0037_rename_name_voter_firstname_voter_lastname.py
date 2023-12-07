# Generated by Django 4.0.1 on 2022-04-28 09:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0036_remove_voter_lastname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='name',
            new_name='Firstname',
        ),
        migrations.AddField(
            model_name='voter',
            name='Lastname',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$')]),
        ),
    ]

# Generated by Django 4.0.1 on 2022-04-21 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0015_alter_voter_aadhar_no_alter_voter_voter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='Aadhar_no',
            field=models.SmallIntegerField(max_length=12, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.0.1 on 2022-04-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0017_alter_voter_aadhar_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='Aadhar_no',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]

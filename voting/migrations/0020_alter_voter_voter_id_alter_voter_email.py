# Generated by Django 4.0.1 on 2022-04-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0019_alter_voter_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='Voter_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='voter',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]

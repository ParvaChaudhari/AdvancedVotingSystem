# Generated by Django 4.0.1 on 2022-04-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0014_remove_politicalparty_candidate_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='Aadhar_no',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='voter',
            name='Voter_id',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]

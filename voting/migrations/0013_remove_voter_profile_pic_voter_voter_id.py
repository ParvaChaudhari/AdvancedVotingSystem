# Generated by Django 4.0.1 on 2022-04-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0012_delete_recmail_delete_varn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='voter',
            name='Voter_id',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]

# Generated by Django 3.2.5 on 2022-04-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_recmail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Varn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(max_length=4)),
            ],
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-26 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectCar', '0003_remove_contact_us_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='first_name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='last_name',
            field=models.TextField(max_length=50),
        ),
    ]
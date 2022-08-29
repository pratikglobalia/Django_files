# Generated by Django 4.1 on 2022-08-12 05:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0004_alter_user_area_alter_user_city_alter_user_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(12)]),
        ),
    ]
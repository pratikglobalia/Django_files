# Generated by Django 4.1 on 2022-08-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0006_alter_user_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.IntegerField(),
        ),
    ]
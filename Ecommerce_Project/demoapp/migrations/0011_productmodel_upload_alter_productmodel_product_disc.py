# Generated by Django 4.1 on 2022-08-22 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0010_productmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='upload',
            field=models.ImageField(default=1, upload_to='media/images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_disc',
            field=models.TextField(max_length=500),
        ),
    ]
# Generated by Django 4.0.5 on 2022-07-05 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_student_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='comment',
            field=models.CharField(default='nothing', max_length=40),
        ),
    ]

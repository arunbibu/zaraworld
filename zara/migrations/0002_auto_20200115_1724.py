# Generated by Django 3.0.2 on 2020-01-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zara', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='ParentName',
        ),
        migrations.AddField(
            model_name='parent',
            name='FatherName',
            field=models.CharField(default='Father Name', max_length=100),
        ),
        migrations.AddField(
            model_name='parent',
            name='MotherName',
            field=models.CharField(default='Mother Name', max_length=100),
        ),
    ]

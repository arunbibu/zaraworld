# Generated by Django 3.0.2 on 2020-02-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zara', '0003_parent_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='attendance',
            field=models.CharField(blank=True, default='0', max_length=100),
        ),
    ]

# Generated by Django 3.0 on 2019-12-09 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20191203_1631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TwitterUser',
        ),
    ]

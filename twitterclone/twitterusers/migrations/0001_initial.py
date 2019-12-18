# Generated by Django 3.0 on 2019-12-09 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=20)),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Bio')),
                ('tweet_count', models.IntegerField()),
                ('follower_count', models.IntegerField()),
            ],
        ),
    ]

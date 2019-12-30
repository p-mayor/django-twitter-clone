# Generated by Django 3.0 on 2019-12-30 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tweets', '0001_initial'),
        ('twitterusers', '0002_auto_20191229_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.Tweet')),
                ('tweetfor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterusers.TwitterUser')),
            ],
        ),
    ]

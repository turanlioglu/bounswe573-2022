# Generated by Django 4.0.3 on 2022-05-18 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_linkedin_url_alter_profile_twitter_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='linkedin_url',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='twitter_url',
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-15 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='teacher',
            new_name='user',
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colearning', '0006_rename_desription_space_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]

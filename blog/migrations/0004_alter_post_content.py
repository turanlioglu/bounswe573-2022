# Generated by Django 4.0.3 on 2022-05-07 12:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image_url_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

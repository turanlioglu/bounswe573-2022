# Generated by Django 4.0.3 on 2022-05-18 18:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-17 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.ImageField(blank=True, null=True, upload_to='course_thumbnails'),
        ),
    ]

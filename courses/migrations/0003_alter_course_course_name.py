# Generated by Django 4.0.3 on 2022-05-16 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_teacher_course_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(blank=False, max_length=200, null=False),
        ),
    ]

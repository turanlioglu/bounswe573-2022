# Generated by Django 4.0.3 on 2022-05-10 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('blog', '0012_post_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]
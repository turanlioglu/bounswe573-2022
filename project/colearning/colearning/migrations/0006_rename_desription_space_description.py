# Generated by Django 4.0.3 on 2022-05-04 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colearning', '0005_category_remove_space_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='space',
            old_name='desription',
            new_name='description',
        ),
    ]

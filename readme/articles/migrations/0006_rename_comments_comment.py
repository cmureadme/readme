# Generated by Django 5.0.6 on 2024-06-16 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_rename_author_post_authors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]

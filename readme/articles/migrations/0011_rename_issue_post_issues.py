# Generated by Django 5.0.6 on 2024-06-16 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_rename_theme_issue_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='issue',
            new_name='issues',
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_rename_issue_post_issues'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.CharField(default='a', max_length=1000),
            preserve_default=False,
        ),
    ]

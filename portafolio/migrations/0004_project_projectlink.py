# Generated by Django 4.0 on 2022-09-15 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0003_rename_github_repo_project_githubrepo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projectLink',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

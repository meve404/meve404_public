# Generated by Django 4.0 on 2022-09-22 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0007_alter_project_imageslide1'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='inDevelopment',
            field=models.BooleanField(default=False),
        ),
    ]

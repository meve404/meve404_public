# Generated by Django 4.0 on 2022-09-15 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0005_project_lenguagesused'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ImageSlide1',
            field=models.ImageField(upload_to='hdFtuI2_sA'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ImageSlide2',
            field=models.ImageField(blank=True, null=True, upload_to='hdFtuI2_sA'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ImageSlide3',
            field=models.ImageField(blank=True, null=True, upload_to='hdFtuI2_sA'),
        ),
    ]
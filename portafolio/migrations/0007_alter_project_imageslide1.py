# Generated by Django 4.0 on 2022-09-15 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0006_alter_project_imageslide1_alter_project_imageslide2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ImageSlide1',
            field=models.ImageField(help_text='1903 x 960', upload_to='hdFtuI2_sA'),
        ),
    ]
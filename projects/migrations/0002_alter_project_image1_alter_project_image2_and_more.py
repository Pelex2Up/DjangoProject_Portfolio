# Generated by Django 4.1.2 on 2022-11-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image1',
            field=models.FilePathField(path='/img'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image2',
            field=models.FilePathField(path='/img'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image3',
            field=models.FilePathField(path='/img'),
        ),
    ]

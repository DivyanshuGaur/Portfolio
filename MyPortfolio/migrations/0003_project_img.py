# Generated by Django 3.2.6 on 2021-12-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPortfolio', '0002_remove_project_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='img',
            field=models.ImageField(null=True, upload_to='uploads'),
        ),
    ]

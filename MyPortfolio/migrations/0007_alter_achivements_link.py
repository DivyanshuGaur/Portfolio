# Generated by Django 3.2.6 on 2021-12-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPortfolio', '0006_alter_achivements_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achivements',
            name='link',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]

# Generated by Django 2.0 on 2018-09-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_auto_20180926_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

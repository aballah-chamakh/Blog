# Generated by Django 2.0 on 2018-11-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0002_remove_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentresponse',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]

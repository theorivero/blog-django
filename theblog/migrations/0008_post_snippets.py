# Generated by Django 3.1.7 on 2021-05-04 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_auto_20210503_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippets',
            field=models.CharField(default='check my post!', max_length=255),
        ),
    ]

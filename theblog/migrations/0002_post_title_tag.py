# Generated by Django 3.1.7 on 2021-05-01 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blog!', max_length=255),
        ),
    ]

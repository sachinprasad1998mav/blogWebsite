# Generated by Django 3.0.9 on 2022-04-23 19:27

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-12 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0006_merge_20220512_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
    ]

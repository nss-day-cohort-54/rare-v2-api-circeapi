# Generated by Django 4.0.4 on 2022-05-11 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
    ]
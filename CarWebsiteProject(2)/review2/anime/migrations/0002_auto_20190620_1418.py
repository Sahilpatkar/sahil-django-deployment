# Generated by Django 2.2.2 on 2019-06-20 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReviewAnime',
            new_name='Review',
        ),
    ]

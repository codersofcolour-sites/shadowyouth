# Generated by Django 3.0.4 on 2020-06-24 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200624_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='banner',
            new_name='banner_title',
        ),
    ]

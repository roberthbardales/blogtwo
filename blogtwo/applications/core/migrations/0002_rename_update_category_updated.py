# Generated by Django 3.2.25 on 2024-03-09 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='update',
            new_name='updated',
        ),
    ]

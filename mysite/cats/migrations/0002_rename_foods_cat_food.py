# Generated by Django 3.2.3 on 2022-07-28 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='foods',
            new_name='food',
        ),
    ]

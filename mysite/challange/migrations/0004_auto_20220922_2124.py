# Generated by Django 3.2.3 on 2022-09-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challange', '0003_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='week',
        ),
        migrations.RemoveField(
            model_name='week',
            name='name',
        ),
        migrations.RemoveField(
            model_name='week',
            name='week',
        ),
        migrations.AddField(
            model_name='week',
            name='weeknum',
            field=models.IntegerField(help_text='Enter what week you would like to add scores for (between 1-10)', max_length=200, null=True),
        ),
    ]

# Generated by Django 3.2.3 on 2022-09-22 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challange', '0002_alter_week_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_createded', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2022-09-23 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challange', '0004_auto_20220922_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='challange.customer'),
        ),
        migrations.AddField(
            model_name='score',
            name='week',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='challange.week'),
        ),
    ]

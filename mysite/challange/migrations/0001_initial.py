# Generated by Django 3.2.3 on 2022-09-21 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wholename', models.CharField(help_text='Enter your whole name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(help_text='Enter what week you would like to add scores for (between 1-10)', max_length=10)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challange.name')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movescore', models.BooleanField()),
                ('focusscore', models.BooleanField()),
                ('learnscore', models.BooleanField()),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challange.week')),
            ],
        ),
    ]

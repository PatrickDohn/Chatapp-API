# Generated by Django 3.0 on 2020-09-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='color',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='name',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='ripe',
        ),
        migrations.AddField(
            model_name='chat',
            name='content',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]

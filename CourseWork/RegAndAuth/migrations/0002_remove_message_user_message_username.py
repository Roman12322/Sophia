# Generated by Django 4.0.1 on 2022-01-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegAndAuth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='Username',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]

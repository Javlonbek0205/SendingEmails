# Generated by Django 5.1.4 on 2024-12-20 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usernotification',
            options={'get_latest_by': 'pk'},
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-30 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200730_1116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
    ]

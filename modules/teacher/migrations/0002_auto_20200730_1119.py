# Generated by Django 3.0.8 on 2020-07-30 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherdocument',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='Specializations',
        ),
        migrations.DeleteModel(
            name='TeacherDocument',
        ),
    ]

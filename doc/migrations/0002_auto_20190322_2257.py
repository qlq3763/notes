# Generated by Django 2.1.7 on 2019-03-22 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]

# Generated by Django 2.0 on 2019-08-07 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20190807_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='host',
            name='mac',
        ),
        migrations.RemoveField(
            model_name='host',
            name='purchase_time',
        ),
        migrations.RemoveField(
            model_name='host',
            name='user',
        ),
    ]
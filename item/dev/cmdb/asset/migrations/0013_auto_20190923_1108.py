# Generated by Django 2.0 on 2019-09-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0012_auto_20190827_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='network_total_use',
        ),
        migrations.AddField(
            model_name='resource',
            name='volume',
            field=models.CharField(default='[]', max_length=1024),
        ),
    ]

# Generated by Django 2.0 on 2019-08-07 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='sn',
            new_name='kernel',
        ),
        migrations.RemoveField(
            model_name='host',
            name='over_insurance_time',
        ),
        migrations.AddField(
            model_name='host',
            name='cpu_core',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='host',
            name='cpu_thread',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='host',
            name='user',
            field=models.CharField(default='', max_length=32),
        ),
    ]

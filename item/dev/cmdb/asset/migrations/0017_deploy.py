# Generated by Django 2.0 on 2020-01-08 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0016_auto_20191101_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deploy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_address', models.CharField(default='无', max_length=128)),
                ('project_name', models.CharField(default='无', max_length=64)),
                ('deploy_version', models.CharField(default='无', max_length=64)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('remark', models.TextField(default='')),
            ],
        ),
    ]

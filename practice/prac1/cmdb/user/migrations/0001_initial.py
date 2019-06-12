# Generated by Django 2.0 on 2019-04-22 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=32)),
                ('password', models.CharField(default='', max_length=512)),
                ('age', models.IntegerField(default=0)),
                ('tel', models.CharField(default='', max_length=32)),
                ('sex', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField()),
            ],
        ),
    ]

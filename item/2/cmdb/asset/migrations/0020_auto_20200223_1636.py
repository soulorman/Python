# Generated by Django 2.0 on 2020-02-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0019_interview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='question_number',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='question_type',
        ),
        migrations.AddField(
            model_name='interview',
            name='question_type_number',
            field=models.CharField(default='无', max_length=128),
        ),
    ]

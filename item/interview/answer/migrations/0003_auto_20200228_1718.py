# Generated by Django 2.0 on 2020-02-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0002_interview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview_sort_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField(default=0)),
                ('question_title', models.TextField(default='无')),
                ('question_answer', models.TextField(default='无')),
                ('scores', models.IntegerField(default=0)),
                ('update_time', models.DateTimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Interview',
            new_name='Interview_options',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

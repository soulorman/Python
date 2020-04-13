# Generated by Django 2.0 on 2020-02-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField(default=0)),
                ('question_title', models.TextField(default='无')),
                ('options_A', models.CharField(default='无', max_length=64)),
                ('options_B', models.CharField(default='无', max_length=64)),
                ('options_C', models.CharField(default='无', max_length=64)),
                ('options_D', models.CharField(default='无', max_length=64)),
                ('question_answer', models.TextField(default='无')),
                ('scores', models.IntegerField(default=0)),
                ('update_time', models.DateTimeField()),
            ],
        ),
    ]
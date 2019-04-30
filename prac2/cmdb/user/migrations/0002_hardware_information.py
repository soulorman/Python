# Generated by Django 2.2 on 2019-04-24 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hardware_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Host_Name', models.CharField(default='', max_length=32)),
                ('Network_Name', models.CharField(default='', max_length=32)),
                ('Network_Mac', models.CharField(default='', max_length=128)),
                ('Network_Ip', models.CharField(default='', max_length=128)),
                ('Gpu_Total_Mem', models.IntegerField(default=0)),
                ('GPU_Name', models.CharField(default='', max_length=128)),
                ('Cpu_Type', models.CharField(default='', max_length=512)),
                ('Cpu_Thread', models.IntegerField(default=0)),
                ('Cpu_Core', models.IntegerField(default=0)),
                ('Cpu_Number', models.IntegerField(default=0)),
                ('Data_Size', models.CharField(default='', max_length=1024)),
                ('Root_Size', models.IntegerField(default=0)),
                ('Server_Number', models.IntegerField(default=0, max_length=64)),
                ('Server_Type', models.CharField(default='', max_length=64)),
                ('Server_Producter', models.CharField(default='', max_length=128)),
                ('Kernel_Name', models.CharField(default='', max_length=128)),
                ('OS_Name', models.CharField(default='', max_length=64)),
                ('Disks_each_Size', models.CharField(default='', max_length=1024)),
                ('Disk_Number', models.IntegerField(default=0)),
                ('Mem_each_Size', models.CharField(default='', max_length=1024)),
                ('Mem_scalable', models.IntegerField(default=0)),
                ('Mem_slot_Number', models.IntegerField(default=0)),
                ('Mem_total_Size', models.IntegerField(default=0)),
                ('create_time', models.IntegerField()),
            ],
        ),
    ]
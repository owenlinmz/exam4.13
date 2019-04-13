# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostPerformance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mem', models.CharField(max_length=10, verbose_name='\u5185\u5b58\u4f7f\u7528\u7387')),
                ('disk', models.CharField(max_length=10, verbose_name='\u78c1\u76d8\u4f7f\u7528\u7387')),
                ('cpu', models.CharField(max_length=10, verbose_name='CPU\u4f7f\u7528\u7387')),
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('check_time', models.DateTimeField(auto_now=True, verbose_name='\u68c0\u6d4b\u65f6\u95f4')),
                ('bk_host_innerip', models.ForeignKey(to='home_application.HostInfo', max_length=20)),
            ],
        ),
    ]

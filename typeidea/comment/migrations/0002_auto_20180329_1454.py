# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='\u90ae\u7bb1'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0003_auto_20160511_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditconfig',
            name='cache_ttl',
            field=models.PositiveIntegerField(default=0, help_text='\u6307\u5b9a\u4e3a\u79d2\u3002\u501f\u7531\u8bbe\u5b9a\u8fd9\u4e2a\u5927\u4e8e0\u7684\u503c\u6765\u542f\u52a8\u5feb\u53d6\u3002', verbose_name='\u5feb\u53d6\u5b58\u7559\u65f6\u95f4'),
        ),
    ]

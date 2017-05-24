# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('course_creators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecreator',
            name='note',
            field=models.CharField(help_text='\u5173\u4e8e\u672c\u7528\u6237\u7684\u53ef\u9009\u5907\u6ce8\uff08\u4f8b\u5982\uff0c\u8bfe\u7a0b\u521b\u5efa\u88ab\u62d2\u7edd\u7684\u539f\u56e0\uff09', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='coursecreator',
            name='state',
            field=models.CharField(default=b'unrequested', help_text='\u8bfe\u7a0b\u521b\u5efa\u8005\u5f53\u524d\u72b6\u6001', max_length=24, choices=[(b'unrequested', '\u672a\u8bf7\u6c42\u7684'), (b'pending', '\u6302\u8d77'), (b'granted', '\u5df2\u6388\u6743'), (b'denied', '\u5df2\u62d2\u7edd')]),
        ),
        migrations.AlterField(
            model_name='coursecreator',
            name='state_changed',
            field=models.DateTimeField(help_text='\u72b6\u6001\u6700\u540e\u66f4\u65b0\u65e5\u671f', verbose_name=b'state last updated', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='coursecreator',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, help_text='Studio\u7528\u6237'),
        ),
    ]

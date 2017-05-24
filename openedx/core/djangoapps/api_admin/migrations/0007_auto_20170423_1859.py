# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0006_catalog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiaccessrequest',
            name='reason',
            field=models.TextField(help_text='\u6b64\u7528\u6237\u5e0c\u671b\u8bbf\u95ee API \u7684\u539f\u56e0\u3002'),
        ),
        migrations.AlterField(
            model_name='apiaccessrequest',
            name='status',
            field=models.CharField(default=b'pending', help_text='\u6b64 API \u8bbf\u95ee\u8bf7\u6c42\u7684\u72b6\u6001', max_length=255, db_index=True, choices=[(b'pending', '\u6302\u8d77'), (b'denied', '\u62d2\u7edd'), (b'approved', '\u5df2\u6279\u51c6')]),
        ),
        migrations.AlterField(
            model_name='apiaccessrequest',
            name='website',
            field=models.URLField(help_text='\u4e0e\u6b64 API \u7528\u6237\u76f8\u5173\u7684\u7f51\u7ad9\u7684 URL\u3002'),
        ),
        migrations.AlterField(
            model_name='historicalapiaccessrequest',
            name='reason',
            field=models.TextField(help_text='\u6b64\u7528\u6237\u5e0c\u671b\u8bbf\u95ee API \u7684\u539f\u56e0\u3002'),
        ),
        migrations.AlterField(
            model_name='historicalapiaccessrequest',
            name='status',
            field=models.CharField(default=b'pending', help_text='\u6b64 API \u8bbf\u95ee\u8bf7\u6c42\u7684\u72b6\u6001', max_length=255, db_index=True, choices=[(b'pending', '\u6302\u8d77'), (b'denied', '\u62d2\u7edd'), (b'approved', '\u5df2\u6279\u51c6')]),
        ),
        migrations.AlterField(
            model_name='historicalapiaccessrequest',
            name='website',
            field=models.URLField(help_text='\u4e0e\u6b64 API \u7528\u6237\u76f8\u5173\u7684\u7f51\u7ad9\u7684 URL\u3002'),
        ),
    ]

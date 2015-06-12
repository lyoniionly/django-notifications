# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import monica.contrib.notifications.models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notify_type',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='timestamp',
            field=models.DateTimeField(default=monica.contrib.notifications.models.now),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0014_event_event_hosted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_hosted_by',
        ),
        migrations.AddField(
            model_name='event',
            name='event_hosted_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='hosted_by'),
        ),
    ]

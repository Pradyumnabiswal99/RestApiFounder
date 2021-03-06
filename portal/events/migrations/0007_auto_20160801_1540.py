# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20160720_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='hosted_by',
            field=models.ManyToManyField(blank=True, related_name='hosted_events', to='startups.startUp'),
        ),
    ]

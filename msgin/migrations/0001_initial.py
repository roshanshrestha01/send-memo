# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_content', models.TextField()),
                ('send_time', models.DateTimeField(null=True, verbose_name=b'scheduled date', blank=True)),
                ('status', models.CharField(default=b'OUTBOX', max_length=6, choices=[(b'OUTBOX', b'Outbox'), (b'SEND', b'Send'), (b'SEEN', b'Received')])),
                ('group_receiver', models.ManyToManyField(to='auth.Group', null=True, blank=True)),
                ('sender', models.ForeignKey(related_name=b'message_sender', to=settings.AUTH_USER_MODEL)),
                ('user_recieiver', models.ManyToManyField(related_name=b'message_receiver', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
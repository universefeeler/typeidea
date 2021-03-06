# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-15 17:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('status', models.PositiveIntegerField(choices=[(1, b'\xe5\x8f\xaf\xe7\x94\xa8'), (2, b'\xe5\x88\xa0\xe9\x99\xa4')], default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('is_nav', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe5\xaf\xbc\xe8\x88\xaa')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('desc', models.CharField(blank=True, max_length=255, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81')),
                ('content', models.TextField(help_text=b'\xe6\xb3\xa8: \xe7\x9b\xae\xe5\x89\x8d\xe4\xbb\x85\xe6\x94\xaf\xe6\x8c\x81Markdown\xe6\xa0\xbc\xe5\xbc\x8f\xe6\x95\xb0\xe6\x8d\xae', verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('status', models.IntegerField(choices=[(1, b'\xe4\xb8\x8a\xe7\xba\xbf'), (2, b'\xe8\x8d\x89\xe7\xa8\xbf'), (3, b'\xe5\x88\xa0\xe9\x99\xa4')], default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('created_time', models.TimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('status', models.PositiveIntegerField(choices=[(1, b'\xe6\xad\xa3\xe5\xb8\xb8'), (2, b'\xe5\x88\xa0\xe9\x99\xa4')], default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
    ]

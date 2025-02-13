# Generated by Django 5.1 on 2025-02-13 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_heart_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbor',
            name='request_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='comment_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='게시판', max_length=50, null=True),
        ),
    ]

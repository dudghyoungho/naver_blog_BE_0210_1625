# Generated by Django 5.1 on 2025-02-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_profile_urlname_profile_urlname_edit_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='urlname',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]

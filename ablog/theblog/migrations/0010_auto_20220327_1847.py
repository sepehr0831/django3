# Generated by Django 3.2 on 2022-03-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_auto_20220327_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
    ]

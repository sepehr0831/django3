# Generated by Django 3.2 on 2022-04-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0020_auto_20220330_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
    ]

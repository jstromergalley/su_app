# Generated by Django 3.1.2 on 2020-10-20 20:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0004_auto_20201020_1715'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='song',
            unique_together={('username', 'artist', 'name')},
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-14 00:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_remove_userprofile_email_remove_userprofile_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Details',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-13 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_activity_userprofile_delete_profile_alter_team_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='id_activitate',
        ),
        migrations.AddField(
            model_name='team',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='users.activity'),
        ),
    ]

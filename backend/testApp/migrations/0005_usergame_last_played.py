# Generated by Django 5.1.6 on 2025-03-25 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0004_games_genres_delete_gamegenre'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergame',
            name='last_played',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

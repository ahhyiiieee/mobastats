# Generated by Django 3.2.3 on 2021-06-18 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_alter_game_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='hero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='players.playerhero'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hero',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='playerhero',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

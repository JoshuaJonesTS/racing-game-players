# Generated by Django 3.2.20 on 2023-08-07 22:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('playersapp', '0006_alter_player_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='vehicle',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]

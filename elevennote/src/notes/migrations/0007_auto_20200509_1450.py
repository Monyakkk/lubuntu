# Generated by Django 2.0.1 on 2020-05-09 14:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_note_shared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='shared',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

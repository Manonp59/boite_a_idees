# Generated by Django 4.1 on 2023-03-24 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0007_alter_idea_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 24, 9, 18, 16, 980499, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='titre',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]

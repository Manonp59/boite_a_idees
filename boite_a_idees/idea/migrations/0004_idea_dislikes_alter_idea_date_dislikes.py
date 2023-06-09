# Generated by Django 4.1 on 2023-03-23 11:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('idea', '0003_idea_likes_idea_user_alter_idea_date_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='dislikes',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 23, 11, 18, 18, 524647, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Dislikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idea_dislikes', to='idea.idea')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_dislikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

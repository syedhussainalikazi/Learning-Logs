# Generated by Django 4.2.13 on 2024-06-08 09:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_remove_topic_date_added_topic_text2'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

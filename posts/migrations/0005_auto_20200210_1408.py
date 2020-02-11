# Generated by Django 3.0.3 on 2020-02-10 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_posts_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

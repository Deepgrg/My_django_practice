# Generated by Django 3.0.3 on 2020-02-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]

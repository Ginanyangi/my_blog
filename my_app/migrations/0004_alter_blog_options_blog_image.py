# Generated by Django 5.0.6 on 2024-06-07 09:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_rename_created_date_blog_last_updated_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]

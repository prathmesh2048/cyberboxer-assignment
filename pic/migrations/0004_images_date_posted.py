# Generated by Django 3.2.7 on 2021-09-18 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0003_alter_images_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

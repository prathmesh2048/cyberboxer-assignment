# Generated by Django 3.2.7 on 2021-09-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='images',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='images',
            name='name',
        ),
        migrations.AddField(
            model_name='images',
            name='image_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
# Generated by Django 3.2.9 on 2021-11-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='small_img',
            field=models.ImageField(null=True, upload_to='small_img'),
        ),
    ]

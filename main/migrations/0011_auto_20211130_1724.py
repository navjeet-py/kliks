# Generated by Django 3.2.9 on 2021-11-30 11:54

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_profilepic_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='small_img',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=80, size=[1024, 768], upload_to='small_img'),
        ),
        migrations.AlterField(
            model_name='profilepic',
            name='pp',
            field=django_resized.forms.ResizedImageField(crop=None, default='static_imgs/default_pp.jpeg', force_format='PNG', keep_meta=True, quality=90, size=[1000, 1000], upload_to='profile_pics'),
        ),
    ]

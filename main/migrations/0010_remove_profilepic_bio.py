# Generated by Django 3.2.9 on 2021-11-29 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_profilepic_pp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepic',
            name='bio',
        ),
    ]
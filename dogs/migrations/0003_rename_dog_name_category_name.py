# Generated by Django 3.2.9 on 2022-05-04 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0002_auto_20220504_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='dog_name',
            new_name='name',
        ),
    ]
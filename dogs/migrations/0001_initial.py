# Generated by Django 3.2.9 on 2022-04-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_name', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

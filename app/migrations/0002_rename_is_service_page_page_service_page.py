# Generated by Django 4.1 on 2023-12-22 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='is_service_page',
            new_name='service_page',
        ),
    ]
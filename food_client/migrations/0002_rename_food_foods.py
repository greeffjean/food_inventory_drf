# Generated by Django 3.2.5 on 2021-07-01 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_client', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Foods',
            new_name='Food',
        ),
    ]

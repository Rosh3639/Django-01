# Generated by Django 3.2.4 on 2021-06-23 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_alter_contact_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='description',
            new_name='desc',
        ),
    ]
# Generated by Django 4.1.3 on 2024-01-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpreeApp', '0003_user_data_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity_data',
            name='description',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='entity_type',
            name='description',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='user_roles',
            name='description',
            field=models.TextField(default='', null=True),
        ),
    ]

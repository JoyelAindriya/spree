# Generated by Django 4.2.7 on 2024-03-21 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpreeApp', '0028_usertoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SpreeApp.user_data'),
        ),
    ]

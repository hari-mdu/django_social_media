# Generated by Django 5.0 on 2024-01-07 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_users_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]

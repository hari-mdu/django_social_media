# Generated by Django 5.0 on 2024-01-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_created_on_alter_users_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
    ]

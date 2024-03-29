# Generated by Django 5.0 on 2024-01-07 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='deleted_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='modified_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='profile_image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='userid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

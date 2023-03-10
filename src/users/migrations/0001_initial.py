# Generated by Django 4.1.6 on 2023-02-07 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('user', models.OneToOneField(db_column='user_uid', on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='admin_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'admin_profile',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('user', models.OneToOneField(db_column='user_uid', on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='author', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'author',
            },
        ),
    ]

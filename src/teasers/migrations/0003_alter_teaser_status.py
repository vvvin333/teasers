# Generated by Django 4.1.6 on 2023-02-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teasers', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teaser',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('denied', 'Denied')], default='pending', max_length=16),
        ),
    ]

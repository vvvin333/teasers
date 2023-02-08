# Generated by Django 4.1.6 on 2023-02-07 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teasers', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaser',
            name='author',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.PROTECT, related_name='teasers', related_query_name='teaser', to='users.author'),
        ),
    ]
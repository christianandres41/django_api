# Generated by Django 4.1 on 2022-08-24 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='room',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='django_api.room'),
        ),
    ]
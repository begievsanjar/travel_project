# Generated by Django 4.1.2 on 2022-10-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='Ismingiz',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='Qayerdansiz',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='Sharifingiz',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]

# Generated by Django 3.2.16 on 2022-11-16 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio_tech', '0002_alter_users_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 3.2.16 on 2022-11-16 05:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_user', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('login', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(blank=True, default='', max_length=50)),
                ('birth', models.DateField()),
            ],
        ),
    ]
# Generated by Django 5.0.1 on 2024-03-16 19:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

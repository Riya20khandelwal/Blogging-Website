# Generated by Django 5.0.6 on 2024-05-23 17:09

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(default=False, max_length=200)),
                ('title', models.CharField(default=False, max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('blog_image', models.ImageField(default='', upload_to='blog_images')),
                ('content', models.TextField(default=False)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
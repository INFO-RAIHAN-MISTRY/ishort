# Generated by Django 4.2.4 on 2023-08-16 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(blank=True, max_length=20, verbose_name='Short Url Auto Generated')),
                ('long_url', models.TextField(verbose_name='Long Url')),
                ('url_title', models.CharField(max_length=100, verbose_name='Url Title')),
                ('url_hit_count', models.PositiveIntegerField(default=0, verbose_name='Url Hit Count')),
                ('url_created_at', models.DateField(auto_now=True)),
                ('url_updated_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

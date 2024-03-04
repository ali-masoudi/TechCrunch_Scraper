# Generated by Django 4.2.10 on 2024-03-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='twitter_id',
        ),
        migrations.AddField(
            model_name='author',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter'),
        ),
    ]